from langchain_core.tools import tool

PRODUCTS = {
    "노트북": {"stock": 4, "price": 1_300_000},
    "모니터": {"stock": 0, "price": 320_000},
}

POLICIES = {
    "환불": "결제 후 7일 이내이며 사용하지 않은 상품은 환불 요청이 가능합니다.",
    "교환": "불량 상품은 수령 후 7일 이내 교환 요청이 가능합니다.",
}

@tool
def get_product_info(name: str) -> str:
    """상품명으로 재고와 가격을 조회합니다."""
    item = PRODUCTS.get(name)
    if item is None:
        return "상품을 찾을 수 없습니다."
    return f"{name}: 재고 {item['stock']}개, 가격 {item['price']}원"

@tool
def get_policy(keyword: str) -> str:
    """환불 또는 교환 정책을 조회합니다."""
    return POLICIES.get(keyword, "관련 정책을 찾지 못했습니다.")
