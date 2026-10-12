# TODO: 보충 실습 개념을 변경해 실행 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

import os
from typing import Literal

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel, Field

load_dotenv()

@tool
def find_stock(product: str) -> str:
    """상품명으로 학습용 재고 수량을 확인합니다."""
    stocks = {"모니터": 0, "노트북": 4}
    print("[TOOL] 재고 조회:", product)
    if product not in stocks:
        return "등록되지 않은 상품입니다."
    return f"{product} 재고는 {stocks[product]}개입니다."

class SupportOutput(BaseModel):
    category: Literal["stock", "other"] = Field(
        description="재고 문의인지 그 외 문의인지 구분"
    )
    answer: str = Field(description="한국어 고객 안내 문장")

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

agent = create_agent(
    model=model,
    tools=[find_stock],
    system_prompt=(
        "당신은 상품 안내 Agent입니다. 재고 관련 사실은 "
        "find_stock Tool로 확인하고, 없는 정보는 만들지 마세요."
    ),
    response_format=ToolStrategy(SupportOutput),
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": "agent-integration-1"}}

questions = [
    "모니터 재고를 알려 주세요.",
    "방금 문의한 상품을 지금 구매할 수 있나요?",
]

for turn, question in enumerate(questions, 1):
    result = agent.invoke(
        {"messages": [{"role": "user", "content": question}]},
        config=config,
    )
    structured = result["structured_response"]
    print(f"[TURN {turn}]", structured.model_dump())
    print("메시지 수:", len(result["messages"]))
