# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
result = []

for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        result.extend((i, n // i))

result = sorted(set(result))

with open("output1.txt", "a") as f:
    print(result[k - 1] if len(result) >= k else -1, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)


# Test Case 1.
# input : 6 3
# output : 3

# Test Case 2.
# input : 6 5
# output : -1
