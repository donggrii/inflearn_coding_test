# 내 풀이 1 (80% 정답, 3번 Test Case 오답)
# 회고 : 액수가 큰 동전을 많이 사용한다고 '무조건' 최소 개수의 동전을 사용하는 게 아님
# (ex) 아래의 Test Case 2의 경우, 7개(50, 50, 25, 1, 1, 1, 1) vs. 5개(50, 50, 20, 8, 1)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global flag
    if flag:
        return
    if sum_ > m:
        return
    elif sum_ == m:
        flag = True
        print(level)
        # sys.exit(0)
    else:
        for i in range(n):
            DFS(level + 1, sum_ + coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    flag = False
    DFS(0, 0)


# 내 풀이 2 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global result
    if level > result:  # Cut Edge : 현재까지 구한 최소 동전 개수보다 많다면 볼 필요 없음
        return
    if sum_ > m:
        return
    elif sum_ == m:
        result = min(result, level)
    else:
        for i in range(n):
            DFS(level + 1, sum_ + coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    result = 2147000000
    DFS(0, 0)
    print(result)


# 정답 해설
# Tip : 작은 값부터 넣으면 처음 출발이 너무 깊게 들어가므로 내림차순으로 가장 큰 동전부터 적용하기
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global result
    if level > result:
        return
    if sum_ > m:
        return
    if sum_ == m:
        if level < result:
            result = level
    else:
        for i in range(n):
            DFS(level + 1, sum_ + coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    result = 2147000000
    DFS(0, 0)
    print(result)


# Test Case 1.
# < input >
# 3
# 1 2 5
# 15

# < output >
# 3

# Test Case 2.
# < input >
# 5
# 1 8 20 25 50
# 129

# < output >
# 5
