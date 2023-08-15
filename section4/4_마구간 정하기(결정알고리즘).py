# 내 풀이 (실패)
# 회고 : 강의에서 문제를 풀기 위한 논리만 듣고 풀었을 때, 정답 맞췄음
#        => 즉, 문제 풀이를 어떻게 접근할지 생각해내지 못했지만, 구현은 했음
import sys

sys.stdin = open("input.txt", "r")
n, c = map(int, input().split())
loc = sorted([int(input()) for _ in range(n)])


# 가장 가까운 두 말의 최대 거리를 max_len으로 했을 때, 세울 수 있는 말의 수
def Count(max_len):
    cnt = 1
    last_loc = loc[0]
    for i in range(1, n):
        if loc[i] - last_loc >= max_len:
            last_loc = loc[i]
            cnt += 1
    return cnt


lt = 1
rt = loc[n - 1]
res = 0  # 가장 가까운 두 말의 최대 거리
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

with open("output4.txt", "a") as f:
    print(res, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")


# 배치할 수 있는 말의 마리 수를 반환
def Count(len):
    cnt = 1
    ep = line[0]  # end point
    for i in range(1, n):
        if line[i] - ep >= len:
            cnt += 1
            ep = line[i]
    return cnt


n, c = map(int, input().split())
line = []
for _ in range(n):
    tmp = int(input())
    line.append(tmp)
line.sort()

lt = 1  # 최소 거리는 무조건 1일 것
rt = line[n - 1]  # 마구간의 맨 끝 좌표
while lt <= rt:
    mid = (lt + rt) // 2  # 가장 가까운 두 말의 거리
    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)


# Test Case.
# < input >
# 5 3
# 1
# 2
# 8
# 4
# 9

# output : 3
