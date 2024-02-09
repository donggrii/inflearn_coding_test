# 내 풀이 (정답)
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = 7
matrix = [list(map(int, input().split())) for _ in range(n)]  # 0은 도로, 1은 벽
check = [[0] * n for _ in range(n)]  # 방문 표시
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

queue = deque()
queue.append((0, 0, 0))  # (x, y, 이동 수)
check[0][0] = 1
result = 0
flag = False

while queue:
    x, y, cnt = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == 0 and matrix[nx][ny] == 0:
            check[nx][ny] = 1
            queue.append((nx, ny, cnt + 1))
        if nx == 6 and ny == 6:  # 종착점 (x, y) = (6, 6)이면 중지
            flag = True
            result = cnt + 1
            break
    if flag:
        break

print(result) if flag else print(-1)


# 정답 해설
# - check 변수 사용 X (방문 시, 주어진 2차원 리스트 값을 변경)
# - 거리 배열 사용
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 12시, 3시, 6시, 9시 (시계방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(7)]
distance = [[0] * 7 for _ in range(7)]

queue = deque()
queue.append((0, 0))
board[0][0] = 1  # 방문한 곳은 벽(1)으로 만들기

while queue:
    tmp = queue.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1  # 방문한 곳은 벽(1)으로 만들기
            distance[x][y] = distance[tmp[0]][tmp[1]] + 1
            queue.append((x, y))

if distance[6][6] == 0:
    print(-1)
else:
    print(distance[6][6])


# Test Case.
# < input >
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0

# < output >
# 12
