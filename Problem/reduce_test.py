import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda a, b: a + b, data)
print(result)
# reduce() 함수를 사용하여 누적 합 구하기

num_list = [3, 2, 8, 1, 6, 7]
max_num = functools.reduce(lambda a, b: a if a > b else b, num_list)
print(max_num)
# reduce() 함수를 사용하여 최댓값 구하기