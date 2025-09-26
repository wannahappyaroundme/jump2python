import itertools
print(list(itertools.permutations(['1', '2', '3'], 2)))

for a, b in itertools.permutations(['1', '2', '3'], 2):
    print(a, b)
# 순열 구하기 / 순서가 있는 모든 경우의 수

print(list(itertools.combinations(['1', '2', '3'], 2)))

it = itertools.combinations(range(1, 46), 6)

print(len(list(it)))

# 조합 구하기 / 순서가 없는 모든 경우의 수
# 1~45 숫자 중에서 6개를 고르는 경우의 수
# 로또 번호 만들기

# 중복 조합을 사용하는 함수
print(list(itertools.combinations_with_replacement(['1', '2', '3'], 2)))

def add(data):
    result = 0
    for i in data:
        result += i
    return result

data = [1, 2, 3, 4, 5]
result = add(data)
print(result)