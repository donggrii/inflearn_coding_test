# 내 풀이 (정답)
# 1. result 변수에 total에 digit_sum 함수 map으로 적용한 것 저장
# 2. result의 max 값에 해당하는 index를 total에서 구하기
#   2-1. max 값에 해당하는 게 2개 이상일 경우 index가 가장 작은 것 출력
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
total = list(map(int, input().split()))


def digit_sum(x):  # 자릿수의 합 구하는 함수
    string = str(x)
    result = sum(int(string[i]) for i in range(len(string)))
    return result


result = list(map(digit_sum, total))
max_sum = max(result)

for i in range(n):
    if max_sum == result[i]:
        max_index = i
        break

with open("output6.txt", "a") as f:
    print(total[max_index], file=f)


# 정답 해설 1
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum_ = 0
    while x > 0:
        sum_ += x % 10
        x //= 10
    return sum_


max_ = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max_:
        max_ = tot
        res = x

print(res)


# 정답 해설 2 (pythonic한 방법)
def digit_sum(x):
    sum_ = 0
    for i in str(x):
        sum_ += int(i)
    return sum_


# Test Case.
# < input >
# 3
# 125 15232 97

# output : 97
