# 내 풀이 (성공!)
def dfs(L):
    global cnt
    if L >= m:
        for j in res:
            print(j, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if check[i] == 0:
                res[L] = i
                check[i] = 1
                dfs(L + 1)
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())  # 3, 2
    res = [0] * m
    check = [0] * (n + 1)
    cnt = 0
    dfs(0)
    print(cnt)


# 답안 예시
def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)
