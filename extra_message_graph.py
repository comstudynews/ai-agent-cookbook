from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]

def reply(state: State) -> dict:
    last = state["messages"][-1].content
    return {"messages": [AIMessage(content=f"입력 확인: {last}")]}

builder = StateGraph(State)
builder.add_node("reply", reply)
builder.add_edge(START, "reply")
builder.add_edge("reply", END)
graph = builder.compile()

result = graph.invoke({"messages": [HumanMessage(content="안녕하세요")]})
for message in result["messages"]:
    print(type(message).__name__, message.content)
