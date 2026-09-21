import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")

print("[PASS] OPENAI_API_KEY 설정" if api_key else "[FAIL] OPENAI_API_KEY 없음")
print(f"[PASS] OPENAI_MODEL={model}" if model else "[FAIL] OPENAI_MODEL 없음")

if not api_key or not model:
    raise SystemExit(1)

print("API Key 값은 보안을 위해 출력하지 않습니다.")
