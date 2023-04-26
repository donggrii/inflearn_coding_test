# 내 풀이 (실패)
# 회고 : 이분탐색으로 문제를 풀다가 무한루프에 빠져 해결 불가
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
runtimes = list(map(int, input().split()))
lt, rt = 1, sum(runtimes)
final = 2147000000


def get_count(minimum):
    i = cnt = 0
    candidate = minimum
    while i < len(runtimes):
        if candidate - runtimes[i] > 0:
            candidate -= runtimes[i]
            i += 1
        elif candidate - runtimes[i] == 0:
            candidate -= runtimes[i]
            i += 1
            cnt += 1
            candidate = minimum
        else:
            cnt += 1
            candidate = minimum
    return cnt + 1


while lt <= rt:
    mid = (lt + rt) // 2
    result = get_count(mid)
    if result == m:
        if final > mid:
            final = mid
            rt = mid - 1
    elif result < m:
        rt = mid - 1
    else:
        lt = mid + 1

print(final)


# 정답 해설
# 결정 알고리즘을 적용했을 때의 범위 : 1 ~ 45 (전체 부른 곡 길이의 합 : DVD 1장에 모두 담는다고 가정)
#                                      => DVD 용량을 45로 해도 3장에 적절히 나눠 담을 수 있음
# [반례 수정 강의] : DVD 1개의 용량은 music 리스트의 최대값보다는 커야 함
#                    1개의 DVD에 1개의 노래는 전부 들어가야 하기 때문!
#                    따라서, mid >= max_ 부분이 추가되어야 함!
import sys

sys.stdin = open("input.txt", "r")


def Count(capacity):
    cnt = 1
    sum_ = 0
    for x in music:
        if sum_ + x > capacity:
            cnt += 1
            sum_ = x
        else:
            sum_ += x
    return cnt


n, m = map(int, input().split())
music = list(map(int, input().split()))
max_ = max(music)
lt = 1
rt = sum(music)
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max_ and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)


# Test Case 1.
# < input >
# 9 3
# 1 2 3 4 5 6 7 8 9

# output : 17

# Test Case 2.
# < input >
# 9 9
# 1 2 3 4 5 6 7 8 9

# output : 9

# Test Case 3.
# < input >
# 5 4
# 1 1 1 1 1

# output : 2
