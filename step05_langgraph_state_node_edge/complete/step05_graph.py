from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# State에 text와 result라는 두 값을 보관한다고 선언합니다.
class State(TypedDict):
    text: str
    result: str

# Node는 현재 State를 입력받고 변경할 값만 dict로 반환합니다.
def upper_node(state: State) -> dict:
    return {"result": state["text"].upper()}

# State 구조를 사용하는 Graph 설계도를 만듭니다.
builder = StateGraph(State)

# upper_node 함수를 "upper"라는 Node로 등록합니다.
builder.add_node("upper", upper_node)

# START → upper → END 흐름을 연결합니다.
builder.add_edge(START, "upper")
builder.add_edge("upper", END)

# 설계가 끝난 Graph를 실제 실행 가능한 객체로 컴파일합니다.
graph = builder.compile()

result = graph.invoke({
    "text": "hello agent",
    "result": "",
})

print(result)
