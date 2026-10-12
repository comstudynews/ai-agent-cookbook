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
