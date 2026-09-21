import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

PRODUCTS = {
    "노트북": {"stock": 4, "price": 1_300_000},
    "모니터": {"stock": 0, "price": 320_000},
}

POLICIES = {
    "환불": "결제 후 7일 이내이며 사용하지 않은 상품은 환불 요청이 가능합니다.",
    "교환": "불량 상품은 수령 후 7일 이내 교환 요청이 가능합니다.",
}

@tool
def get_product_info(name: str) -> str:
    """상품명으로 재고와 가격을 조회합니다."""
    item = PRODUCTS.get(name)

    if item is None:
        return "상품을 찾을 수 없습니다."

    return f"{name}: 재고 {item['stock']}개, 가격 {item['price']}원"

@tool
def get_policy(keyword: str) -> str:
    """환불 또는 교환 정책을 조회합니다."""
    return POLICIES.get(
        keyword,
        "관련 정책을 찾지 못했습니다.",
    )

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

product_agent = create_agent(
    model=model,
    tools=[get_product_info],
    system_prompt=(
        "상품 재고와 가격은 반드시 "
        "get_product_info 도구로 확인하세요."
    ),
)

policy_agent = create_agent(
    model=model,
    tools=[get_policy],
    system_prompt=(
        "정책 질문은 반드시 "
        "get_policy 도구로 확인하세요."
    ),
)

@tool
def ask_product_agent(question: str) -> str:
    """상품 재고와 가격 문의를 상품 전문 Agent에 전달합니다."""
    print("[SUPERVISOR -> PRODUCT]")

    result = product_agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    return result["messages"][-1].text

@tool
def ask_policy_agent(question: str) -> str:
    """환불과 교환 정책 문의를 정책 전문 Agent에 전달합니다."""
    print("[SUPERVISOR -> POLICY]")

    result = policy_agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    return result["messages"][-1].text

supervisor = create_agent(
    model=model,
    tools=[
        ask_product_agent,
        ask_policy_agent,
    ],
    system_prompt=(
        "당신은 고객지원 Supervisor입니다. "
        "상품 정보가 필요하면 ask_product_agent를 사용하고, "
        "정책 정보가 필요하면 ask_policy_agent를 사용하세요. "
        "복합 질문이면 필요한 두 Agent를 모두 사용한 뒤 "
        "결과를 합쳐 답하세요."
    ),
    middleware=[
        ModelCallLimitMiddleware(
            run_limit=8,
            exit_behavior="end",
        )
    ],
)

def run_service(question: str) -> dict:
    return supervisor.invoke({
        "messages": [{
            "role": "user",
            "content": question,
        }]
    })

if __name__ == "__main__":
    question = (
        "모니터 재고를 확인하고, "
        "구매 후 환불 가능 기간도 알려 주세요."
    )

    result = run_service(question)
    answer = result["messages"][-1].text

    print(answer)

    used_tools = []

    for message in result["messages"]:
        for call in getattr(message, "tool_calls", []):
            used_tools.append(call["name"])

    print("호출된 Tool:", used_tools)

    required_tools = {
        "ask_product_agent",
        "ask_policy_agent",
    }

    missing = required_tools - set(used_tools)

    print("필수 Tool 누락:", missing or "없음")
