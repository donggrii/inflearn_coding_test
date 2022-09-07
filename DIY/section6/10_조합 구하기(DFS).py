# 내 풀이 (실패.. -> 설명 듣고 다시 해보기 -> 성공!)
def dfs(L, s):
    """
    :param L: Level
    :param s: Start (s부터 가지가 뻗기 시작)
    :return:
    """
    global cnt
    if L == m:
        for j in res:
            print(j, end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            if check[i] == 0:
                check[i] = 1
                res[L] = i
                dfs(L + 1, i + 1)
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    check = [0] * (n + 1)
    cnt = 0
    dfs(0, 1)
    print(cnt)


# 답안 예시
# "조합 구하기" 굉장히 중요함!! -> 이 문제를 기본으로 해서 많은 문제들이 응용으로 출제되므로 잘 기억해둘 것!!
# 순열 구하는 것과 코드는 매우 유사하지만, 상태 트리의 유형이 다름!!
# => start를 의미하는 s 변수가 추가되고, check 리스트는 필요 X
def DFS(L, s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)
