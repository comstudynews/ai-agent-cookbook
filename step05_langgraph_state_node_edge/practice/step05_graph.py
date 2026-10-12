# TODO: State 변경 확인 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# State에 text와 result라는 두 값을 보관한다고 선언합니다.
class State(TypedDict):
    text: str
    result: str

# Node는 현재 State를 입력받고 변경할 값만 dict로 반환합니다.
def upper_node(state: State) -> dict:
    return {"result": state["text"].upper()}

# Graph 생성
builder = StateGraph(State)

# upper_node 함수를 "upper"라는 Node로 등록합니다.
builder.add_node("upper", upper_node)

# START → upper → END 흐름을 연결합니다.
builder.add_edge(START, "upper")
builder.add_edge("upper", END)

# Graph 컴파일
graph = builder.compile()

result = graph.invoke({
    "text": "hello agent",
    "result": "",
})

print(result)
