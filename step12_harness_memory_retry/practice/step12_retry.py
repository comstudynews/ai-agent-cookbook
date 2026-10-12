# TODO: 호출·재시도·기억 제한 비교 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

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
    retry_policy=RetryPolicy(
        max_attempts=3,
        retry_on=ConnectionError,
    ),
)

builder.add_edge(START, "call_api")
builder.add_edge("call_api", END)

graph = builder.compile()

result = graph.invoke({
    "result": ""
})

print(result["result"])
