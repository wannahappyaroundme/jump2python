from  operator import itemgetter

students = [
    ("Jane", 22, "A"),
    ("Dave", 32, "B"),
    ("Sally", 17, "B"),
]

result = sorted(students, key=itemgetter(1))
print(result)