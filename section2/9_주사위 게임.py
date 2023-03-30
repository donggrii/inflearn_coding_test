# 내 풀이 (정답)
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")
n = int(input())
total = [list(map(int, input().split())) for _ in range(n)]
prize = [0] * n

for i in range(n):
    k = set(total[i])
    if len(k) == 1:  # 규칙(1)
        prize[i] = 10000 + (max(k) * 1000)
    elif len(k) == 2:  # 규칙(2)
        freq = Counter(total[i]).items()
        freq = sorted(freq, key=lambda x: x[1], reverse=True)
        prize[i] = 1000 + (freq[0][0] * 100)
    else:  # 규칙(3)
        prize[i] = max(k) * 100

with open("output9.txt", "a") as f:
    print(max(prize), file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    # if를 쓸 때, 가장 좋은 조건을 우선적으로 적을 것 (최대 상금을 출력하라고 했기 때문)
    # 조건 (1)
    if a == b and b == c:
        money = 10000 + (a * 1000)
    # 조건 (2)
    elif a == b or a == c:  # 이 경우 하나의 "a" 변수로 계산할 수 있으므로, b == c 경우는 밑에서 따로 지정
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    # 조건 (3)
    else:
        money = c * 100
    if money > res:
        res = money
print(res)


# Test Case.
# < input >
# 3
# 3 3 6
# 2 2 2
# 6 2 5

# output : 12000
