# 내 풀이 (성공!)
n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a - 1][b - 1] = cost
print(graph)


# Test Case.
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
# [[0, 7, 4, 0, 0, 0],
#  [2, 0, 5, 0, 5, 0],
#  [0, 0, 0, 5, 0, 0],
#  [0, 2, 0, 0, 5, 0],
#  [0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 5, 0, 0]]


# 답안 예시 1 (인접행렬(무방향 그래프))
n, m = map(int, input().split())  # 노드 개수(n), 간선 개수(m)
g = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=" ")
    print()


# Test Case.
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


# 답안 예시 2 (인접행렬(가중치 방향 그래프))
n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(g[i][j], end=" ")
    print()


# Test Case.
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
