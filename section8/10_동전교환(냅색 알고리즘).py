# 내 풀이
# dy[i] : i 금액을 만들기 위한 최소 동전 개수
n = int(input())
coins = sorted(map(int, input().split()))
m = int(input())
dy = [0] * (m + 1)
for i in range(m + 1):
    dy[i] = i // coins[0]

for i in range(1, len(coins)):  # 2 5
    c = coins[i]
    for j in range(c, m + 1):  # 5 ~ 15
        dy[j] = min(dy[j], dy[j - c] + 1)

print(dy[m])


# Test Case.
# < input >
# 3
# 1 2 5
# 15

# output : 3
