# TODO: Tool부터 검증 Graph까지 연결 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

from final_service_agent import (
    get_product_info, get_policy, product_agent, policy_agent,
)

# 1. Tool부터 확인: Tool 호출 자체는 모델 API 요청 없이 실행
print("상품 Tool:", get_product_info.invoke({"name": "모니터"}))
print("정책 Tool:", get_policy.invoke({"keyword": "환불"}))

# 2. 전문 Agent 개별 호출: 모델 API 요청 발생
product_result = product_agent.invoke({
    "messages": [{"role": "user", "content": "모니터 재고는?"}]
})
print("Product Agent:", product_result["messages"][-1].text)

policy_result = policy_agent.invoke({
    "messages": [{"role": "user", "content": "환불 가능 기간은?"}]
})
print("Policy Agent:", policy_result["messages"][-1].text)
