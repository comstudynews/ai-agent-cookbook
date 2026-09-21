from typing import TypedDict

from langgraph.graph import END, START, StateGraph

class State(TypedDict):
    text: str
    result: str

def process(state: State) -> dict:
    return {"result": state["text"].upper()}

builder = StateGraph(State)

# TODO 1: process 노드를 등록하세요.
# TODO 2: START -> process -> END를 연결하세요.
# TODO 3: compile() 후 invoke()를 실행하세요.
