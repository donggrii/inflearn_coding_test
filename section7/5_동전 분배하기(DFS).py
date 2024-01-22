# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_a, sum_b, sum_c):
    global min_result
    if level == n:
        result = sum_a, sum_b, sum_c
        if len(set(result)) == 3:
            min_result = min(min_result, max(result) - min(result))
    else:
        DFS(level + 1, sum_a + coins[level], sum_b, sum_c)
        DFS(level + 1, sum_a, sum_b + coins[level], sum_c)
        DFS(level + 1, sum_a, sum_b, sum_c + coins[level])


if __name__ == "__main__":
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    min_result = 2147000000
    DFS(0, 0, 0, 0)
    print(min_result)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")


def DFS(level):
    global min_result
    if level == n:
        gap = max(money) - min(money)
        if gap < min_result:
            tmp = set(money)
            if len(tmp) == 3:
                min_result = gap
    else:
        for i in range(3):
            money[i] += coins[level]
            DFS(level + 1)
            money[i] -= coins[level]  # 주의! 다시 되돌려 놔야 함


if __name__ == "__main__":
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    money = [0] * 3
    min_result = 2147000000
    DFS(0)
    print(min_result)


# Test Case.
# < input >
# 7
# 8
# 9
# 11
# 12
# 23
# 15
# 17

# < output >
# 5
