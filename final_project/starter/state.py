from typing import TypedDict

class State(TypedDict):
    question: str
    answer: str
    passed: bool
    retry_count: int
    approved: bool | None
