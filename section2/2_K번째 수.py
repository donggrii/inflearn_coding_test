# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")

t = int(input())
total = []

for _ in range(t):
    n, s, e, k = map(int, input().split())
    digits = list(map(int, input().split()))
    total.append(([s, e, k], digits))

with open("output2.txt", "a") as f:
    for i in range(t):
        s, e, k = total[i][0]
        char = total[i][1]
        print(f"#{i + 1}", sorted(char[s - 1:e])[k - 1], file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "rt")
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s - 1:e]
    a.sort()
    print(f"#{t + 1} {a[k - 1]}")


# Test Case.
# < input >
# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

# < output >
# #1 7
# #2 6
