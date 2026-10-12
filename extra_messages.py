from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[list, add_messages]

before = [HumanMessage(content="첫 질문", id="user-1")]
added = add_messages(before, [AIMessage(content="첫 답변", id="ai-1")])
replaced = add_messages(added, [HumanMessage(content="수정된 질문", id="user-1")])

print("추가 후 개수:", len(added))
print("교체 후 개수:", len(replaced))
print("첫 메시지:", replaced[0].content)
