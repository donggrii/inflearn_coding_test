# 내 풀이 1 (정답)
# DFS 풀이
import sys

sys.stdin = open("input.txt", "r")


def dfs(x, y):
    global count

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and check[nx][ny] == 0:
            check[nx][ny] = 1
            count += 1
            dfs(nx, ny)


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    check = [[0] * n for _ in range(n)]
    block_count = 0
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    count_per_block = []  # 각 단지별 집의 수를 담은 리스트

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and check[i][j] == 0:
                block_count += 1
                check[i][j] = 1
                count = 1  # 단지에 속하는 집의 수: 시작점에 있는 집의 수 1개를 세고, count 변수 초기화
                dfs(i, j)
                count_per_block.append(count)

    print(block_count)
    for x in sorted(count_per_block):
        print(x)


# 내 풀이 2 (정답)
# 내 풀이 1(DFS 풀이)를 발전시켜보기
# dfs(x, y) 함수에서 global 명령어로 count를 계산하지 않고, 값을 return하는 방식으로 풀기
# 장점 : 글로벌 변수를 사용하지 않고, dfs(x, y) 함수의 input과 output을 명확하게 알 수 있게 됨
#        dfs(x, y) 함수가 외부 상태에 의존하지 않고 독립적인 기능을 수행할 수 있게 됨
import sys

sys.stdin = open("input.txt", "r")


def dfs(x, y):
    count = 1
    check[x][y] = 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 1 and check[nx][ny] == 0:
            count += dfs(nx, ny)

    return count


if __name__ == "__main__":
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(n)]
    check = [[0] * n for _ in range(n)]
    block_count = 0
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    count_per_block = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and check[i][j] == 0:
                block_count += 1
                count = dfs(i, j)
                count_per_block.append(count)

    print(block_count)
    for x in sorted(count_per_block):
        print(x)


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


# 정답 해설 1 (DFS 풀이)
# [내 풀이와 다른 점]
# 1. check 변수를 따로 두지 않고, input으로 받은 값을 변경하여 노드에 재방문하지 않도록 함 (공간 복잡도 고려)
# 2. 각 단지별 집의 개수를 담은 리스트의 길이가 전체 단지의 수라는 점을 활용
# 3. 단지별 집의 개수인 cnt를 1 증가하고, 노드 방문 처리해주는 기능을 DFS(x, y) 함수 시작 부분에 선언해서 코드의 중복을 방지
import sys

sys.stdin = open("input.txt", "r")


def DFS(x, y):
    global cnt

    cnt += 1
    board[x][y] = 0  # 체크 개념: 한번 방문하면 0으로 변경

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
            DFS(nx, ny)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    result = []  # 한 단지의 집의 개수를 추가할 리스트

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 단지가 발견되면
                cnt = 0  # 단지에 속하는 집의 수: 0으로 초기화
                DFS(i, j)
                result.append(cnt)

    print(len(result))
    result.sort()
    for x in result:
        print(x)


# 정답 해설 2 (BFS 풀이)
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
result = []
queue = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            queue.append((i, j))
            cnt = 1
            while queue:
                tmp = queue.popleft()
                for k in range(4):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 0:
                        continue
                    board[x][y] = 0
                    queue.append((x, y))
                    cnt += 1
            result.append(cnt)

print(len(result))
result.sort()
for x in result:
    print(x)


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
