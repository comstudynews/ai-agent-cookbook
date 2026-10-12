from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int

correct: Student = {"name": "홍길동", "age": 25}
incorrect: Student = {"name": "홍길동", "age": "25"}

print(correct)
print(incorrect)
