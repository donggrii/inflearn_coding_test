# 내 풀이 (성공!)
def dfs(L, s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = nums[i]
            dfs(L + 1, i + 1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    dfs(0, 0)
    print(cnt)


# 답안 예시 1 (DFS)
def DFS(L, s, sum_):
    global cnt
    if L == k:
        if sum_ % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L + 1, i + 1, sum_ + a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)


# 답안 예시 2 (라이브러리를 이용한 조합)
import itertools as it


n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)
