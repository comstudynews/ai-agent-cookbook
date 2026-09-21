# AI Agent 설계 및 구축 Cookbook — 실습 소스

이 저장소는 아래 Notion 교재를 수업 진행 기준으로 사용합니다.

- 교재: https://app.notion.com/p/AI-Agent-Cookbook-Step-by-Step-3df91bd5a9ac8167928af84bceafc375

각 Step 폴더에는:
- `practice/` : 수업 중 TODO를 채우는 실습 준비 소스
- `complete/` : 교재 코드 기준 실습 완료 소스

중간에 놓쳤다면 현재 Step의 `complete/`에서 같은 파일명을 찾아 실행한 뒤 다음 Step으로 합류하면 됩니다.

## 진행 순서

1. `step01_llm/` — Step 01 — 가장 단순한 LLM 호출
2. `step02_tool_calling/` — Step 02 — Tool 1개 연결하기
3. `step03_multi_tool_structured_output/` — Step 03 — 여러 Tool 선택과 Structured Output
4. `step04_react_streaming/` — Step 04 — ReAct 흐름과 Streaming
5. `step05_langgraph_state_node_edge/` — Step 05 — LangGraph State, Node, Edge
6. `step06_conditional_loop/` — Step 06 — 조건 분기와 Loop
7. `step07_agentic_workflow/` — Step 07 — Goal → Plan → Execute → Reflect
8. `step08_agentic_rag/` — Step 08 — Retrieval Tool / Agentic RAG Loop
9. `step09_handoff/` — Step 09 — Agent Handoff
10. `step10_supervisor/` — Step 10 — Supervisor / Agent-as-Tool
11. `step11_parallel/` — Step 11 — Fan-out / Fan-in
12. `step12_harness_memory_retry/` — Step 12 — Middleware / Memory / Retry
13. `step13_hitl/` — Step 13 — Human-in-the-Loop
14. `step14_trace_evaluation/` — Step 14 — Trace와 Agent 평가
15. `final_multi_agent/` — Final — 통합 고객지원 Multi-Agent

## 환경

```bash
python -m venv .venv
python -m pip install -r requirements.txt
python check_env.py
```

`.env.example`을 복사해 `.env`를 만들고 본인의 API Key를 설정하세요.

> Complete 소스는 지정된 Notion 교재의 코드와 일치시키는 것을 우선하며, Practice 소스는 그 코드에서 해당 Step의 핵심 부분만 TODO 처리합니다.
