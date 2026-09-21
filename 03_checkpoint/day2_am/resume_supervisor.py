import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model=os.environ["OPENAI_MODEL"], use_responses_api=True)

@tool
def get_product_info(name: str) -> str:
    """상품의 재고와 가격을 조회합니다."""
    data = {
        "노트북": "재고 4개, 가격 1,300,000원",
        "모니터": "재고 0개, 가격 320,000원",
    }
    return data.get(name, "상품을 찾을 수 없습니다.")

@tool
def get_policy(keyword: str) -> str:
    """교환 또는 환불 정책을 조회합니다."""
    data = {
        "환불": "결제 후 7일 이내이며 사용하지 않은 상품은 환불 요청이 가능합니다.",
        "교환": "불량 상품은 수령 후 7일 이내 교환 요청이 가능합니다.",
    }
    return data.get(keyword, "관련 정책을 찾지 못했습니다.")

product_agent = create_agent(
    model=model,
    tools=[get_product_info],
    system_prompt="상품 사실은 반드시 get_product_info로 확인하세요.",
)

policy_agent = create_agent(
    model=model,
    tools=[get_policy],
    system_prompt="정책 사실은 반드시 get_policy로 확인하세요.",
)

@tool
def ask_product_agent(question: str) -> str:
    """상품 문의를 상품 전문 Agent에게 전달합니다."""
    print("[SUPERVISOR -> PRODUCT]")
    result = product_agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].text

@tool
def ask_policy_agent(question: str) -> str:
    """정책 문의를 정책 전문 Agent에게 전달합니다."""
    print("[SUPERVISOR -> POLICY]")
    result = policy_agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].text

supervisor = create_agent(
    model=model,
    tools=[ask_product_agent, ask_policy_agent],
    system_prompt=(
        "상품 정보는 ask_product_agent, 정책 정보는 ask_policy_agent를 사용하세요. "
        "복합 질문이면 필요한 두 Agent를 모두 사용한 뒤 결과를 합쳐 답하세요."
    ),
)

result = supervisor.invoke({
    "messages": [{
        "role": "user",
        "content": "모니터 재고와 환불 가능 기간을 함께 알려 주세요.",
    }]
})

print(result["messages"][-1].text)
