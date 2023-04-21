# 내 풀이 (실패)
# 회고 : (1번째 시도) Test Case 5문제 모두 Time Limit에 걸림
#        (2번째 시도) rt = mid - 1, lt = mid + 1로 바꿨으나, 출력값이 모두 -2147000000으로 나옴
#        (3번째 시도) 탐색 범위를 주어진 랜선의 길이 중 최소 -> 최대로 바꿨으나 Test Case 3, 4번 틀림
#         => 이분 탐색을 3가지 if 조건문으로 나눈다는 고정관념을 버릴 것!
import sys

sys.stdin = open("input.txt", "r")
k, n = map(int, input().split())
total = sorted([int(input().strip()) for _ in range(k)])
lt, rt = 0, total[-1]
maximum = -2147000000

while lt <= rt:
    mid = (lt + rt) // 2
    result = sum(i // mid for i in total)
    if result == n:
        if maximum < mid:
            maximum = mid
            lt = mid + 1
    elif result < n:
        rt = mid - 1
    else:
        lt = mid + 1

with open("output2.txt", "a") as f:
    print(maximum, file=f)


# 정답 해설
# 이분 탐색을 이용해서 1부터 "랜선의 최댓값" 사이에서 최적의 해를 구하기
# 결정 알고리즘의 특징 : 찾고자 하는 답이 "특정 범위" 안에 있다는 것을 알 수 있음!
#                        => 정답 범위를 정해놓고, 그 범위 내에서 이분 탐색을 이용해서 탐색 범위를 좁혀나감
import sys

sys.stdin = open("input.txt", "r")


def Count(len):
    cnt = 0
    for x in line:
        cnt += x // len
    return cnt


k, n = map(int, input().split())
line = []
res = 0
largest = 0

for _ in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:  # 더 많이 자를 수 있다는 것 = 랜선을 자르는 길이가 짧다는 것 = 더 긴 길이가 있을 수 있음!
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)


# Test Case.
# < input >
# 4 11
# 802
# 743
# 457
# 539

# output : 200
