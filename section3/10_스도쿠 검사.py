# 내 풀이 (정답)
# 회고 : 각 행, 열에 1 ~ 9가 중복되어 나타나는지 따로 체크하지 않았는데 정답을 맞춤
#        이후엔 행, 열도 검사하는 것 고려하기
import sys

sys.stdin = open("input.txt", "r")
matrix = [list(map(int, input().split())) for _ in range(9)]
sections = [(0, 3), (3, 6), (6, 9)]
total = list(range(1, 10))


def check_sudoku():
    for s1, e1 in sections:
        for s2, e2 in sections:
            tmp = [matrix[x][y] for x in range(s1, e1) for y in range(s2, e2)]
            tmp.sort()
            if total != tmp:
                return "NO"
    return "YES"


with open("output10.txt", "a") as f:
    print(check_sudoku(), file=f)


# 정답 해설 1
# 행, 열, 3 x 3 격자 -> 총 3개의 체크리스트 필요
import sys

sys.stdin = open("input.txt", "r")


def check(a):
    # 1. 행, 열에 1 ~ 9가 있는지 체크
    for i in range(9):
        ch1 = [0] * 10  # 행 체크리스트
        ch2 = [0] * 10  # 열 체크리스트
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    # (중요) 2. 구간 탐색 : 각 3 x 3 격자에 1 ~ 9가 있는지 체크 (4중 for문)
    # 9개의 그룹을 보는 것
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            # 9개의 숫자를 보는 것
            for k in range(3):
                for s in range(3):
                    ch3[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")


# 정답 해설 2 (itertools.product를 이용해 2중 for문으로 변경)
# 행, 열, 3 x 3 격자 -> 총 3개의 체크리스트 필요
import sys
import itertools

sys.stdin = open("input.txt", "r")


def check(a):
    # 1. 행, 열에 1 ~ 9가 있는지 체크
    for i in range(9):
        ch1 = [0] * 10  # 행 체크리스트
        ch2 = [0] * 10  # 열 체크리스트
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    # (중요) 2. 구간 탐색 : 각 3 x 3 격자에 1 ~ 9가 있는지 체크 (2중 for문)
    # 9개의 그룹을 보는 것
    for i, j in itertools.product(range(3), range(3)):
        ch3 = [0] * 10
        # 9개의 숫자를 보는 것
        for k, s in itertools.product(range(3), range(3)):
            ch3[a[i * 3 + k][j * 3 + s]] = 1
        if sum(ch3) != 9:
            return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")


# Test Case.
# < input >
# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7

# output : YES
