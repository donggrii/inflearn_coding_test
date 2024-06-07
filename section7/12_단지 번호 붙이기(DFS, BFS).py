# 내 풀이 1 (정답)
# DFS 풀이
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
block_count = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
count_per_block = []


def dfs(x, y):
    global count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and check[nx][ny] == 0:
            check[nx][ny] = 1
            count += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and check[i][j] == 0:
            block_count += 1
            check[i][j] = 1
            count = 1
            dfs(i, j)
            count_per_block.append(count)

print(block_count)
for x in sorted(count_per_block):
    print(x)
# with open("output12_5.txt", "a") as f:
#     print(block_count, file=f)
#     for x in sorted(count_per_block):
#         print(x, file=f)


# 내 풀이 2 (정답)
# DFS 풀이
# dfs(x, y) 함수에서 global 명령어로 count를 계산하지 않고, 값을 return하는 방식으로 풀기
# 장점 : 글로벌 변수를 사용하지 않고, dfs(x, y) 함수의 input과 output을 명확하게 알 수 있게 됨
#        dfs(x, y) 함수가 외부 상태에 의존하지 않고 독립적인 기능을 수행할 수 있게 됨
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
block_count = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
count_per_block = []


def dfs(x, y):
    count = 1
    check[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and check[nx][ny] == 0:
            count += dfs(nx, ny)

    return count


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and check[i][j] == 0:
            block_count += 1
            count = dfs(i, j)
            count_per_block.append(count)

print(block_count)
for x in sorted(count_per_block):
    print(x)
# with open("output12_5.txt", "a") as f:
#     print(block_count, file=f)
#     for x in sorted(count_per_block):
#         print(x, file=f)


# 내 풀이 3 (정답)
# BFS 풀이
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]
block_count = 0
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
count_per_block = []
queue = deque()

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and check[i][j] == 0:
            block_count += 1
            count = 1
            check[i][j] = 1
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and check[nx][ny] == 0:
                        count += 1
                        check[nx][ny] = 1
                        queue.append((nx, ny))
            count_per_block.append(count)

print(block_count)
for x in sorted(count_per_block):
    print(x)
# with open("output12_5.txt", "a") as f:
#     print(block_count, file=f)
#     for x in sorted(count_per_block):
#         print(x, file=f)


# # 정답 해설
# import sys

# sys.stdin = open("input.txt", "r")


# Test Case.
# < input >
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# < output >
# 3
# 7
# 8
# 9
