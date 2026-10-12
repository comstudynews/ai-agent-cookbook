# TODO: 호출·재시도·기억 제한 비교 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

import os
from dotenv import load_dotenv
from langchain.agents import create_agent

# 미들웨어는 Agent 실행 전후에 공통 제어 기능을 삽입합니다.
from langchain.agents.middleware import ModelCallLimitMiddleware

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """두 정수를 더합니다."""
    print(f"[TOOL] add({a}, {b})")
    return a + b

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

agent = create_agent(
    model=model,
    tools=[add],
    system_prompt="덧셈은 반드시 add 도구를 사용하세요.",

    # 모델 호출 최대 4회
    middleware=[
        ModelCallLimitMiddleware(
            run_limit=4,
            exit_behavior="end",
        )
    ],
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "100과 250을 더해 주세요."}
    ]
})

print(result["messages"][-1].text)
