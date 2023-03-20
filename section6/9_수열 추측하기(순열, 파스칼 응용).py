# 내 풀이 (라이브러리 이용한 완전탐색으로는 성공. But, DFS는 실패)
from itertools import permutations, combinations


n, f = map(int, input().split())
b = [0] * n  # n-1Ci
res = list(permutations(range(1, n + 1)))
final = []
for i in range(n):
    b[i] = len(list(combinations(range(n-1), i)))
for x in range(len(res)):
    val = 0
    for y in range(len(b)):
        val += b[y] * res[x][y]
    if val == f:
        final = res[x]
        break
for a in final:
    print(a, end=" ")


# 답안 예시 1 (DFS)
# 나올 수 있는 순열을 전부 구해서, 파스칼 계산에 적용하고, 발견되면 즉시 stop
# 파스칼 계산
# (ex) 1, 2, 3, 4 => 1 + (2 + 2 + 2) + (3 + 3 + 3) + 4
# => "이항계수"의 규칙과 동일
# (ex) (a + b)^2 = a^2 + 2ab + b^2 : (1, 2, 1)
#      (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3 : (1, 3, 3, 1) = (3C0, 3C1, 3C2, 3C3)
# 그렇다면, n = 5일 때는? (1, 4, 6, 4, 1) = (4C0, 4C1, 4C2, 4C3, 4C4)
# 그 다음은, (5C0, 5C1, 5C2, 5C3, 5C4, 5C5) = (1, 5, 10, 10, 5, 1)
# => 이러한 규칙을 저장해놓으면 좋을 것!
# => b 배열만 잘 초기화하면 나머지는 순열과 동일함
import sys


def DFS(L, sum_):  # sum_ : 최종 f로 향해가는 누적 합
    if L == n and sum_ == f:
        for x in p:
            print(x, end=" ")
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum_ + (p[L] * b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n  # 순열을 계속 만들어나갈 것
    b = [1] * n  # binary : 이항계수를 초기화, 저장할 것
    ch = [0] * (n + 1)  # 순열 만들 때 중복을 방지하기 위한 check
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i
    DFS(0, 0)


# 답안 예시 2 (itertools 라이브러리를 이용한 순열)
import itertools as it


n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i
a = list(range(1, n + 1))
for tmp in it.permutations(a):
    sum_ = 0
    for L, x in enumerate(tmp):
        sum_ += (x * b[L])
    if sum_ == f:
        for x in tmp:
            print(x, end=" ")
        break
