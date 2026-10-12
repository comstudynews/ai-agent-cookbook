from typing import Literal, TypedDict
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt

class State(TypedDict):
    action: str
    approved: bool | None
    status: str

def approval_node(state: State) -> dict:
    answer = interrupt({
        "question": "이 작업을 승인하시겠습니까?",
        "action": state["action"],
    })
    return {"approved": bool(answer)}

def route_approval(state: State) -> Literal["run", "reject"]:
    return "run" if state["approved"] else "reject"

def run_demo(state: State) -> dict:
    # 실제 파일을 삭제하지 않는 모의 실행입니다.
    print("[DEMO] 승인된 작업을 모의 실행")
    return {"status": "승인됨(모의 실행)"}

def reject_demo(state: State) -> dict:
    print("[DEMO] 승인 거절: 작업 미실행")
    return {"status": "거절됨(미실행)"}

builder = StateGraph(State)
builder.add_node("approval", approval_node)
builder.add_node("run", run_demo)
builder.add_node("reject", reject_demo)
builder.add_edge(START, "approval")
builder.add_conditional_edges(
    "approval", route_approval,
    {"run": "run", "reject": "reject"},
)
builder.add_edge("run", END)
builder.add_edge("reject", END)
graph = builder.compile(checkpointer=InMemorySaver())

def test_approval(thread_id: str, decision: bool) -> None:
    config = {"configurable": {"thread_id": thread_id}}
    first = graph.invoke(
        {"action": "중요 파일 삭제", "approved": None, "status": ""},
        config=config,
    )
    print("승인 대기:", "__interrupt__" in first)
    second = graph.invoke(Command(resume=decision), config=config)
    print("승인:", second["approved"], "결과:", second["status"])

test_approval("hitl-approve", True)
test_approval("hitl-reject", False)
