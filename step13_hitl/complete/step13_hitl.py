from typing import TypedDict
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt

class State(TypedDict):
    action: str
    approved: bool | None

def approval_node(state: State) -> dict:
    # interrupt()는 Graph 실행을 중단하고 사람의 입력을 기다립니다.
    approved = interrupt({
        "question": "이 작업을 승인하시겠습니까?",
        "action": state["action"],
    })

    # 재개되면 사람이 전달한 값을 State에 저장합니다.
    return {"approved": bool(approved)}

builder = StateGraph(State)
builder.add_node("approval", approval_node)
builder.add_edge(START, "approval")
builder.add_edge("approval", END)

# Interrupt를 사용하려면 Checkpointer가 필요합니다.
graph = builder.compile(
    checkpointer=InMemorySaver()
)

# 같은 thread_id를 사용해야 중단된 실행을 이어갈 수 있습니다.
config = {
    "configurable": {
        "thread_id": "hitl-demo-1"
    }
}

# 첫 실행은 approval Node에서 중단됩니다.
first = graph.invoke(
    {
        "action": "중요 파일 삭제",
        "approved": None,
    },
    config,
)

print("1차 실행:", first)

# 사용자가 승인했다고 가정하고 같은 Thread를 재개합니다.
second = graph.invoke(
    Command(resume=True),
    config,
)

print("승인 후:", second)
