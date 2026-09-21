import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# TODO 1: model.invoke()로 질문을 전달하세요.
response = None

# TODO 2: AIMessage에서 텍스트 응답을 출력하세요.
print(response)
