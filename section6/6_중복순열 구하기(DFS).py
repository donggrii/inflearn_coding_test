# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, arr):
    global cnt
    if level == m:
        for x in range(m):
            print(arr[x], end=" ")
        print()
        cnt += 1
    else:
        for i in range(n):
            DFS(level + 1, arr + [nums[i]])


if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(range(1, n + 1))
    cnt = 0
    DFS(0, [])
    print(cnt)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")


def DFS(level):
    global cnt
    if level == m:
        for j in range(m):
            print(result[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            result[level] = i
            DFS(level + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)


# Test Case.
# < input >
# 3 2

# < output >
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
# 9
