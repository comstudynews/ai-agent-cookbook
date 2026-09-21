import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

# 실제 Vector DB 대신 Agent 흐름 확인용 정책 데이터를 준비합니다.
POLICIES = {
    "환불": "결제 후 7일 이내이며 사용하지 않은 상품은 환불 요청이 가능합니다.",
    "배송": "배송은 결제 완료 후 영업일 기준 2~3일이 소요됩니다.",
    "교환": "불량 상품은 수령 후 7일 이내 교환 요청이 가능합니다.",
}

@tool
def retrieve_policy(keyword: str) -> str:
    """환불, 배송, 교환 정책을 키워드로 조회합니다."""

    print(f"[TOOL] retrieve_policy({keyword})")

    # 검색 결과가 없을 때는 임의의 정책을 만들지 않습니다.
    return POLICIES.get(keyword, "관련 정책을 찾지 못했습니다.")

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

agent = create_agent(
    model=model,
    tools=[retrieve_policy],
    system_prompt=(
        "정책 질문에는 반드시 retrieve_policy 도구를 사용하세요. "
        "도구에서 찾지 못한 내용은 임의로 만들지 마세요."
    ),
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "상품 환불은 언제까지 가능한가요?"}
    ]
})

print(result["messages"][-1].text)
