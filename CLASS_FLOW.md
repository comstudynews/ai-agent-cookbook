# AI Agent 설계 및 구축 — 실강 운영 흐름

이 문서는 2일 브로드캐스팅 실강을 기준으로 한 교수자용 진행 가이드입니다.

## 기본 수업 단위

한 주제를 다음 순서로 반복합니다.

1. **목표 제시** — 이번 Step이 끝나면 무엇이 실행되는지 먼저 보여줍니다.
2. **핵심 개념** — 구조도와 용어를 5~10분 내로 설명합니다.
3. **Micro Live Coding** — 핵심 코드 3~15줄 정도만 직접 작성합니다.
4. **Starter 완성** — 수강생이 TODO를 채웁니다.
5. **실행/확인** — 정상 로그와 결과를 비교합니다.
6. **변형 문제** — 값, Tool, 조건 중 하나를 바꿉니다.
7. **Checkpoint** — 해결이 오래 걸리는 수강생을 정상 상태로 복구합니다.
8. **Challenge** — 빠른 수강생은 추가 과제를 진행합니다.

## Day 1

### 오전

- 환경 확인
- LLM 호출
- Tool 1개
- 여러 Tool
- Structured Output

Checkpoint: `03_checkpoint/day1_am/`

### 오후

- ReAct 흐름 관찰
- Streaming
- LangGraph State / Node / Edge
- Conditional Edge / Loop
- Goal → Plan → Execute → Reflect

Checkpoint: `03_checkpoint/day1_pm/`

## Day 2

### 오전

- Retrieval Tool
- Agentic RAG
- Handoff
- Supervisor
- Agent-as-Tool
- 병렬 처리 개념

Checkpoint: `03_checkpoint/day2_am/`

### 오후

- Memory / Retry / Middleware
- HITL
- Trace / Evaluation
- Final Project

Checkpoint: `03_checkpoint/day2_pm/`

## 진행 원칙

- package/import/boilerplate를 길게 라이브코딩하지 않습니다.
- 핵심 Agent 로직만 직접 작성합니다.
- 한 Step에서 모든 학생이 완벽히 해결될 때까지 방송을 멈추지 않습니다.
- 복구 지점을 명확히 제공해 다음 Step에 다시 합류하게 합니다.
- 외부 API보다 Mock Tool로 개념을 먼저 익힌 뒤 실제 서비스 연동으로 확장합니다.
- 자연어 답변보다 Tool 호출 여부, State 변화, 종료 조건을 확인합니다.
