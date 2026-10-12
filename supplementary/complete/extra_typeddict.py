from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int

student: Student = {"name": "홍길동", "age": 25}
print(student)
print(type(student))

# 다음 줄은 타입 검사기에서 오류로 지적할 수 있습니다.
# wrong: Student = {"name": "홍길동", "age": "25"}
