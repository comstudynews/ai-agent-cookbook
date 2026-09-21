import os
from typing import Literal

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

class SupportResult(BaseModel):
    category: Literal["product", "policy", "other"]
    request: str
    confidence: float = Field(ge=0.0, le=1.0)

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# TODO 1: response_format에 ToolStrategy(SupportResult)를 지정하세요.
agent = None

# TODO 2: 문의를 전달한 뒤 result["structured_response"]을 확인하세요.
