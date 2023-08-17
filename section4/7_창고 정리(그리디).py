# 내 풀이 (성공)
# 구해야 하는 것 : M회 높이 조정(= 가장 높은 곳의 상자를 가장 낮은 곳으로 이동) 후 가장 높은 곳과 가장 낮은 곳의 차이 출력
# 1. 최댓값, 최솟값 기준 연산을 해야 하니, 정렬을 해 두면 좋을 것이라 생각
# 2. 가장 간단한 방법 : M만큼 반복하면서, 가장 큰 값 -1, 가장 작은 값 +1, 정렬
#                       => nums는 늘 정렬 상태 유지
import sys

sys.stdin = open("input.txt", "r")
w = int(input())
nums = list(map(int, input().split()))
m = int(input())
nums.sort()

for _ in range(m):
    nums[-1] -= 1
    nums[0] += 1
    nums.sort()

result = nums[-1] - nums[0]

with open("output7.txt", "a") as f:
    print(result, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()

for _ in range(m):
    a[0] += 1
    a[L - 1] -= 1
    a.sort()

print(a[L - 1] - a[0])


# Test Case.
# < input >
# 10
# 69 42 68 76 40 87 14 65 76 81
# 50

# < output >
# 20
