# TODO: Supervisor·Swarm 역할 교체 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph_swarm import create_handoff_tool, create_swarm

load_dotenv()

@tool
def product_info(name: str) -> str:
    """상품명으로 재고를 확인합니다."""
    print(f"[PRODUCT TOOL] {name}")
    stock = {"모니터": 0, "노트북": 4}
    return f"{name} 재고: {stock[name]}개" if name in stock else "상품 없음"

@tool
def refund_policy(keyword: str) -> str:
    """환불 또는 교환 정책을 확인합니다."""
    print(f"[POLICY TOOL] {keyword}")
    policies = {
        "환불": "결제 후 7일 이내 미사용 상품 환불 가능",
        "교환": "수령 후 7일 이내 불량품 교환 가능",
    }
    return policies.get(keyword, "해당 정책을 찾지 못했습니다.")

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

product_agent = create_agent(
    model=model,
    name="product_agent",
    tools=[
        product_info,
        create_handoff_tool(
            agent_name="policy_agent",
            description="환불·교환 정책 문의를 정책 담당에게 넘깁니다.",
        ),
    ],
    system_prompt=(
        "당신은 상품 담당입니다. 상품 재고는 product_info로 확인하세요. "
        "환불·교환 문의는 정책 담당 Agent로 Handoff하세요."
    ),
)

policy_agent = create_agent(
    model=model,
    name="policy_agent",
    tools=[
        refund_policy,
        create_handoff_tool(
            agent_name="product_agent",
            description="상품 재고 문의를 상품 담당에게 넘깁니다.",
        ),
    ],
    system_prompt=(
        "당신은 정책 담당입니다. 정책은 refund_policy로 확인하세요. "
        "상품 재고 문의는 상품 담당 Agent로 Handoff하세요."
    ),
)

workflow = create_swarm(
    agents=[product_agent, policy_agent],
    default_active_agent="product_agent",
)
app = workflow.compile(checkpointer=InMemorySaver())

# 같은 thread_id로 세 번 질문하여 담당 Agent가 유지되는지 확인합니다.
config = {"configurable": {"thread_id": "swarm-demo-1"}}
questions = [
    "모니터 재고를 확인해 주세요.",
    "환불 담당 Agent에게 연결해서 환불 가능 기간을 알려 주세요.",
    "방금 설명한 환불 가능 기간을 다시 알려 주세요.",
]

for turn, question in enumerate(questions, 1):
    result = app.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config=config,
    )
    print(f"\n[TURN {turn}] 질문: {question}")
    print("현재 담당:", result.get("active_agent"))
    print("답변:", result["messages"][-1].text)
