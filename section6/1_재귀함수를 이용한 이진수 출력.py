# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(n):
    if n > 0:
        quotient, remainder = divmod(n, 2)
        DFS(quotient)
        print(remainder, end="")


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# (과거) 내 풀이
from typing import List


def dfs(x: int, lst: List[str]):
    if x > 0:
        lst.append(str(x % 2))  # ['1', '1', '0', '1']
        x //= 2  # 0
        dfs(x, lst)
    else:
        print(int("".join(reversed(lst))))


if __name__ == "__main__":
    n = int(input())  # 11
    answer = []
    dfs(n, answer)  # 1011


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")


def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end="")


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# Test Case.
# < input >
# 11

# < output >
# 1011
