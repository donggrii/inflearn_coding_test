# # 내 풀이 1 (실패)
# # [회고]
# # - 종료 조건을 어떻게 설정해야 할 지 헷갈렸음
# # - level이 아닌 sum_으로 종료하려고 했더니 level에서 IndexError 발생
# # - [내 풀이 2]처럼, 10원 x 2개인 경우는 5원 x 0개, 1원 x 0개로 생각하고 원래처럼 level(동전의 종류 수)로 종료 조건 설정해서 말단 노드에서 종료되게 하면 됨
# import sys

# sys.stdin = open("input.txt", "r")


# def DFS(level, sum_):
#     global cnt
#     if level <= total_nums:
#         if sum_ > total:
#             return
#         elif sum_ == total:
#             cnt += 1
#         else:
#             for i in range(coins[level][1], -1, -1):
#                 DFS(level + 1, sum_ + (coins[level][0] * i))


# if __name__ == "__main__":
#     total = int(input())
#     total_nums = int(input())
#     coins = [tuple(map(int, input().split())) for _ in range(total_nums)]
#     coins.sort(reverse=True)
#     cnt = 0
#     DFS(0, 0)
#     print(cnt)


# 내 풀이 2 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global cnt
    if sum_ > total:
        return
    if level == total_nums:
        if sum_ == total:
            cnt += 1
    else:
        for i in range(coins[level][1], -1, -1):
            DFS(level + 1, sum_ + (coins[level][0] * i))


if __name__ == "__main__":
    total = int(input())
    total_nums = int(input())
    coins = [tuple(map(int, input().split())) for _ in range(total_nums)]
    coins.sort(reverse=True)
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 정답 해설
# [참고]
# - 원래 이 문제의 동전의 가지수(k)가 100 이하였는데, 10 이하인 것으로 변형해서 DFS 문제로 만드신 것
# - 원래대로 k가 100 이하라면, 시간 복잡도 때문에 DFS가 아닌 DP(냅색 알고리즘)로 해결해야 하는 문제임
# [시간 복잡도]
# - 수정된 문제의 시간 복잡도 : 10(동전의 최대 종류 수)^10(각 동전의 최대 개수)
# - 원래 문제의 시간 복잡도 : 100(동전의 최대 종류 수)^10(각 동전의 최대 개수)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global cnt
    if sum_ > total:
        return
    if level == total_nums:
        if sum_ == total:
            cnt += 1
    else:
        for i in range(coin_nums[level] + 1):
            DFS(level + 1, sum_ + (coin_values[level] * i))


if __name__ == "__main__":
    total = int(input())
    total_nums = int(input())
    coin_values = []
    coin_nums = []
    for _ in range(total_nums):
        a, b = map(int, input().split())
        coin_values.append(a)
        coin_nums.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)


# Test Case.
# < input >
# 20
# 3
# 5 3
# 10 2
# 1 5

# < output >
# 4
