# 내 풀이
from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
result = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(result)


# Test Case.
# < input >
# 6 6
# 1 4
# 5 4
# 4 3
# 2 5
# 2 3
# 6 2

# output : 1 6 2 5 4 3
