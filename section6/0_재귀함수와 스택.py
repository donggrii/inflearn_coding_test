# 1. 재귀함수 : 반복문 대체(순서대로 출력)
# (ex) `DFS(3)` 함수 실행 시, 스택에 기록되는 3가지(스택 프레임) : 매개변수(x=3), 지역변수, 복귀주소(main - 19 line)
# (ex) `DFS(2)` 함수 실행 시, 스택에 기록되는 3가지(스택 프레임) : 매개변수(x=2), 지역변수, 복귀주소(D(3) - 13 line)
# (ex) `DFS(1)` 함수 실행 시, 스택에 기록되는 3가지(스택 프레임) : 매개변수(x=1), 지역변수, 복귀주소(D(2) - 13 line)
# (ex) `DFS(0)` 함수 실행 시, 스택에 기록되는 3가지(스택 프레임) : 매개변수(x=0), 지역변수, 복귀주소(D(1) - 13 line)
import sys

sys.stdin = open("input.txt", "r")


def DFS(x):
    if x > 0:
        DFS(x - 1)
        print(x, end=" ")


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# Test Case.
# < input >
# 3

# < output >
# 1 2 3


# 2. 재귀함수 : 반복문 대체(역순으로 출력)
import sys

sys.stdin = open("input.txt", "r")


def DFS(x):
    if x > 0:
        print(x, end=" ")
        DFS(x - 1)


if __name__ == "__main__":
    n = int(input())
    DFS(n)


# Test Case.
# < input >
# 3

# < output >
# 3 2 1
