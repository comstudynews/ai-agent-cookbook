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
    # 정확히 3번 실행한 뒤 종료하도록 결정적 조건을 사용합니다.
    if state["attempt_count"] < 3:
        return "retry"
    return "end"

builder = StateGraph(State)
builder.add_node("improve", improve)
builder.add_edge(START, "improve")

# decide()가 반환한 문자열을 실제 다음 경로와 연결합니다.
builder.add_conditional_edges(
    "improve",
    decide,
    {
        "retry": "improve",
        "end": END,
    },
)

graph = builder.compile()

result = graph.invoke({
    "draft": "초안.",
    "attempt_count": 0,
})

print("최종 시도 횟수:", result["attempt_count"])
print("최종 초안:", result["draft"])
