from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph

POLICIES = {
    "환불": "결제 후 7일 이내이며 사용하지 않은 상품은 환불 요청이 가능합니다.",
    "배송": "배송은 결제 완료 후 영업일 기준 2~3일이 소요됩니다.",
    "교환": "불량 상품은 수령 후 7일 이내 교환 요청이 가능합니다.",
}

class State(TypedDict):
    keyword: str
    context: str
    found: bool
    retry_count: int

def search_node(state: State) -> dict:
    context = POLICIES.get(state["keyword"], "")
    found = bool(context)

    print(
        f"[SEARCH] keyword={state['keyword']}, "
        f"found={found}, retry={state['retry_count']}"
    )

    return {
        "context": context,
        "found": found,
    }

def route_after_search(state: State) -> Literal["done", "rewrite", "stop"]:
    if state["found"]:
        return "done"

    if state["retry_count"] < 2:
        return "rewrite"

    return "stop"

def rewrite_node(state: State) -> dict:
    # 학습용 결정적 예제입니다.
    # 실제 서비스에서는 LLM이나 검색 전략이 검색어를 다시 만들 수 있습니다.
    keyword = state["keyword"]

    if "배송" in keyword:
        keyword = "배송"
    elif "환불" in keyword:
        keyword = "환불"
    elif "교환" in keyword:
        keyword = "교환"

    return {
        "keyword": keyword,
        "retry_count": state["retry_count"] + 1,
    }

builder = StateGraph(State)
builder.add_node("search", search_node)
builder.add_node("rewrite", rewrite_node)

builder.add_edge(START, "search")

builder.add_conditional_edges(
    "search",
    route_after_search,
    {
        "done": END,
        "rewrite": "rewrite",
        "stop": END,
    },
)

builder.add_edge("rewrite", "search")

graph = builder.compile()

result = graph.invoke({
    "keyword": "배송기간",
    "context": "",
    "found": False,
    "retry_count": 0,
})

print("최종 검색어:", result["keyword"])
print("검색 결과:", result["context"] or "관련 정책을 찾지 못했습니다.")
