import datetime

day1 = datetime.date(2021, 12, 14)
day2 = datetime.date(2023, 4, 5)

diff = day2 - day1
print(diff.days)

day3 = datetime.date(2020, 2, 17)
day4 = datetime.date(2025, 9, 25)

diff2 = day4 - day3
print(diff2.days)

day = datetime.date(2021, 12, 14)
print(day.weekday())
print(day.isoweekday())