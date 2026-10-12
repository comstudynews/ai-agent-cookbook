import operator
import os
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from langgraph.types import Send
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

class TaskPlan(BaseModel):
    tasks: list[str] = Field(
        min_length=2,
        max_length=3,
        description="독립적으로 조사할 하위 작업 2~3개",
    )

planner = model.with_structured_output(TaskPlan)

class State(TypedDict):
    topic: str
    tasks: list[str]
    outputs: Annotated[list[dict[str, str]], operator.add]
    report: str

class WorkerState(TypedDict):
    task: str
    outputs: Annotated[list[dict[str, str]], operator.add]

def orchestrator(state: State) -> dict:
    plan = planner.invoke(
        "다음 주제를 서로 독립적인 조사 작업 2~3개로 나누세요. "
        f"주제: {state['topic']}"
    )
    print("[PLAN]", plan.tasks)
    return {"tasks": plan.tasks}

def assign_workers(state: State) -> list[Send]:
    # 계획한 작업마다 독립적인 Worker 입력을 보냅니다.
    return [Send("worker", {"task": task}) for task in state["tasks"]]

def worker(state: WorkerState) -> dict:
    task = state["task"]
    response = model.invoke(
        f"다음 작업을 한국어 2문장으로 정리하세요: {task}. "
        "검증하지 않은 숫자나 출처는 만들지 마세요."
    )
    print("[WORKER]", task)
    return {"outputs": [{"task": task, "text": response.text}]}

def synthesize(state: State) -> dict:
    # 병렬 완료 순서와 관계없이 보고서 순서를 안정적으로 정렬합니다.
    outputs = sorted(state["outputs"], key=lambda x: x["task"])
    report = "\n\n".join(
        f"## {item['task']}\n{item['text']}" for item in outputs
    )
    return {"report": report}

builder = StateGraph(State)
builder.add_node("orchestrator", orchestrator)
builder.add_node("worker", worker)
builder.add_node("synthesize", synthesize)
builder.add_edge(START, "orchestrator")
builder.add_conditional_edges(
    "orchestrator", assign_workers, ["worker"]
)
builder.add_edge("worker", "synthesize")
builder.add_edge("synthesize", END)
graph = builder.compile()

result = graph.invoke({
    "topic": "AI Agent 서비스의 운영 고려사항",
    "tasks": [],
    "outputs": [],
    "report": "",
})
print("실행된 작업 수:", len(result["outputs"]))
print(result["report"])
