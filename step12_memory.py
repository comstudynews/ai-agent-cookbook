import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

agent = create_agent(
    model=model,
    tools=[],
    checkpointer=InMemorySaver(),
    system_prompt="이 대화에서 사용자가 알려준 정보를 기억해 답하세요.",
)

config = {
    "configurable": {
        "thread_id": "memory-demo-1"
    }
}

first = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "제가 관심 있는 분야는 AI Agent입니다."}
        ]
    },
    config,
)

print("1차 응답:", first["messages"][-1].text)

second = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "제가 관심 있다고 한 분야가 무엇이었죠?"}
        ]
    },
    config,
)

print("2차 응답:", second["messages"][-1].text)
