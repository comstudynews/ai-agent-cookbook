import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model=os.environ["OPENAI_MODEL"], use_responses_api=True)

@tool
def product_lookup(name: str) -> str:
    """상품 정보를 조회합니다."""
    return f"{name}: 재고 4개"

@tool
def policy_lookup(keyword: str) -> str:
    """정책 정보를 조회합니다."""
    return f"{keyword}: 7일 이내 요청 가능"

product_agent = create_agent(
    model=model,
    tools=[product_lookup],
    system_prompt="상품 문의는 product_lookup을 사용하세요.",
)

policy_agent = create_agent(
    model=model,
    tools=[policy_lookup],
    system_prompt="정책 문의는 policy_lookup을 사용하세요.",
)

# TODO 1: product_agent와 policy_agent를 호출하는 Agent-as-Tool 함수를 만드세요.
# TODO 2: 두 Tool을 사용하는 Supervisor Agent를 만드세요.
