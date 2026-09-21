from typing import Literal

Category = Literal["product", "policy", "shipping", "other"]

def route_by_keyword(question: str) -> Category:
    """LLM을 붙이기 전, 규칙 기반으로 Routing 기준을 먼저 확인하는 연습입니다."""
    text = question.lower()

    if any(word in text for word in ["재고", "가격", "상품"]):
        return "product"
    if any(word in text for word in ["환불", "교환", "정책"]):
        return "policy"

    # TODO: 배송 관련 키워드 조건을 추가하세요.

    return "other"

if __name__ == "__main__":
    samples = [
        "모니터 재고 알려줘",
        "환불 기간 알려줘",
        "언제 배송되나요?",
        "안녕하세요",
    ]

    for sample in samples:
        print(sample, "->", route_by_keyword(sample))
