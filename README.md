# AI Agent 설계 및 구축 Cookbook — 실습 소스

이 저장소는 아래 Notion 교재를 수업 진행 기준으로 사용합니다.

- 교재: https://app.notion.com/p/AI-Agent-Cookbook-Step-by-Step-3df91bd5a9ac8167928af84bceafc375

각 Step 폴더에는 다음 두 종류의 소스가 있습니다.

- `practice/` : 수업 중 교수자와 함께 TODO 부분을 채우는 **실습 준비 소스**
- `complete/` : 교재 코드 기준의 **실습 완료 소스**

수업 중 코드를 놓쳤거나 오류가 오래 해결되지 않으면 현재 Step의 `complete/`에서 같은 파일명을 찾아 실행한 뒤 다음 Step으로 합류하면 됩니다.

---

## 1. 실습 소스 내려받기

먼저 Git이 설치되어 있는지 확인합니다.

```bash
git --version
```

원하는 작업 폴더에서 저장소를 내려받습니다.

```bash
git clone https://github.com/comstudynews/ai-agent-cookbook.git
cd ai-agent-cookbook
```

이미 한 번 Clone한 저장소가 있다면 수업 시작 전에 최신 내용을 받아옵니다.

```bash
git pull
```

---

## 2. VS Code에서 프로젝트 열기

터미널에서 프로젝트 폴더에 들어온 상태라면 다음 명령으로 VS Code를 열 수 있습니다.

```bash
code .
```

또는 VS Code에서 직접 다음 순서로 엽니다.

```text
File
→ Open Folder...
→ ai-agent-cookbook 폴더 선택
```

VS Code 왼쪽 Explorer에서 아래와 같은 구조가 보이면 정상입니다.

```text
ai-agent-cookbook/
├── README.md
├── requirements.txt
├── check_env.py
├── .env.example
├── step01_llm/
├── step02_tool_calling/
├── ...
└── final_multi_agent/
```

---

## 3. Python 가상환경 만들기

이 교재는 **Python 3.11을 권장**하며 Python 3.10 이상을 기준으로 합니다.

### macOS / Linux

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows에서 `py -3.11`을 사용할 수 없다면 설치된 Python 버전을 먼저 확인합니다.

```powershell
python --version
```

Python 3.10 이상이라면 다음과 같이 만들 수 있습니다.

```powershell
python -m venv .venv
```

가상환경이 제대로 선택되었는지 확인합니다.

```bash
python --version
python -c "import sys; print(sys.executable)"
```

출력된 Python 경로에 `.venv`가 포함되어 있으면 정상입니다.

---

## 4. VS Code Python Interpreter 선택

VS Code에서 다음 순서로 현재 프로젝트의 가상환경을 선택합니다.

```text
Cmd + Shift + P      macOS
Ctrl + Shift + P     Windows

→ Python: Select Interpreter
→ ai-agent-cookbook/.venv 안의 Python 선택
```

선택 후 VS Code에서 새 Terminal을 열고 다시 확인합니다.

```bash
python -c "import sys; print(sys.executable)"
```

프로젝트의 `.venv` 경로가 표시되어야 합니다.

---

## 5. 필요한 패키지 설치

프로젝트 루트에서 실행합니다.

```bash
python -m pip install -r requirements.txt
```

현재 교재 기준 주요 패키지는 다음과 같습니다.

```text
langchain==1.4.1
langchain-openai==1.6.2
langgraph==1.2.11
python-dotenv==1.2.3
pydantic==2.13.5
```

수업 중 임의로 `pip install -U`를 실행하면 API 차이로 코드가 달라질 수 있으므로 교재 기준 버전을 유지하는 것을 권장합니다.

---

## 6. 환경 확인

패키지 설치 후 다음 파일을 실행합니다.

```bash
python check_env.py
```

예상되는 출력 형식은 다음과 같습니다.

```text
langchain          ...
langchain-openai   ...
langgraph          ...
python-dotenv      ...
pydantic           ...
환경 확인 완료
```

