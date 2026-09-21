import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

# 실제 DB 대신 학습용 상품 데이터를 메모리에 준비합니다.
PRODUCTS = {
    "노트북": {"stock": 4, "price": 1_300_000},
    "모니터": {"stock": 0, "price": 320_000},
    "키보드": {"stock": 12, "price": 95_000},
}

@tool
def get_product_info(name: str) -> str:
    """상품명으로 재고와 가격을 조회합니다."""

    # Tool 실행 여부를 눈으로 확인합니다.
    print(f"[TOOL] get_product_info({name})")

    item = PRODUCTS.get(name)

    # 존재하지 않는 상품도 예외 대신 설명 가능한 문자열로 반환합니다.
    if item is None:
        return "상품을 찾을 수 없습니다."

    return f"{name}: 재고 {item['stock']}개, 가격 {item['price']}원"

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

agent = create_agent(
    model=model,
    # TODO: 상품 조회 Tool을 Agent에 연결하세요.
    tools=[...],
    system_prompt=(
        "상품의 재고나 가격에 관한 질문은 반드시 get_product_info 도구로 확인하세요. "
        "재고가 0이면 품절이라고 안내하세요."
    ),
)

result = agent.invoke({
    "messages": [
        {"role": "user", "content": "모니터를 지금 주문할 수 있나요?"}
    ]
})

print(result["messages"][-1].text)
