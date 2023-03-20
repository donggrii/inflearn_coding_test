# 내 풀이 (성공!)
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


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = sorted(map(int, input().split()))
    result = binary_search(nums, 0, n - 1, m)

    if result is None:
        print("찾을 수 없습니다.")
    else:
        print(result + 1)


# 답안 예시
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
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


# Test Case.
# < input >
# 8 32
# 23 87 65 12 57 32 99 81

# output : 3
