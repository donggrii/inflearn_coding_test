# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, start_idx):
    global cnt
    if level == k:
        if sum(result) % m == 0:
            cnt += 1
    else:
        for i in range(start_idx, n):
            result[level] = nums[i]
            DFS(level + 1, i + 1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())
    result = [0] * k
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 정답 해설 1 (DFS)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, start_idx, sum_):
    global cnt
    if level == k:
        if sum_ % m == 0:
            cnt += 1
    else:
        for i in range(start_idx, n):
            DFS(level + 1, i + 1, sum_ + nums[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)


# 정답 해설 2 (itertools 라이브러리를 이용한 조합)
import sys
import itertools as it

sys.stdin = open("input.txt", "r")

n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())
cnt = 0
for x in it.combinations(nums, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)


# Test Case.
# < input >
# 5 3
# 2 4 5 8 12
# 6

# < output >
# 2
