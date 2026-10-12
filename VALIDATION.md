# 최종 배포 검증 체크리스트

## API 없이 수행하는 검사
```bash
python -m compileall -q .
python -m pip check
python run_offline_checks.py
```
정적 문법·오프라인 Graph 검사만 수행합니다. 전체 실행 검증은 아닙니다.

## API가 필요한 실습
1. Step 01/02: 모델·Tool 호출
2. Step 03/04: Structured Output·Streaming v2
3. Step 10: Supervisor와 Swarm 전환
4. Step 11: Orchestrator–Workers 작업 분해
5. Step 14: Evaluator–Optimizer 피드백 루프
6. Final: Tool·전문 Agent 개별 검증 → Supervisor → Graph 정상/Retry/HITL 거절 경로

**주의:** `final_smoke_test.py`는 모듈 import 시 OpenAI 모델을 초기화하므로 `.env` 키 설정이 필요합니다. 다만 초기 Tool 호출 자체에는 모델 API 요청이 없습니다.

## 배포·안전
- 실제 API 키, 개인정보, 내부자료를 GitHub에 게시하지 않습니다.
- 외부 그림은 출처만으로 재배포 허락이 되는 것은 아니므로 사용 범위를 따로 확인합니다.
- `InMemorySaver`는 프로그램 종료 시 대화 상태가 사라집니다.
- 모델 Tool 선택과 출력은 비결정적일 수 있으므로 관찰한 로그와 평가 조건을 대조합니다.

**본 리포지토리에 코드가 반영되어도 Python 3.11·실제 API 환경에서 전 단계를 실행하기 전까지 최종 실행 검증 완료로 표시하지 않습니다.**
