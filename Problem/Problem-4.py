# Q1

def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
# Q2

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))