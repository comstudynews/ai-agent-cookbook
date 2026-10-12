# TODO: 보충 실습 개념을 변경해 실행 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

class State(TypedDict):
    messages: Annotated[list, add_messages]

def reply(state: State) -> dict:
    last = state["messages"][-1].content
    return {"messages": [AIMessage(content=f"확인: {last}")]}

builder = StateGraph(State)
builder.add_node("reply", reply)
builder.add_edge(START, "reply")
builder.add_edge("reply", END)
graph = builder.compile(checkpointer=InMemorySaver())

a = {"configurable": {"thread_id": "class-a"}}
b = {"configurable": {"thread_id": "class-b"}}

graph.invoke({"messages": [HumanMessage(content="A의 첫 질문")]}, config=a)
graph.invoke({"messages": [HumanMessage(content="B의 첫 질문")]}, config=b)
graph.invoke({"messages": [HumanMessage(content="A의 두 번째 질문")]}, config=a)

for name, config in [("A", a), ("B", b)]:
    snapshot = graph.get_state(config)
    messages = snapshot.values["messages"]
    print(name, "메시지 수:", len(messages))
    print(name, "첫 질문:", messages[0].content)
