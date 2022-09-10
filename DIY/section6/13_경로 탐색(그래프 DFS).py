# 내 풀이 (성공!)
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


# 답안 예시
# 문제에는 주어지지 않았지만, 재방문은 허용 X (만약 허용한다면, 1 ~ 2번을 무한정 왔다갔다 할 수 있기 때문)
# => check 리스트에 방문했다는 것을 표시해줘야 함!
def DFS(v):  # v : 노드 번호
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=" ")
        print()
    else:
        for i in range(1, n + 1):  # i : 방문하려고 하는 노드 번호
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)  # 경로 추가
                DFS(i)
                path.pop()  # 되돌아갈 때 pop 반드시 해줘야 함!
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)  # 방문 체크 리스트
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = [1]  # 실제로 원하는 경로대로 갔는지 "경로"까지 출력해보기
    ch[1] = 1  # 출발 지점 방문 표시
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
# [[0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 1, 1, 0],
#  [0, 1, 0, 1, 0, 1],
#  [0, 0, 0, 0, 1, 0],
#  [0, 0, 1, 0, 0, 1],
#  [0, 0, 0, 0, 0, 0]]
