# 내 풀이 (정답)
# 회고 : lt = mid, rt = mid가 아니라, lt = mid + 1, rt = mid - 1
#        이분탐색의 시간 복잡도는 "log2(N)"
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
total = sorted(map(int, input().split()))
lt, rt = 0, len(total) - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if total[mid] == m:
        result = mid + 1
        break
    elif total[mid] < m:
        lt = mid
    else:
        rt = mid

with open("output1.txt", "a") as f:
    print(result, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
a = sorted(map(int, input().split()))
lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1


# 참고 : 재귀를 활용한 이분탐색
import sys


def binary_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, end, target)


input_ = sys.stdin.readline
n, m = map(int, input_().split())
nums = sorted(map(int, input().split()))
result = binary_search(nums, 0, n - 1, m)

if result is None:
    print("원소를 찾을 수 없습니다.")
else:
    print(result + 1)


# Test Case.
# < input >
# 8 32
# 23 87 65 12 57 32 99 81

# output : 3
