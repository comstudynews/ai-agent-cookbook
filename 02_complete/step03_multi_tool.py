import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """두 정수를 더합니다."""
    print(f"[TOOL] add({a}, {b})")
    return a + b

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
    tools=[add, multiply],
    system_prompt=(
        "산술 계산은 반드시 제공된 도구를 사용하세요. "
        "덧셈은 add, 곱셈은 multiply를 사용하세요."
    ),
)

for question in ["35와 27을 더해 주세요.", "35와 27을 곱해 주세요."]:
    result = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    print("질문:", question)
    print("답변:", result["messages"][-1].text)
