# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")


def DFS(v):
    if v == n:
        sum_ = 0
        for i in range(n):
            if check[i] == 1:
                sum_ += lst[i]
        if sum_ * 2 == total:
            result = "YES"
            print(result)
            sys.exit(0)
    else:
        check[v] = 1
        DFS(v + 1)
        check[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    check = [0] * n

    total = sum(lst)
    result = "NO"
    DFS(0)
    print(result)


# 정답 해설 1
# 부분 집합의 합을 sum_ 변수에 누적하는 상태 트리 구성
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    if sum_ > total / 2:  # Cut Edge, 가지치기 (시간 복잡도 개선)
        return
    if level == n:
        if sum_ == (total - sum_):
            print("YES")
            sys.exit(0)  # 프로그램 전체 종료 (0: 정상 종료, 1: 비정상 종료)
    else:
        DFS(level + 1, sum_ + a[level])  # 부분집합으로 사용 O
        DFS(level + 1, sum_)  # 부분집합으로 사용 X


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")  # 프로그램 종료되지 않았다면 "NO" 출력


# 정답 해설 2 : sys.exit(0) 사용하지 않고 종료하는 방법
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global answer, flag
    if flag:  # 신호 변수를 두고, 답을 구하면 그 다음 호출들은 바로 종료
        return
    if sum_ > total / 2:
        return
    if level == n:
        if sum_ == (total - sum_):
            answer = "YES"
            flag = True
    else:
        DFS(level + 1, sum_ + a[level])
        DFS(level + 1, sum_)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    answer = "NO"
    flag = False
    DFS(0, 0)
    print(answer)


# Test Case.
# < input >
# 6
# 1 3 5 6 7 10

# < output >
# YES
