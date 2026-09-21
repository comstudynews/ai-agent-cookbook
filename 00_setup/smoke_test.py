import os
import sys
from importlib.metadata import version

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

required = [
    "langchain",
    "langchain-openai",
    "langgraph",
    "python-dotenv",
    "pydantic",
]

print(f"[PASS] Python {sys.version.split()[0]}")
for package in required:
    print(f"[PASS] {package} {version(package)}")

api_key = os.getenv("OPENAI_API_KEY")
model_name = os.getenv("OPENAI_MODEL")
if not api_key or not model_name:
    raise RuntimeError(".env의 OPENAI_API_KEY와 OPENAI_MODEL을 확인하세요.")

print("[PASS] 환경변수")

model = ChatOpenAI(model=model_name, use_responses_api=True)
response = model.invoke("OK라고만 답하세요.")
print("[PASS] LLM connection:", response.text)

@tool
def multiply(a: int, b: int) -> int:
    """두 정수를 곱합니다."""
    return a * b

agent = create_agent(
    model=model,
    tools=[multiply],
    system_prompt="곱셈은 반드시 multiply 도구를 사용하세요.",
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "6과 7을 곱해 주세요."}]
})

tool_names = []
for message in result["messages"]:
    for call in getattr(message, "tool_calls", []):
        tool_names.append(call["name"])

if "multiply" not in tool_names:
    raise RuntimeError("Tool Calling 확인 실패")

print("[PASS] Tool Calling")
print("Smoke Test 완료")
