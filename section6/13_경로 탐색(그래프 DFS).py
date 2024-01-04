# 내 풀이 (성공)
import sys

sys.stdin = open("input.txt", "r")


def DFS(vertex):
    global cnt
    if vertex == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if check[i] == 0 and graph[vertex][i] == 1:
                check[i] = 1
                DFS(i)
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start][end] = 1
    cnt = 0
    check = [0] * (n + 1)
    check[1] = 1
    DFS(1)
    print(cnt)


# (과거) 내 풀이 (성공)
import sys

sys.stdin = open("input.txt", "r")


def dfs(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        if not visited[v]:
            visited[v] = True
            for idx, val in enumerate(g[v]):
                if val == 1:
                    dfs(idx)
            visited[v] = False


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    visited = [False] * (n + 1)
    dfs(1)
    print(cnt)


# 정답 해설
# 그래프 이론에서 "경로"의 정의 : 한 번 방문한 노드는 재방문 하지 않음
import sys

sys.stdin = open("input.txt", "r")


def DFS(vertex):
    global cnt
    if vertex == n:
        cnt += 1
        # for x in path:
        #     print(x, end=" ")
        # print()
    else:
        for i in range(1, n + 1):
            if graph[vertex][i] == 1 and check[i] == 0:
                check[i] = 1
                # path.append(i)
                DFS(i)
                # path.pop()
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    check = [0] * (n + 1)  # 방문 체크 리스트
    for _ in range(m):
        start, end = map(int, input().split())
        graph[start][end] = 1
    cnt = 0
    # path = [1]
    check[1] = 1  # 출발 지점 방문 표시
    DFS(1)
    print(cnt)


# Test Case.
# < input >
# 5 9
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 5
# 3 4
# 4 2
# 4 5

# < output >
# 6
