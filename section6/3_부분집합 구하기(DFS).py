# 정답 해설
import sys

sys.stdin = open("input.txt", "r")


def DFS(v):
    if v == (n + 1):  # 종착점(종료) 설정
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=" ")
        print()
    else:
        check[v] = 1  # 부분집합으로 사용 O
        DFS(v + 1)
        check[v] = 0  # 부분집합으로 사용 X
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n + 1)
    DFS(1)


# Test Case.
# < input >
# 3

# < output >
# 1 2 3
# 1 2
# 1 3
# 1
# 2 3
# 2
# 3
