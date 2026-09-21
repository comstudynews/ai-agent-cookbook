import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

response = model.invoke("AI Agent를 한 문장으로 설명해 주세요.")
print(response.text)
