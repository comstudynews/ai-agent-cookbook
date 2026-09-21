import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """두 정수를 곱합니다."""
    # TODO 1: 실제 곱셈 결과를 반환하세요.
    raise NotImplementedError

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# TODO 2: create_agent()에 model과 multiply Tool을 연결하세요.
agent = None

# TODO 3: "123과 456을 곱해 주세요."를 Agent에게 전달하세요.
