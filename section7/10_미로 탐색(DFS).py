# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and check[nx][ny] == 0:
                check[nx][ny] = 1
                DFS(nx, ny)
                check[nx][ny] = 0


if __name__ == "__main__":
    N = 7
    board = [list(map(int, input().split())) for _ in range(N)]
    check = [[0] * N for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

    cnt = 0
    check[0][0] = 1
    DFS(0, 0)
    print(cnt)


# 정답 해설
# check 변수 없이 주어진 데이터인 board에 방문 표시하여 공간 복잡도가 더 낮음 (더 효율적)
import sys

sys.stdin = open("input.txt", "r")


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= 6 and 0 <= ny <= 6 and board[nx][ny] == 0:
                board[nx][ny] = 1  # 방문한 곳은 벽(1)로 만들기
                DFS(nx, ny)
                board[nx][ny] = 0  # 돌아왔을 때는 다시 통로(0)로 만들기


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    cnt = 0
    board[0][0] = 1  # 방문한 곳은 벽(1)로 만들기
    DFS(0, 0)
    print(cnt)


# Test Case.
# < input >
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 0 0 0 1
# 1 1 0 1 1 0 0
# 1 0 0 0 0 0 0

# < output >
# 8
