# 내 풀이 (실패..)
def dfs(weight, value):
    global res
    if weight > target:
        return
    if value > res:
        res = value
    else:
        for i in range(n):
            dfs(weight + a[i][0], value + a[i][1])
            dfs(weight, value)


if __name__ == "__main__":
    n, target = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    dfs(0, 0)
    print(res)


# 답안 예시
# dy[j] 의미 : 가방에 j 무게만큼 보석을 담았을 때의 최대가치
n, m = map(int, input().split())
dy = [0] * (m + 1)
for i in range(n):  # 보석의 개수만큼
    w, v = map(int, input().split())
    for j in range(w, m + 1):  # (j - w) 할거니까 w부터
        dy[j] = max(dy[j], dy[j - w] + v)  # j - w : w라는 무게의 보석을 담기 위해 빈 공간 마련
print(dy[m])


# Test Case.
# < input >
# 4 11
# 5 12
# 3 8
# 6 14
# 4 8

# output : 28
