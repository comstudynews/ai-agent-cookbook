from typing import Literal, TypedDict

from final_service_agent import run_service
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

class State(TypedDict):
    question: str
    answer: str
    passed: bool
    retry_count: int
    approved: bool | None

def call_agent(state: State) -> dict:
    result = run_service(state["question"])
    answer = result["messages"][-1].text

    print("[AGENT] 답변 생성")

    return {
        "answer": answer,
    }

def validate(state: State) -> dict:
    question = state["question"]
    answer = state["answer"]

    checks: list[bool] = []

    # 종합실습의 테스트 질문에 필요한 핵심 사실을 검사합니다.
    if "모니터" in question:
        checks.append("0" in answer)

    if "환불" in question:
        checks.append("7일" in answer)

    passed = all(checks) if checks else bool(answer.strip())

    print(f"[VALIDATE] passed={passed}")

    return {
        "passed": passed,
    }

def route_after_validate(
    state: State,
) -> Literal["end", "retry", "human"]:
    if state["passed"]:
        return "end"

    if state["retry_count"] < 1:
        return "retry"

    return "human"

def retry_node(state: State) -> dict:
    retry_count = state["retry_count"] + 1

    print(f"[RETRY] count={retry_count}")

    return {
        "retry_count": retry_count,
    }

def human_review(state: State) -> dict:
    approved = interrupt({
        "question": "자동 검증에 실패했습니다. 현재 답변을 승인하시겠습니까?",
        "answer": state["answer"],
    })

    return {
        "approved": bool(approved),
    }

builder = StateGraph(State)

builder.add_node("call_agent", call_agent)
builder.add_node("validate", validate)
builder.add_node("retry", retry_node)
builder.add_node("human_review", human_review)

builder.add_edge(START, "call_agent")
builder.add_edge("call_agent", "validate")

builder.add_conditional_edges(
    "validate",
    route_after_validate,
    {
        "end": END,
        "retry": "retry",
        "human": "human_review",
    },
)

builder.add_edge("retry", "call_agent")
builder.add_edge("human_review", END)

graph = builder.compile(
    checkpointer=InMemorySaver()
)

config = {
    "configurable": {
        "thread_id": "final-demo-1"
    }
}

result = graph.invoke(
    {
        "question": (
            "모니터 재고를 확인하고, "
            "구매 후 환불 가능 기간도 알려 주세요."
        ),
        "answer": "",
        "passed": False,
        "retry_count": 0,
        "approved": None,
    },
    config,
)

print("최종 결과:", result)
