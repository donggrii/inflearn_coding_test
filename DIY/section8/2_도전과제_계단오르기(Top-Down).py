# 내 풀이 (성공!)
def dfs(x):
    if d[x] > 0:
        return d[x]
    if x == 1 or x == 2:
        return x
    else:
        d[x] = dfs(x - 1) + dfs(x - 2)
        return d[x]


if __name__ == "__main__":
    n = int(input())  # 7
    d = [0] * (n + 1)
    print(dfs(n))  # 21
