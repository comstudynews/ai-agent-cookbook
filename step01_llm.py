import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# .env 파일의 OPENAI_API_KEY와 OPENAI_MODEL을 환경변수로 읽습니다.
load_dotenv()

# 모델 이름을 코드에 고정하지 않고 .env에서 가져옵니다.
model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# 아직 Tool 없이 LLM 자체에 질문합니다.
response = model.invoke("AI Agent를 한 문장으로 설명해 주세요.")

# 최신 LangChain 메시지는 .text 속성으로 텍스트만 안전하게 꺼낼 수 있습니다.
print(response.text)
