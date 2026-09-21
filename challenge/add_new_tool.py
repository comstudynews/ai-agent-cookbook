from langchain_core.tools import tool

@tool
def discount_price(price: int, rate: float) -> int:
    """상품 가격과 할인율을 받아 최종 가격을 계산합니다."""
    # TODO: rate는 0.0~1.0 범위라고 가정하고 최종 가격을 반환하세요.
    raise NotImplementedError

# 예시
# print(discount_price.invoke({"price": 100000, "rate": 0.1}))
