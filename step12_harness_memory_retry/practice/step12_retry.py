from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import RetryPolicy

class State(TypedDict):
    result: str

attempts = {"count": 0}

def unstable_api(state: State) -> dict:
    attempts["count"] += 1
    print(f"[CALL] attempt={attempts['count']}")

    # 앞의 두 번은 일시적 연결 실패를 가정합니다.
    if attempts["count"] < 3:
        raise ConnectionError("temporary connection error")

    return {"result": "외부 API 호출 성공"}

builder = StateGraph(State)

builder.add_node(
    "call_api",
    unstable_api,
    # TODO: ConnectionError를 최대 3회 Retry하도록 설정하세요.
    retry_policy=...,
)

builder.add_edge(START, "call_api")
builder.add_edge("call_api", END)

graph = builder.compile()

result = graph.invoke({
    "result": ""
})

print(result["result"])
