from supervisor import supervisor

question = "모니터 재고를 확인하고, 구매 후 환불 가능 기간도 알려 주세요."

if supervisor is None:
    raise RuntimeError("supervisor.py의 TODO를 먼저 완성하세요.")

result = supervisor.invoke({
    "messages": [{"role": "user", "content": question}]
})

print(result["messages"][-1].text)
