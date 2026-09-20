# 설치된 패키지의 실제 버전을 읽기 위해 사용합니다.
from importlib.metadata import version

# 이번 교재에서 반드시 필요한 패키지 목록입니다.
PACKAGES = ["langchain", "langchain-openai", "langgraph", "python-dotenv", "pydantic"]

# 각 패키지의 설치 버전을 한 줄씩 출력합니다.
for package in PACKAGES:
    print(f"{package:<18} {version(package)}")

print("환경 확인 완료")