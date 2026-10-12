# TODO: 보충 실습 개념을 변경해 실행 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

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
