# # 내 풀이 (실패..)
# from collections import deque
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# it = n // 2
#
# q = deque([(it, it)])
# ch = [[0] * n for _ in range(n)]
# ch[it][it] = 1
# res = 0  # 총 사과 개수
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# idx = 0
# while idx <= it:
#     x, y = q.popleft()
#     res += arr[x][y]
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0:
#             ch[nx][ny] = 1
#             q.append((nx, ny))
#     idx += 1
#
# while q:
#     x, y = q.popleft()
#     res += arr[x][y]
#
# print(res)


# 답안 예시
# BFS : Level 기준으로 탐색
# 시작 지점 -> 방문 처리, Queue에 추가하는 등의 처리는 미리 해두고 시작하는 편
# Queue, Check, Sum 3단계!
# [n // 2, n // 2] : 격자의 중심점
from collections import deque


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

sum_ = 0
ch = [[0] * n for _ in range(n)]
Q = deque()

start = n // 2
sum_ += a[start][start]
ch[start][start] = 1
Q.append((start, start))
L = 0
while True:
    if L == n // 2:
        break
    size = len(Q)
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum_ += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    # print(L, size)
    # for x in ch:
    #     print(x)
    L += 1

print(sum_)


# Test Case.
# < input >
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# output : 379
