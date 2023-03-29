# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
total = list(map(int, input().split()))
correct, result = 0, 0

for x in total:
    if x == 1:  # 정답
        correct += 1
        result += correct
    else:  # 오답
        correct = 0

with open("output10.txt", "a") as f:
    print(result, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
sum_ = 0
cnt = 0  # 가중치

for x in a:
    if x == 1:
        cnt += 1
        sum_ += cnt
    else:
        cnt = 0

print(sum_)


# Test Case.
# < input >
# 10
# 1 0 1 1 1 0 0 1 1 0

# output : 10
