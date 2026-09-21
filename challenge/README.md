# Challenge

기본 실습을 먼저 끝낸 수강생이 진행하는 추가 과제입니다.

## Challenge 1 — 새 Tool 추가

`add_new_tool.py`

- 할인율을 적용하는 `discount_price` Tool을 구현합니다.
- Type Hint와 Docstring을 명확하게 작성합니다.
- 최소 2개 입력값으로 테스트합니다.

## Challenge 2 — 새 전문 Agent 추가

`add_new_agent.py`

- Shipping Agent를 추가합니다.
- 배송 문의만 담당하도록 Tool 범위를 제한합니다.
- Supervisor가 배송 질문에 Shipping Agent를 선택하도록 확장합니다.

## Challenge 3 — Routing 변경

`modify_routing.py`

- product / policy / shipping / other 네 범주로 분기합니다.
- 모호한 질문은 other로 보내도록 기준을 작성합니다.
