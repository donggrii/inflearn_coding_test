# 내 풀이 (정답)
# 회고 : check 변수에 숫자 사용 여부에 대한 정보를 저장했지만, 순서 정보를 저장할 변수가 추가로 필요했음
#       따라서, result 변수에 순서 정보를 저장해 출력함
import sys

sys.stdin = open("input.txt", "r")


def DFS(level):
    global cnt
    if level == m:
        for j in range(m):
            print(result[j] + 1, end=" ")
        print()
        cnt += 1
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                result[level] = i
                DFS(level + 1)
                check[i] = 0
                result[level] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [0] * n
    result = [0] * m
    cnt = 0
    DFS(0)
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
            if check[i] == 0:
                check[i] = 1
                result[level] = i
                DFS(level + 1)
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    check = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)


# Test Case.
# < input >
# 3 2

# < output >
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2
# 6
