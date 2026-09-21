import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def add(a: int, b: int) -> int:
    """두 정수를 더합니다."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """두 정수를 곱합니다."""
    return a * b

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# TODO 1: add와 multiply를 모두 등록하세요.
agent = None

questions = [
    "35와 27을 더해 주세요.",
    "35와 27을 곱해 주세요.",
]

# TODO 2: 각 질문을 Agent에 전달하고 최종 답변을 출력하세요.
