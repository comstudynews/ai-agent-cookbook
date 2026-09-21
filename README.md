# AI Agent 설계 및 구축 Cookbook

작은 LLM 호출에서 시작해 Tool Calling, Structured Output, ReAct, LangGraph, Agentic RAG, Multi-Agent, Memory, Middleware, Retry, HITL, Evaluation까지 단계적으로 실습하는 **Step by Step Cookbook**입니다.

교재: https://app.notion.com/p/AI-Agent-Cookbook-Step-by-Step-3df91bd5a9ac8167928af84bceafc375

## 수업용 저장소 사용법

이 저장소는 브로드캐스팅 실강에서 긴 라이브코딩을 줄이고, 수강생이 **설명 → 짧은 구현 → 실행 → 확인 → 응용** 흐름으로 학습하도록 구성합니다.

- `00_setup/` : 환경 확인, API Key 확인, 전체 Smoke Test
- `01_starter/` : 수강생이 핵심 TODO를 직접 채우는 시작 코드
- `02_complete/` : 검증된 완성 예제
- `03_checkpoint/` : 수업 중 막힌 수강생이 다시 합류하는 복구 지점
- `data/` : 외부 API 없이 연습할 수 있는 샘플 데이터
- `tools/` : Mock Tool 모음
- `tests/` : Tool/환경 기본 테스트
- `challenge/` : 빠르게 끝낸 수강생용 추가 과제
- `final_project/` : 종합실습 Starter / Complete
- `CLASS_FLOW.md` : 교수자 진행 순서

기존 루트의 `step*.py` 파일은 기존 교재 링크와의 호환성을 위해 유지합니다.

## 실습 환경

| 항목 | 기준 |
| --- | --- |
| IDE | Visual Studio Code |
| Python | 3.11 권장, 3.10 이상 |
| 가상환경 | `.venv` |
| langchain | 1.4.1 |
| langchain-openai | 1.6.2 |
| langgraph | 1.2.11 |
| python-dotenv | 1.2.3 |
| pydantic | 2.13.5 |

### 시작

```bash
git clone https://github.com/comstudynews/ai-agent-cookbook.git
cd ai-agent-cookbook

python3 -m venv .venv
source .venv/bin/activate   # Windows는 .venv\Scripts\activate

python -m pip install -r requirements.txt
python check_env.py
python 00_setup/check_api_key.py
```

프로젝트 루트에 `.env` 파일을 만들고 API Key와 수업에서 사용할 모델명을 설정합니다.

```text
OPENAI_API_KEY=본인의_OpenAI_API_Key
OPENAI_MODEL=수업에서_사용할_모델명
```

> `.env`와 API Key는 GitHub에 올리지 않습니다.

## 권장 수업 패턴

1. Cookbook에서 **왜 배우는가 / 전체 구조**를 먼저 설명합니다.
2. 교수자가 Complete 실행 결과를 짧게 보여줍니다.
3. 수강생은 `01_starter/`의 TODO만 직접 채웁니다.
4. 정상 결과를 확인하고 한 가지 조건을 바꿔봅니다.
5. 해결이 오래 걸리면 `03_checkpoint/`에서 다시 합류합니다.
6. 빠른 수강생은 `challenge/`를 진행합니다.
7. 마지막에는 `final_project/`로 핵심 요소를 통합합니다.

## 보안

`.env`, API Key, 개인 계정정보는 커밋하지 않습니다. 공개 저장소이므로 수업 내부정보나 개인정보도 올리지 않습니다.
