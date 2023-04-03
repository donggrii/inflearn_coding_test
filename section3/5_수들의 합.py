# 내 풀이 (오답)
# 정답은 모두 맞았지만, 채점했을 때 5문제 중 2문제(4, 5번)가 Time Limit에 걸림
# 내 풀이처럼 2중 for문에 아무리 break를 걸었어도, 정답 해설의 while문 + 투포인터 풀이가 어렵지만 더 좋은 풀이인 듯함
# A[i] + ... + A[j] = M이 되는 경우의 수 출력
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())  # 1 <= n <= 10,000 | 1 <= m <= 3억
total = list(map(int, input().split()))
total.insert(0, 0)

cnt = 0
for i in range(1, n + 1):
    res = total[i]
    for j in range(i + 1, n + 1):
        if res < m:
            res += total[j]
        if res > m:
            break
        if res == m:
            cnt += 1
            break

with open("output5.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
# N개의 숫자 중 "연속적인 부분합"이 M이 되는 경우의 수 구하는 문제
# 연속적인 부분합 "tot" : lt ~ (rt - 1)까지의 부분합
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())  # 1 <= n <= 10,000 | 1 <= m <= 3억
a = list(map(int, input().split()))
lt, rt = 0, 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt >= n:
            break  # 어떤 경우든 여기서 break 걸림 (rt가 모든 자료를 보고 n에 있는데 tot < m이어서 rt를 더해줘야 할 때)
        tot += a[rt]
        rt += 1
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)


# Test Case.
# < input >
# 8 3
# 1 2 1 3 1 1 1 2

# output : 5 => (1, 2), (2, 1), (3), (1, 1, 1), (1, 2)
