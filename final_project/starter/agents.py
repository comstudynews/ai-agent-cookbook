import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from tools import get_policy, get_product_info

load_dotenv()

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# TODO 1: 상품 정보는 반드시 get_product_info를 사용하도록 Product Agent를 만드세요.
product_agent = None

# TODO 2: 정책 정보는 반드시 get_policy를 사용하도록 Policy Agent를 만드세요.
policy_agent = None
