# 내 풀이 (정답)
# "에라토스테네스의 체"를 이용해서 1부터 N까지의 소수의 개수 출력
# 좀 더 시간을 줄이려면, "line 11에 if prime[i] == 1"을 추가하기!!
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
prime = [1] * (n + 1)

for i in range(2, int(n**0.5) + 1):
    k = 2
    while i * k <= n:
        prime[i * k] = 0
        k += 1

with open("output7.txt", "a") as f:
    print(sum(prime[2:]), file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
ch = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1

print(cnt)


# Test Case.
# input : 20
# output : 8
