# import sys
# sys.stdin = open("input.txt", "r")

# 내 풀이 (성공!)
from typing import List


def dfs(x: int, lst: List[str]):
    if x > 0:
        lst.append(str(x % 2))  # ['1', '1', '0', '1']
        x //= 2  # 0
        dfs(x, lst)
    else:
        print(int(''.join(reversed(lst))))


if __name__ == "__main__":
    n = int(input())  # 11
    answer = []
    dfs(n, answer)  # 1011


# 답안 예시
def DFS(x):
    if x == 0:
        return  # 값을 호출한 곳에 값을 반환해주는 의미도 있지만, 함수 종료 명령어도 됨
    else:
        DFS(x // 2)
        print(x % 2, end="")


if __name__ == "__main__":
    n = int(input())  # 11
    DFS(n)  # 1011
