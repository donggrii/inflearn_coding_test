# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(x, y):
    global cnt
    if x == end_x and y == end_y:
        cnt += 1
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and check[nx][ny] == 0
                and matrix[x][y] < matrix[nx][ny]  # 더 높은 값으로만 이동 가능
            ):
                check[nx][ny] = 1
                DFS(nx, ny)
                check[nx][ny] = 0


if __name__ == "__main__":
    n = int(input())
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우

    # 출발지는 가장 낮은 곳, 목적지는 가장 높은 곳 구하기
    matrix = []
    minimum, maximum = 2147000000, -2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)
        min_tmp, max_tmp = min(tmp), max(tmp)
        if minimum > min_tmp:
            minimum = min_tmp
            start_x, start_y = i, tmp.index(minimum)  # 최소값이 발견되면 x,y 좌표 갱신
        if maximum < max_tmp:
            maximum = max_tmp
            end_x, end_y = i, tmp.index(maximum)  # 최대값이 발견되면 x,y 좌표 갱신

    cnt = 0
    check = [[0] * n for _ in range(n)]
    check[start_x][start_y] = 1
    DFS(start_x, start_y)
    print(cnt)


# 정답 해설
# [Section 7] 10. 미로 탐색과 풀이가 유사하지만, 아래의 2가지가 다름
# 1. 이전보다 더 높은 값으로만 이동 가능
# 2. 출발지, 목적지 따로 구해줘야 함
import sys

sys.stdin = open("input.txt", "r")


def DFS(x, y):
    global cnt
    if x == end_x and y == end_y:
        cnt += 1
    else:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and check[nx][ny] == 0
                and board[nx][ny] > board[x][y]  # 더 높은 값으로만 이동 가능
            ):
                check[nx][ny] = 1
                DFS(nx, ny)
                check[nx][ny] = 0


if __name__ == "__main__":
    n = int(input())
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    board = [[0] * n for _ in range(n)]
    check = [[0] * n for _ in range(n)]
    min_, max_ = 2147000000, -2147000000

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min_:
                min_ = tmp[j]
                start_x, start_y = i, j
            if tmp[j] > max_:
                max_ = tmp[j]
                end_x, end_y = i, j
            board[i][j] = tmp[j]

    check[start_x][start_y] = 1
    cnt = 0
    DFS(start_x, start_y)
    print(cnt)


# Test Case.
# < input >
# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100

# < output >
# 5
