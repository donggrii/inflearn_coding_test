# (과거) 내 풀이 (라이브러리 이용한 완전탐색으로는 성공. But, DFS는 실패)
import sys
from itertools import permutations, combinations

sys.stdin = open("input.txt", "r")

n, f = map(int, input().split())
b = [0] * n
res = list(permutations(range(1, n + 1)))  # 모든 순열 구하기
final = []

for i in range(n):
    b[i] = len(list(combinations(range(n - 1), i)))  # (n-1)Ci (ex. N=4, 3C0, 3C1, 3C2, 3C3)

for x in range(len(res)):
    val = 0
    for y in range(len(b)):
        val += b[y] * res[x][y]
    if val == f:
        final = res[x]
        break

for a in final:
    print(a, end=" ")


# 정답 해설 1 (순열 구하기 + 이항 계수 접근법)
# 순열은 사전 순으로 전부 확인하되, N에 따라 이항 계수를 미리 구해놓고 계산
# 파스칼 계산 : (ex) 1, 2, 3, 4 => 1 + (2 + 2 + 2) + (3 + 3 + 3) + 4 => "이항 계수"의 규칙과 동일
# (ex) N = 3, (a + b)^2 = a^2 + 2ab + b^2 : (1, 2, 1) = (2C0, 2C1, 2C2)
#      N = 4, (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 : (1, 3, 3, 1) = (3C0, 3C1, 3C2, 3C3)
#      N = 5, (1, 4, 6, 4, 1) = (4C0, 4C1, 4C2, 4C3, 4C4)
#      N = 6, (1, 5, 10, 10, 5, 1) = (5C0, 5C1, 5C2, 5C3, 5C4, 5C5)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    if level == n and sum_ == f:
        for x in permutation:
            print(x, end=" ")
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                check[i] = 1
                permutation[level] = i
                DFS(level + 1, sum_ + (permutation[level] * binary[level]))
                check[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    permutation = [0] * n  # 순열
    binary = [1] * n  # 이항 계수 초기화 (ex. 3C0, 3C1, 3C2, 3C3)
    check = [0] * (n + 1)  # 순열 중복 방지
    for i in range(1, n):
        binary[i] = binary[i - 1] * (n - i) // i  # 원래 나누기(/)지만 이항 계수는 실수가 없으므로 몫(//) 연산
    DFS(0, 0)


# 정답 해설 2 (itertools 라이브러리를 이용한 순열)
import sys
import itertools as it

sys.stdin = open("input.txt", "r")

n, f = map(int, input().split())
binary = [1] * n
for i in range(1, n):
    binary[i] = binary[i - 1] * (n - i) // i

a = list(range(1, n + 1))
for tmp in it.permutations(a):
    sum_ = 0
    for level, x in enumerate(tmp):
        sum_ += x * binary[level]
    if sum_ == f:
        for x in tmp:
            print(x, end=" ")
        break


# Test Case.
# < input >
# 4 16

# < output >
# 3 1 2 4
