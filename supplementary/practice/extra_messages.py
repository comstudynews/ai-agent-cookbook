# TODO: 보충 실습 개념을 변경해 실행 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

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
