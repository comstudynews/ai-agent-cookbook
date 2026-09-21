import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

# @tool을 붙이면 일반 Python 함수가 Agent가 호출할 수 있는 Tool이 됩니다.
@tool
def multiply(a: int, b: int) -> int:
    """두 정수를 곱합니다. 산술 곱셈이 필요할 때 사용합니다."""

    # 실제 Tool이 호출되었는지 터미널에서 확인하기 위한 로그입니다.
    print(f"[TOOL] multiply({a}, {b})")
    # TODO 1: 두 수의 곱을 반환하세요.
    return ...

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# create_agent는 모델과 Tool을 연결하고 Tool Calling Loop를 구성합니다.
agent = create_agent(
    model=model,
    # TODO 2: multiply Tool을 등록하세요.
    tools=[...],
    system_prompt=(
        "당신은 계산 도우미입니다. "
        "곱셈 계산은 반드시 multiply 도구를 사용하고, 도구 결과를 바탕으로 답하세요."
    ),
)

# Agent에게 사용자 메시지를 전달합니다.
result = agent.invoke({
    "messages": [
        {"role": "user", "content": "123과 456을 곱해 주세요."}
    ]
})

# 마지막 AIMessage의 텍스트만 출력합니다.
print(result["messages"][-1].text)
