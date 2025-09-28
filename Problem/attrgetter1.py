from operator import attrgetter

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
students = [
    Student("Jane", 22, "A"),
    Student("Dave", 32, "B"),
    Student("Sally", 17, "B"),
]

result = sorted(students, key=attrgetter("age"))

print(result)