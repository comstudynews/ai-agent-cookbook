# TODO: 보충 실습 개념을 변경해 실행 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

from langgraph.graph import START, END, MessagesState, StateGraph

def reply(state: MessagesState) -> dict:
    question = state["messages"][-1].content
    return {
        "messages": [
            {"role": "assistant", "content": f"입력 확인: {question}"}
        ]
    }

builder = StateGraph(MessagesState)
builder.add_node("reply", reply)
builder.add_edge(START, "reply")
builder.add_edge("reply", END)
graph = builder.compile()

result = graph.invoke({
    "messages": [{"role": "user", "content": "안녕하세요"}]
})

for message in result["messages"]:
    print(type(message).__name__, message.content)
