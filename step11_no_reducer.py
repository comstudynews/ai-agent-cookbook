from typing import TypedDict
from langgraph.errors import InvalidUpdateError
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    results: list[str]  # Reducer 없음

def a(state: State) -> dict:
    return {"results": ["A"]}

def b(state: State) -> dict:
    return {"results": ["B"]}

builder = StateGraph(State)
builder.add_node("a", a)
builder.add_node("b", b)
builder.add_edge(START, "a")
builder.add_edge(START, "b")
builder.add_edge("a", END)
builder.add_edge("b", END)
graph = builder.compile()

try:
    graph.invoke({"results": []})
except InvalidUpdateError as error:
    print("예상 오류:", type(error).__name__)
