# AI Agent 설계 및 구축 — 실습 소스

[Notion 교재](https://app.notion.com/p/3df91bd5a9ac8167928af84bceafc375?pvs=204)의 최신 완료 코드를 기준으로 동기화한 저장소입니다. **Notion에 적힌 `python stepXX_....py` 명령을 바로 실행할 수 있도록 모든 완료 코드를 저장소 루트에도 배치했습니다.**

## 시작하기
```bash
git clone https://github.com/comstudynews/ai-agent-cookbook.git
cd ai-agent-cookbook
```
Python **3.11**을 권장합니다. macOS/Linux에서는 `python3.11 -m venv .venv`와 `source .venv/bin/activate`, Windows PowerShell에서는 `py -3.11 -m venv .venv`와 `.\\.venv\\Scripts\\Activate.ps1`로 가상환경을 만듭니다.

```bash
python -m pip install -r requirements.txt
python -m pip check
python check_env.py
```
`.env.example`을 `.env`로 복사하고 **본인의 OpenAI API 키**를 입력합니다. 실제 키는 GitHub에 게시하지 않습니다.

## Notion과 일치하는 완료 코드 실행 (루트)
```bash
python step01_llm.py
python step02_tool.py
python step07_workflow.py
python step13_hitl.py
python final_smoke_test.py
python final_service_agent.py
python final_graph_orchestrator.py
```
루트 파일과 각 Step의 `complete/` 파일은 동일합니다. `final_smoke_test.py`는 `final_service_agent`를 import하므로 **API 키를 미리 설정해야 합니다**. Tool 실행 자체는 모델 API 호출 없이 동작하지만 Agent 호출은 API 사용량을 발생시킵니다.

## practice/와 complete/
```text
step02_tool_calling/
├── README.md
├── practice/step02_tool.py
└── complete/step02_tool.py
```
- `practice/`: 최신 완료 코드를 바탕으로 작성된 **실행 가능한 변경 실험형 TODO 과제**입니다. 이전의 빈칸 채우기 구조와는 다릅니다.
- `complete/`: Notion 코드와 동일한 기준본입니다.
- 개별 폴더에서 실행한 후 루트로 돌아올 때는 `cd ../..`를 사용합니다.

## Step별 안내
- [LLM 호출](step01_llm/README.md)
- [Tool Calling](step02_tool_calling/README.md)
- [Multi-Tool 및 Structured Output](step03_multi_tool_structured_output/README.md)
- [ReAct 및 Streaming](step04_react_streaming/README.md)
- [State·Node·Edge](step05_langgraph_state_node_edge/README.md)
- [조건 분기 및 Loop](step06_conditional_loop/README.md)
- [Plan–Execute–Reflect](step07_agentic_workflow/README.md)
- [검색 Tool과 재검색 Graph](step08_agentic_rag/README.md)
- [Agent Handoff](step09_handoff/README.md)
- [Supervisor와 Swarm](step10_supervisor/README.md)
- [Fan-out/Fan-in 및 Orchestrator–Workers](step11_parallel/README.md)
- [Middleware·Memory·Retry](step12_harness_memory_retry/README.md)
- [Human-in-the-Loop](step13_hitl/README.md)
- [Trace·Evaluation](step14_trace_evaluation/README.md)
- [통합 고객지원 Multi-Agent](final_multi_agent/README.md)
- [보충 실습](supplementary/README.md)

## 선택 실습
`step10_swarm.py`, `step11_orchestrator_workers.py`, `step14_evaluator_optimizer.py`는 심화 실습입니다. `extra_*.py`는 Notion 23~25장의 보충 실습입니다.

```bash
python -m pip install -r requirements-optional.txt
python -m pip check
```
`extra_typeddict_mypy.py`는 의도적으로 잘못된 타입을 넣어 `python -m mypy extra_typeddict_mypy.py`에서 오류를 확인합니다.

## 배포 전 검증
```bash
python -m compileall -q .
python -m pip check
python run_offline_checks.py
```
실행 범위와 API 기반 검증 목록은 [VALIDATION.md](VALIDATION.md)를 참고하세요. **정적 검사만으로 전체 실행 검증이 완료되는 것은 아닙니다.**

실습의 상품·정책 데이터는 모두 가상 값이며, 안전한 모의 작업 외에 실제 파일 삭제나 결제는 수행하지 않습니다.