---

## 7. OpenAI API Key 설정

프로젝트 루트의 `.env.example`을 복사해 `.env` 파일을 만듭니다.

### macOS / Linux

```bash
cp .env.example .env
```

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

생성된 `.env` 파일을 열고 본인의 API Key를 입력합니다.

```text
OPENAI_API_KEY=본인의_OpenAI_API_Key
OPENAI_MODEL=gpt-5.6-luna
```

> `.env`에는 API Key가 들어 있으므로 GitHub에 Commit하거나 다른 사람에게 공유하지 않습니다.

---

## 8. Step별 실습 진행 방법

예를 들어 **Step 02 — Tool Calling**을 진행한다면 다음 폴더를 사용합니다.

```text
step02_tool_calling/
├── README.md
├── practice/
│   └── step02_tool.py
└── complete/
    └── step02_tool.py
```

수업에서는 먼저 `practice/`의 파일을 엽니다.

```bash
cd step02_tool_calling/practice
python step02_tool.py
```

`practice/` 파일에는 해당 Step에서 직접 작성할 부분이 `TODO`로 표시되어 있습니다.

교수자 설명을 따라 TODO를 완성한 뒤 다시 실행합니다.

실습을 놓쳤거나 코드가 정상적으로 실행되지 않는다면 `complete/`로 이동합니다.

```bash
cd ../complete
python step02_tool.py
```

`complete/`는 해당 Step의 교재 기준 완성 소스입니다. 완성 코드를 실행해 정상 결과를 확인한 뒤 다음 Step으로 진행하면 됩니다.

프로젝트 루트로 돌아가려면 다음처럼 이동할 수 있습니다.

```bash
cd ../..
```

---

## 9. 수업 중 기본 진행 방식

각 Step은 다음 순서로 진행합니다.

```text
Notion 교재에서 현재 Step 확인
        ↓
GitHub의 같은 번호 Step 폴더 열기
        ↓
practice/ 소스 열기
        ↓
TODO 부분을 수업 중 함께 완성
        ↓
실행 및 결과 확인
        ↓
문제가 있으면 complete/ 소스로 확인
        ↓
다음 Step으로 이동
```

즉, 모든 코드를 처음부터 직접 입력하는 방식이 아니라 **준비된 코드에서 그 단계의 핵심 부분을 직접 완성하고 실행 결과를 확인하는 방식**으로 진행합니다.

---

## 10. 전체 실습 순서

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

---

## 11. 수업 중 문제가 생겼을 때

### `ModuleNotFoundError`

먼저 현재 Python이 프로젝트의 `.venv`인지 확인합니다.

```bash
python -c "import sys; print(sys.executable)"
```

필요하면 패키지를 다시 설치합니다.

```bash
python -m pip install -r requirements.txt
```

### `OPENAI_API_KEY` 오류

프로젝트 루트에 `.env` 파일이 있는지 확인합니다.

```text
ai-agent-cookbook/
├── .env
├── requirements.txt
└── ...
```

### 현재 Step을 따라가지 못한 경우

현재 Step 폴더의 `complete/`로 이동해 같은 파일명을 실행합니다.

```text
practice/  → 수업 중 직접 완성
complete/  → 정상 동작하는 완성 소스
```

완성 소스가 정상 실행되면 다음 Step부터 다시 수업에 합류하면 됩니다.

---

## 12. 수업 전 빠른 확인

수업 시작 전에 최소한 다음 순서까지 완료해 두는 것을 권장합니다.

```bash
git pull
python -c "import sys; print(sys.executable)"
python -m pip install -r requirements.txt
python check_env.py
```

그리고 `.env`에 본인의 `OPENAI_API_KEY`가 설정되어 있는지 확인합니다.

---

> **기준 원칙:** `complete/` 소스는 지정된 Notion 교재의 코드와 맞추는 것을 우선하며, `practice/` 소스는 그 완성 코드에서 해당 Step의 핵심 부분만 TODO 처리한 수업용 버전입니다.
