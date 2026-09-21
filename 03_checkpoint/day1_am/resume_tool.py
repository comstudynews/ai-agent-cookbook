import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """두 정수를 곱합니다."""
    print(f"[TOOL] multiply({a}, {b})")
    return a * b

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

agent = create_agent(
    model=model,
    tools=[multiply],
    system_prompt="곱셈은 반드시 multiply 도구를 사용하세요.",
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "12와 8을 곱해 주세요."}]
})

print(result["messages"][-1].text)
