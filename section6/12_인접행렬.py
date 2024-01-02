# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    matrix[start - 1][end - 1] = cost

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


# 정답 해설 1 (인접행렬(가중치 방향 그래프))
import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()


# 정답 해설 2 (인접행렬(무방향 그래프))
import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end=" ")
    print()


# Test Case 1. (인접행렬(가중치 방향 그래프))
# < input >
# 6 9
# 1 2 7
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5

# < output >
# 0 7 4 0 0 0
# 2 0 5 0 5 0
# 0 0 0 5 0 0
# 0 2 0 0 5 0
# 0 0 0 0 0 0
# 0 0 0 5 0 0

# Test Case 2. (인접행렬(무방향 그래프))
# < input >
# 5 5
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5

# < output >
# 0 1 1 0 0
# 1 0 0 1 0
# 1 0 0 1 0
# 0 1 1 0 1
# 0 0 0 1 0
