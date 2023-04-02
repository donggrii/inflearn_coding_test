# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")
total_range = [list(map(int, input().split())) for _ in range(10)]
card = list(range(21))

for a, b in total_range:
    card[a: b + 1] = card[a: b + 1][::-1]

with open("output3.txt", "a") as f:
    for x in card[1:]:
        print(x, end=" ", file=f)


# 정답 해설
# 두 변수의 값을 교환하는 swap 활용 : a, b = b, a
# 구간 반복 횟수 : ((end - start) + 1) // 2
#                 -> (end - start)가 홀수든 짝수든 적용됨
import sys

sys.stdin = open("input.txt", "r")
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        a[s + i], a[e - i] = a[e - i], a[s + i]

a.pop(0)
for x in a:
    print(x, end=" ")


# Test Case.
# < input >
# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20

# output : 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
