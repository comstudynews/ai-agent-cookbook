from typing import Literal, TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    draft: str
    attempt_count: int

def improve(state: State) -> dict:
    # 시도 횟수를 1 증가시킵니다.
    attempt = state["attempt_count"] + 1

    # 학습용으로 매번 문장을 하나 추가합니다.
    draft = state["draft"] + f" 개선문장{attempt}."

    print(f"[improve] attempt={attempt}, length={len(draft)}")

    # State를 직접 수정하지 않고 변경할 값만 반환합니다.
    return {
        "draft": draft,
        "attempt_count": attempt,
    }

def decide(state: State) -> Literal["retry", "end"]:
    # TODO 1: 3회 미만이면 retry, 아니면 end를 반환하세요.
    ...

builder = StateGraph(State)
builder.add_node("improve", improve)
builder.add_edge(START, "improve")

# decide()가 반환한 문자열을 실제 다음 경로와 연결합니다.
# TODO 2: decide() 결과에 따라 반복/종료되는 conditional edge를 연결하세요.

graph = builder.compile()

result = graph.invoke({
    "draft": "초안.",
    "attempt_count": 0,
})

print("최종 시도 횟수:", result["attempt_count"])
print("최종 초안:", result["draft"])
