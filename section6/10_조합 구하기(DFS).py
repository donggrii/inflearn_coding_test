# 내 풀이 (성공)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, start):
    global cnt
    if level == m:
        for x in range(m):
            print(result[x], end=" ")
        print()
        cnt += 1
    else:
        for i in range(start, n + 1):
            if check[i] == 0:
                check[i] = 1
                result[level] = i
                DFS(level + 1, i + 1)
                check[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [0] * (n + 1)
    result = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)


# 정답 해설
# [조합 구하기] 문제 매우 중요! (기본이 되어 많이 응용되어 출제됨)
# - [순열 구하기]와 코드는 유사하지만, 상태 트리의 유형이 다름 => start 변수가 추가되고, check 변수 사용 X
# (참고) 조합에서는 왜 check 변수가 필요 없을까? (순열 vs. 조합)
#        순열 : (1, 2), (1, 3), (1, 4), "(2, 1)"
#        조합 : (1, 2), (1, 3), (1, 4), "(2, 3)"
#        => 조합은 (2, 1)처럼 사용했던 숫자를 다시 쓰지 않고, start 변수에 따라 어차피 순서대로 조합을 구하기 때문
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, start):
    global cnt
    if level == m:
        for j in range(m):
            print(result[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(start, n + 1):
            result[level] = i
            DFS(level + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    result = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)


# Test Case.
# < input >
# 4 2

# < output >
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4
# 6
