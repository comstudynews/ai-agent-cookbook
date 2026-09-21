# 00_setup

수업 시작 전에 모든 수강생이 같은 출발점에 있는지 확인하는 폴더입니다.

## 권장 실행 순서

```bash
python -m pip install -r requirements.txt
python check_env.py
python 00_setup/check_api_key.py
python 00_setup/smoke_test.py
```

- `check_api_key.py`는 Key 값을 출력하지 않고 설정 여부만 확인합니다.
- `smoke_test.py`는 LLM 호출과 Tool Calling까지 최소 기능을 확인합니다.
- Smoke Test가 실패하면 본 진도로 넘어가기 전에 환경을 먼저 복구합니다.
