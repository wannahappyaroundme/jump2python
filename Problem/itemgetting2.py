from operator import itemgetter

students = [
    {"Name": "Jane", "Age": 22, "Grade": "A"},
    {"Name": "Dave", "Age": 32, "Grade": "B"},
    {"Name": "Sally", "Age": 17, "Grade": "B"},
]

result = sorted(students, key=itemgetter("Age"))
print(result)