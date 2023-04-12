# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
matrix = [[0] * (n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    matrix[i][1 : n + 1] = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(x, y):
    val = matrix[x][y]
    for i in range(4):
        x_, y_ = x + dx[i], y + dy[i]
        if matrix[x_][y_] >= val:
            return False
    return True


cnt = sum(check(i, j) for i in range(1, n + 1) for j in range(1, n + 1))

with open("output9.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
# 1. all() : 모든 값이 참일 경우, True를 반환
# 2. dx, dy를 이용해서 4가지 방향(12시, 3시, 6시, 9시) 탐색하는 방법
# 3. 입력을 받아서 가장자리에 0을 추가해주는 방법
import sys

sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i + dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)


# Test Case.
# < input >
# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2

# output : 10
