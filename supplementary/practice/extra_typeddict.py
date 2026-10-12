# TODO: 보충 실습 개념을 변경해 실행 — 아래 실행 가능한 코드를 수정하여 결과를 비교하세요.
# 교재 최신 API·State 구조와 일치하는 실습 시작 파일입니다.

from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int

student: Student = {"name": "홍길동", "age": 25}
print(student)
print(type(student))

# 다음 줄은 타입 검사기에서 오류로 지적할 수 있습니다.
# wrong: Student = {"name": "홍길동", "age": "25"}
