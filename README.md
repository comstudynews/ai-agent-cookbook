# AI Agent 설계 및 구축 Cookbook

작은 LLM 호출에서 시작해 Tool Calling, Structured Output, ReAct, LangGraph, Agentic RAG, Multi-Agent, Memory, Middleware, Retry, HITL, Evaluation까지 단계적으로 실습하는 **Step by Step Cookbook**입니다.

각 실습은 하나의 개념을 익힌 뒤 작은 코드로 직접 실행하고, 마지막에는 앞에서 배운 요소를 통합한 Multi-Agent 서비스를 구성하는 흐름으로 진행합니다.

## 학습 목표

- LLM과 Agent의 차이를 이해합니다.
- Tool Calling과 ReAct 실행 흐름을 확인합니다.
- LangGraph의 State, Node, Edge, Conditional Edge를 사용합니다.
- Agentic Workflow와 Agentic RAG의 반복 구조를 구현합니다.
- Handoff, Supervisor, Agent-as-Tool, Fan-out/Fan-in을 실습합니다.
- Memory, Middleware, Retry, HITL을 이용해 실행 안정성을 높입니다.
- Trace와 간단한 Evaluation으로 Agent의 실행 과정을 검증합니다.

## 실습 환경

| 항목 | 기준 |
| --- | --- |
| IDE | Visual Studio Code |
| Python | 3.11 권장 |
| 가상환경 | `.venv` |
| langchain | 1.4.1 |
| langchain-openai | 1.6.2 |
| langgraph | 1.2.11 |
| python-dotenv | 1.2.3 |
| pydantic | 2.13.5 |

> 실제 수업 또는 개인 실습 전에 `check_env.py`로 설치 버전을 확인하는 것을 권장합니다.

## 시작하기

### macOS / Linux

```bash
git clone https://github.com/comstudynews/ai-agent-cookbook.git
cd ai-agent-cookbook

python3 -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
git clone https://github.com/comstudynews/ai-agent-cookbook.git
cd ai-agent-cookbook

py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
```

VS Code에서는 **Python: Select Interpreter**에서 프로젝트의 `.venv`를 선택합니다.

현재 Python 실행 경로는 다음 명령으로 확인할 수 있습니다.

```bash
python --version
python -c "import sys; print(sys.executable)"
```

## 환경변수

프로젝트 루트에 `.env` 파일을 만들고 본인의 API Key와 수업에서 사용하는 모델명을 설정합니다.

```text
OPENAI_API_KEY=본인의_OpenAI_API_Key
OPENAI_MODEL=수업에서_사용할_모델명
```

> `.env` 파일과 API Key는 GitHub에 올리지 않습니다.

## 실습 흐름

| Step | 주제 |
| --- | --- |
| 01 | 가장 단순한 LLM 호출 |
| 02 | Tool 1개 연결 |
| 03 | 여러 Tool 선택 / Structured Output |
| 04 | ReAct / Streaming |
| 05 | LangGraph State / Node / Edge |
| 06 | Conditional Edge / Loop |
| 07 | Goal → Plan → Execute → Reflect |
| 08 | Retrieval Tool / Agentic RAG Loop |
| 09 | Agent Handoff |
| 10 | Supervisor / Agent-as-Tool |
| 11 | Fan-out / Fan-in |
| 12 | Middleware / Memory / Retry |
| 13 | Human-in-the-Loop |
| 14 | Trace / Evaluation |
| Final | 통합 고객지원 Multi-Agent + LangGraph Orchestration |

## 핵심 개념

```text
사용자 요청
   ↓
LLM / Structured Output
   ↓
Tool Selection
   ↓
Action
   ↓
Observation
   ↓
State Update
   ↓
Validation / Reflect
   ↓
Retry / Next Action / END
```

LangGraph에서는 다음 요소를 중심으로 실행 흐름을 설계합니다.

```text
State            = 현재 작업 상태
Node             = 실행 작업
Edge             = 이동 경로
Conditional Edge = 조건에 따른 분기
Checkpointer     = 상태 저장과 중단/재개
Reducer          = 병렬 State 업데이트 병합
```

Multi-Agent에서는 다음 패턴을 다룹니다.

```text
Handoff        = 다른 Agent로 제어권 전달
Supervisor     = 중앙에서 전문 Agent 조정
Agent-as-Tool  = 전문 Agent를 Tool처럼 호출
Fan-out/Fan-in = 독립 작업을 병렬 실행 후 통합
```

## Git / GitHub 참고

Git 설정은 실습의 핵심이 아니므로 아래 명령 정도만 알아두면 충분합니다.

```bash
git --version
git config --global user.name
git config --global user.email

git status
git add .
git commit -m "Update practice"
git push
```

원격 저장소 연결 확인:

```bash
git remote -v
```

## 보안 주의

다음 파일은 Git에 포함하지 않습니다.

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

특히 API Key가 들어 있는 `.env` 파일은 공개 저장소에 커밋하지 않도록 주의합니다.

## 최종 실습

마지막 실습에서는 앞에서 학습한 내용을 하나의 흐름으로 연결합니다.

```text
사용자 질문
   ↓
Supervisor
   ↓
전문 Agent / Tool
   ↓
Validation
   ↓
PASS ───────────→ END
FAIL → Retry
          ↓
       재실패
          ↓
         HITL
```

최종적으로 **Tool Calling → Multi-Agent → Supervisor → State → Validation → Retry → HITL**이 어떻게 하나의 Agent 시스템으로 연결되는지 확인하는 것이 목표입니다.
