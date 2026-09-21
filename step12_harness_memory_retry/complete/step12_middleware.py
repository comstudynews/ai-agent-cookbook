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

    # 한 번의 Agent 실행에서 모델 호출 횟수를 최대 4회로 제한합니다.
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
