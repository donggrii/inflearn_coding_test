# 내 풀이 1 (정답)
# BFS 풀이, 수확하지 않는 부분(제약조건) 표시
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(input())
apples = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)  # 상하좌우
half_point = n // 2
check = [[0] * n for _ in range(n)]

# 수확하지 않는 부분(제약조건) -1로 채우기
for i in range(1, half_point + 1):
    for j in range(i):
        # 행 방향으로 반 나눠서 위 양쪽 부분 -1로 채우기
        check[half_point - i][j] = -1  # (1, 0) / (0, 0), (0, 1)
        check[half_point - i][-j - 1] = -1  # (1, -1) / (0, -1), (0, -2)
        # 행 방향으로 반 나눠서 아래 양쪽 부분 -1로 채우기
        check[half_point + i][j] = -1  # (3, 0) / (4, 0), (4, 1)
        check[half_point + i][-j - 1] = -1  # (3, -1) / (4, -1), (4, -2)

queue = deque()
queue.append((half_point, half_point))  # (2, 2)
check[half_point][half_point] = 1  # 처음 위치 방문 표시
result = apples[half_point][half_point]  # 수확한 사과의 개수

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0:
            check[nx][ny] = 1
            result += apples[nx][ny]
            queue.append((nx, ny))

print(result)


# 내 풀이 2 (정답)
# BFS 아닌 풀이, 특정 패턴이 있으므로 중간/위/아래 나눠서 바로 답 구하기
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
apples = [list(map(int, input().split())) for _ in range(n)]
half_point = n // 2
result = 0

for i in range(n):
    result += apples[half_point][i]  # 중간 : (2, 0) ~ (2, 4)

for i in range(1, half_point + 1):
    for j in range(n - (2 * i)):
        result += apples[half_point - i][i + j]  # 위 : (1, 1), (1, 2), (1, 3) / (0, 2)
        result += apples[half_point + i][i + j]  # 아래 : (3, 1), (3, 2), (3, 3) / (4, 2)

print(result)


# 정답 해설
# - [Section 3] 7. 사과나무(다이아몬드)와 동일한 문제
# - 가운데 지점 좌표(n // 2, n // 2)를 큐에 넣고, 상하좌우 4갈래로 상태트리를 뻗음 (level 기준 탐색)
# - 종료지점은 level을 활용하여 설정
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 12시, 3시, 6시, 9시 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())  # 홀수 N
apples = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * n for _ in range(n)]  # 방문 표시할 체크 리스트

sum_apples = 0
queue = deque()
sum_apples += apples[n // 2][n // 2]
check[n // 2][n // 2] = 1
queue.append((n // 2, n // 2))
level = 0

while True:
    if level == n // 2:
        break
    size = len(queue)
    for _ in range(size):
        tmp = queue.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if check[x][y] == 0:
                sum_apples += apples[x][y]
                check[x][y] = 1
                queue.append((x, y))
    level += 1

print(sum_apples)


# Test Case.
# < input >
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# < output >
# 379
