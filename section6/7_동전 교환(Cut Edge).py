# # 내 풀이 1 (3번 TC 실패)
# def dfs(L):
#     global m, cnt
#     if m == 0:
#         return
#     else:
#         L_cnt = m // coins[L]
#         cnt += L_cnt
#         m -= coins[L] * L_cnt
#         dfs(L + 1)
#
#
# if __name__ == "__main__":
#     n = int(input())  # 5
#     coins = sorted(map(int, input().split()), reverse=True)  # [1, 8, 20, 25, 50]
#     m = int(input())  # 129
#     cnt = 0
#     dfs(0)
#     print(cnt)  # 답 : 5, 출력 : 7


# 내 풀이 2 (실패)
# def dfs(L, L_cnt, sum_):
#     global cnt
#     if sum_ > m or L >= n:
#         return
#     elif sum_ == m:
#         if cnt > L_cnt:
#             cnt = L_cnt
#     else:
#         for i in range(((m - sum_) // coins[L]) + 1):
#             dfs(L + 1, L_cnt + i, sum_ + i * coins[L])
#
#
# if __name__ == "__main__":
#     n = int(input())  # 5
#     coins = sorted(map(int, input().split()), reverse=True)  # [1, 8, 20, 25, 50]
#     m = int(input())  # 129
#     cnt = int(1e9)
#     dfs(0, 0, 0)
#     print(cnt)


# 내 풀이 3 (설명만 듣고 다시 시도 -> 내림차순 정렬만 다시 적용해주니 성공!)
def dfs(L, sum_):
    global res
    if sum_ > m or L > res:
        return
    if sum_ == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            dfs(L + 1, sum_ + coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = sorted(list(map(int, input().split())), reverse=True)
    m = int(input())
    res = int(1e9)
    dfs(0, 0)
    print(res)


# 답안 예시
# 작은 값부터 넣으면 처음 출발이 너무 깊게 들어가므로 내림차순으로 가장 큰 동전부터 적용해야 함!!
def DFS(L, sum_):
    global res
    if L > res:
        return
    if sum_ > m:
        return
    if sum_ == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L + 1, sum_ + a[i])


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    res = 2147000000  # 매우 큰 값이면 됨
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)
