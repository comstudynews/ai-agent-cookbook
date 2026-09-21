from importlib.metadata import version

PACKAGES = ["langchain", "langchain-openai", "langgraph", "python-dotenv", "pydantic"]

for package in PACKAGES:
    print(f"{package:<18} {version(package)}")

print("환경 확인 완료")
