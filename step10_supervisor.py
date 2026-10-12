import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

# 첫 번째 전문 Agent: 핵심 사실만 정리합니다.
research_agent = create_agent(
    model=model,
    tools=[],
    system_prompt="주어진 주제에서 핵심 사실을 3개 이내로 정리하세요.",
)

# 두 번째 전문 Agent: 받은 내용을 학습자용 문장으로 바꿉니다.
writer_agent = create_agent(
    model=model,
    tools=[],
    system_prompt="주어진 정보를 초보자가 이해하기 쉬운 짧은 설명으로 작성하세요.",
)

# 전문 Agent 자체를 Supervisor가 호출할 수 있는 Tool로 감쌉니다.
@tool
def research_task(topic: str) -> str:
    """주제의 핵심 사실을 조사하는 전문 Agent를 호출합니다."""

    print(f"[SUPERVISOR -> RESEARCH] {topic}")

    result = research_agent.invoke({
        "messages": [{"role": "user", "content": topic}]
    })

    return result["messages"][-1].text

@tool
def writing_task(context: str) -> str:
    """정리된 정보를 학습자용 설명으로 작성하는 전문 Agent를 호출합니다."""

    print("[SUPERVISOR -> WRITER]")

    result = writer_agent.invoke({
        "messages": [{"role": "user", "content": context}]
    })

    return result["messages"][-1].text

# Supervisor는 두 전문 Agent를 Tool처럼 사용합니다.
supervisor = create_agent(
    model=model,
    tools=[research_task, writing_task],
    system_prompt=(
        "당신은 Supervisor입니다. 사용자가 설명을 요청하면 "
        "반드시 research_task를 먼저 호출하고, "
        "그 결과를 writing_task에 전달한 뒤 답하세요."
    ),
)

result = supervisor.invoke({
    "messages": [
        {"role": "user", "content": "AI Agent의 핵심 특징을 설명해 주세요."}
    ]
})

print(result["messages"][-1].text)
