from langchain.agents import create_agent
from langchain_core.tools import tool

from agents import model, policy_agent, product_agent

@tool
def ask_product_agent(question: str) -> str:
    """상품 문의를 Product Agent에게 전달합니다."""
    if product_agent is None:
        raise RuntimeError("agents.py의 product_agent TODO를 먼저 완성하세요.")

    result = product_agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].text

@tool
def ask_policy_agent(question: str) -> str:
    """정책 문의를 Policy Agent에게 전달합니다."""
    if policy_agent is None:
        raise RuntimeError("agents.py의 policy_agent TODO를 먼저 완성하세요.")

    result = policy_agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return result["messages"][-1].text

# TODO 3: ask_product_agent와 ask_policy_agent를 Tool로 사용하는 Supervisor를 만드세요.
supervisor = None
