import operator
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    topic: str

    # 여러 병렬 Node가 반환한 리스트를 operator.add로 합칩니다.
    results: Annotated[list[str], operator.add]

    final: str

def research_a(state: State) -> dict:
    print("[research_a] 기술 관점 조사 완료")
    return {"results": [f"{state['topic']}: 기술 관점"]}

def research_b(state: State) -> dict:
    print("[research_b] 비즈니스 관점 조사 완료")
    return {"results": [f"{state['topic']}: 비즈니스 관점"]}

def merge(state: State) -> dict:
    print(f"[merge] {len(state['results'])}개 결과 통합 완료")

    # 병렬 완료 순서와 관계없이 최종 문자열 순서를 일정하게 만듭니다.
    final = " | ".join(sorted(state["results"]))

    return {"final": final}

builder = StateGraph(State)
builder.add_node("research_a", research_a)
builder.add_node("research_b", research_b)
builder.add_node("merge", merge)

# START에서 두 Node로 동시에 Fan-out 합니다.
builder.add_edge(START, "research_a")
builder.add_edge(START, "research_b")

# 리스트 형태의 start_key를 사용하면 두 upstream Node가 모두 끝난 뒤 merge가 실행됩니다.
builder.add_edge(["research_a", "research_b"], "merge")

builder.add_edge("merge", END)

graph = builder.compile()

result = graph.invoke({
    "topic": "AI Agent",
    "results": [],
    "final": "",
})

print("Fan-in 확인:", len(result["results"]), "개 결과 모두 수신")
print("최종 결과:", result["final"])
