from typing import TypedDict

from langgraph.graph import END, START, StateGraph

class State(TypedDict):
    text: str
    result: str

def process(state: State) -> dict:
    print("[NODE] process")
    return {"result": state["text"].upper()}

builder = StateGraph(State)
builder.add_node("process", process)
builder.add_edge(START, "process")
builder.add_edge("process", END)

graph = builder.compile()
result = graph.invoke({"text": "hello agent", "result": ""})

print(result)
