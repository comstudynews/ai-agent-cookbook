import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model=os.environ["OPENAI_MODEL"], use_responses_api=True)

@tool
def get_shipping_policy(keyword: str) -> str:
    """배송 정책을 조회합니다."""
    return "재고가 있는 상품은 결제 완료 후 순차 발송됩니다."

# TODO 1: 배송 전용 shipping_agent를 만드세요.
shipping_agent = None

# TODO 2: shipping_agent를 Supervisor가 호출할 수 있는 Tool로 감싸세요.
# TODO 3: 기존 Product / Policy Agent와 함께 Supervisor에 등록하세요.
