# 내 풀이 (실패..)
# 이분검색으로 정답에 근접한 값을 찾고, 1씩 줄여나가며 정답 찾기
k, n = map(int, input().split())  # 이미 가지고 있는 랜선 개수 K, 필요한 랜선 개수 N
lines = [int(input()) for _ in range(k)]
min_lines = min(lines)


def get_count(lines, length):
    count = 0
    for a in lines:
        count += a // length
    return count


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if get_count(lines, mid) == target:
            return mid
        elif get_count(lines, mid) > target:
            start = mid + 1
        else:
            end = mid - 1


max_len = binary_search(1, min_lines, n - 1)  # 1 ~ 457
cnt = 0
while cnt < n:
    max_len -= 1
    cnt = get_count(lines, max_len)
print(max_len)


# 답안 예시
# 이분 검색을 이용해서 1부터 랜선의 최댓값 사이에서 최적의 해를 구하기
# < 알고리즘 문제풀이에서 "이분 검색"은 언제 활용할까? >
# => 결정 알고리즘 방법론에서 주로 사용하는데, 특징은 찾고자 하는 답이 특정 범위 안에 있다는 것!
# => 답을 정해놓고, 그 범위 내에서 이분 검색을 이용해서 탐색 범위를 좁혀나감
def Count(len):  # len 길이로 만들 수 있는 랜선의 개수
    cnt = 0
    for x in lines:
        cnt += x // len
    return cnt


k, n = map(int, input().split())  # 4, 11
lines = [int(input()) for _ in range(k)]
res = 0
lt = 1
rt = max(lines)
while lt <= rt:
    mid = (lt + rt) // 2  # 랜선의 길이
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
