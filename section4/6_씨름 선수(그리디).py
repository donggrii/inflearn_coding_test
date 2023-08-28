# 내 풀이 (성공)
# 정리 : https://ddonggrii.tistory.com/4
import sys

sys.stdin = open("input.txt", "r")
n = int(input())  # 총 인원 수
candidate = [list(map(int, input().split())) for _ in range(n)]  # (키, 몸무게)
candidate.sort(reverse=True)  # 키 기준 내림차순 정렬

cnt = 0
max_weight = 0
for h, w in candidate:
    if max_weight < w:
        cnt += 1
        max_weight = w

with open("output6.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)

largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)


# Test Case.
# < input >
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

# < output >
# 3
