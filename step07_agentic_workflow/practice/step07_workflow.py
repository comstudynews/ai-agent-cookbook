from typing import Literal, TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    goal: str
    plan: list[str]
    execution: list[str]
    passed: bool
    retry_count: int

def plan_node(state: State) -> dict:
    # Goal을 달성하기 위한 작은 작업으로 분해합니다.
    return {"plan": ["정보 수집", "초안 작성", "검토"]}

def execute_node(state: State) -> dict:
    # 학습용 예제에서는 각 계획이 실행되었다고 표시합니다.
    execution = [f"완료: {task}" for task in state["plan"]]
    return {"execution": execution}

def reflect_node(state: State) -> dict:
    # 세 작업이 모두 수행되었는지 검사합니다.
    passed = len(state["execution"]) == 3
    return {"passed": passed}

def route_after_reflect(state: State) -> Literal["end", "retry"]:
    # TODO: passed와 retry_count를 기준으로 end/retry를 결정하세요.
    ...

def retry_node(state: State) -> dict:
    return {"retry_count": state["retry_count"] + 1}

builder = StateGraph(State)
builder.add_node("plan", plan_node)
builder.add_node("execute", execute_node)
builder.add_node("reflect", reflect_node)
builder.add_node("retry", retry_node)

builder.add_edge(START, "plan")
builder.add_edge("plan", "execute")
builder.add_edge("execute", "reflect")

builder.add_conditional_edges(
    "reflect",
    route_after_reflect,
    {
        "end": END,
        "retry": "retry",
    },
)

builder.add_edge("retry", "plan")

graph = builder.compile()

result = graph.invoke({
    "goal": "간단한 기술 보고서 작성",
    "plan": [],
    "execution": [],
    "passed": False,
    "retry_count": 0,
})

print("Goal:", result["goal"])
print("Plan:", result["plan"])
print("Execute:", result["execution"])
print("Reflect passed:", result["passed"])
