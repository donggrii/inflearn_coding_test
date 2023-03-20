# import sys
# sys.stdin = open("input.txt", "r")


def DFS(x):
    if x > 0:
        DFS(x - 1)
        print(x, end=' ')


if __name__ == "__main__":
    n = int(input())  # 5
    DFS(n)  # 1 2 3 4 5
