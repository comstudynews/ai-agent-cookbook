from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command

class State(TypedDict):
    request: str
    active_agent: str
    result: str

def tech_agent(state: State) -> Command:
    # 현재 요청이 결제 관련이면 직접 처리하지 않고 다음 Agent로 넘깁니다.
    if "결제" in state["request"]:
        print("[tech_agent] 결제 담당에게 Handoff")

        return Command(
            update={"active_agent": "billing_agent"},
            goto="billing_agent",
        )

    return Command(
        update={
            "active_agent": "tech_agent",
            "result": "기술 문의 처리 완료",
        },
        goto=END,
    )

def billing_agent(state: State) -> Command:
    print("[billing_agent] 결제 문의 처리")

    return Command(
        update={
            "active_agent": "billing_agent",
            "result": "결제 문의 처리 완료",
        },
        goto=END,
    )

builder = StateGraph(State)
builder.add_node("tech_agent", tech_agent)
builder.add_node("billing_agent", billing_agent)

# 첫 진입은 tech_agent로 시작합니다.
builder.add_edge(START, "tech_agent")

graph = builder.compile()

result = graph.invoke({
    "request": "결제 오류가 발생했습니다.",
    "active_agent": "tech_agent",
    "result": "",
})

print("최종 담당:", result["active_agent"])
print("결과:", result["result"])
