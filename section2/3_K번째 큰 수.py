# 내 풀이 (오답)
# 회고 : 문제를 제대로 읽지 않아서, k번째 수를 출력할 때 중복된 값을 빼주지 않았음
import itertools
import sys

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
digits = list(map(int, input().split()))
total = list(itertools.combinations(digits, 3))

total_sum = {sum(total[i]) for i in range(len(total))}
total_sum = sorted(total_sum, reverse=True)

with open("output3.txt", "a") as f:
    print(total_sum[k - 1], file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(a[i] + a[j] + a[m])

res = list(res)
res.sort(reverse=True)
print(res[k - 1])


# Test Case.
# < input >
# 10 3
# 13 15 34 23 45 65 33 11 26 42

# output : 143
