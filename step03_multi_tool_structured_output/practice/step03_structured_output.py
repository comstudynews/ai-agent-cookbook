import os
from typing import Literal

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()


# Structured Output의 형식을 정의합니다.
class SupportResult(BaseModel):
    """고객 문의 분류 결과"""

    category: Literal["product", "policy", "other"] = Field(
        description="문의 유형"
    )

    request: str = Field(
        description="사용자가 실제로 원하는 것을 한 문장으로 요약"
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="분류 확신도"
    )


model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)


agent = create_agent(
    model=model,

    # 실제 업무를 수행하는 Tool은 사용하지 않습니다.
    tools=[],

    # 최종 결과를 SupportResult Schema에 맞는
    # Structured Output으로 받습니다.
    # TODO: SupportResult Schema를 연결하세요.
    response_format=...,

    system_prompt=(
        "사용자 문의를 product, policy, other 중 하나로 분류하고 "
        "요청 내용을 짧게 정리하세요."
    ),
)


result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "모니터 재고를 확인해 주세요."
        }
    ]
})


# Structured Output 결과를 가져옵니다.
structured = result["structured_response"]


print("category:", structured.category)
print("request:", structured.request)
print("confidence:", structured.confidence)
