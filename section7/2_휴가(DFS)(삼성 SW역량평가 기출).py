# 내 풀이 (정답)
# 최대 이익을 얻는 부분 집합 구하기 => DFS 적용
# 회고 : due가 n을 초과할 경우를 고려하지 않았을 때 1, 3, 4 TC에서 index 오류로 40점을 받음
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_price, due):
    global max_price
    if level < due:
        DFS(level + 1, sum_price, due)
        return
    if level == n:
        max_price = max(max_price, sum_price)
    else:
        # DFS(level + 1, sum_price + prices[level], level + days[level])
        if level + days[level] <= n:
            DFS(level + 1, sum_price + prices[level], level + days[level])
        DFS(level + 1, sum_price, due)


if __name__ == "__main__":
    n = int(input())
    days = []
    prices = []
    for _ in range(n):
        day, price = map(int, input().split())
        days.append(day)
        prices.append(price)
    max_price = -2147000000
    DFS(0, 0, 0)
    print(max_price)


# 정답 해설
# [내 풀이]에서 due 라는 인자를 따로 두지 않아도, level을 X일이라고 가정하면 됨
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global result
    if level == (n + 1):
        if sum_ > result:
            result = sum_
    else:
        if level + days[level] <= (n + 1):
            DFS(level + days[level], sum_ + prices[level])
        DFS(level + 1, sum_)


if __name__ == "__main__":
    n = int(input())
    days = []
    prices = []
    for _ in range(n):
        day, price = map(int, input().split())
        days.append(day)
        prices.append(price)
    result = -2147000000
    days.insert(0, 0)
    prices.insert(0, 0)
    DFS(1, 0)
    print(result)


# 다른 풀이 (조합 푸는 방식)
import sys

sys.stdin = open("input.txt", "r")


def DFS(time, price):
    global max_price
    if time > n:
        return
    max_price = max(max_price, price)
    for i in range(time, n):
        DFS(i + lst[i][0], price + lst[i][1])


if __name__ == "__main__":
    n = int(input())
    lst = []
    for _ in range(n):
        time, price = map(int, input().split())
        lst.append((time, price))
    max_price = 0
    DFS(0, 0)
    print(max_price)


# Test Case.
# < input >
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10

# < output >
# 60
