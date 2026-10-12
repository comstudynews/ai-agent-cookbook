import os
from typing import Literal, TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import START, END, StateGraph
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI(
    model=os.environ["OPENAI_MODEL"],
    use_responses_api=True,
)

class Review(BaseModel):
    verdict: Literal["pass", "revise"] = Field(
        description="통과 또는 재작성 필요"
    )
    feedback: str = Field(
        description="수정할 내용. 통과한 경우 짧은 확인 문구"
    )

evaluator = model.with_structured_output(Review)

class State(TypedDict):
    topic: str
    draft: str
    feedback: str
    verdict: str
    attempts: int
    simulate_first_revise: bool

def generator(state: State) -> dict:
    next_attempt = state["attempts"] + 1
    response = model.invoke(
        f"주제: {state['topic']}\n"
        "AI Agent의 의미와 Tool 사용을 한국어 2~4문장으로 설명하세요. "
        f"이전 검토 의견: {state['feedback'] or '없음'}"
    )
    print(f"[GENERATE] {next_attempt}회")
    return {"draft": response.text, "attempts": next_attempt}

def evaluate(state: State) -> dict:
    review = evaluator.invoke(
        "다음 글을 평가하세요. AI Agent의 의미, Tool의 역할, "
        "한국어 2~4문장을 모두 충족하면 pass, 아니면 revise로 판단하세요. "
        "revise라면 구체적 수정 의견을 주세요.\n\n"
        f"{state['draft']}"
    )
    verdict, feedback = review.verdict, review.feedback

    # 학습용: 첫 번만 실패시켜 피드백 루프를 관찰합니다.
    if state["simulate_first_revise"] and state["attempts"] == 1:
        verdict = "revise"
        feedback = "Tool이 실제 작업을 실행한다는 설명을 명확히 보완하세요."

    print(f"[EVALUATE] {verdict}: {feedback}")
    return {"verdict": verdict, "feedback": feedback}

def route(state: State) -> Literal["end", "revise"]:
    if state["verdict"] == "pass" or state["attempts"] >= 2:
        return "end"
    return "revise"

builder = StateGraph(State)
builder.add_node("generator", generator)
builder.add_node("evaluator", evaluate)
builder.add_edge(START, "generator")
builder.add_edge("generator", "evaluator")
builder.add_conditional_edges(
    "evaluator", route,
    {"end": END, "revise": "generator"},
)
graph = builder.compile()

result = graph.invoke({
    "topic": "AI Agent란 무엇인가",
    "draft": "",
    "feedback": "",
    "verdict": "",
    "attempts": 0,
    "simulate_first_revise": True,
})
print("생성 횟수:", result["attempts"])
print("최종 판정:", result["verdict"])
print("최종 글:", result["draft"])
