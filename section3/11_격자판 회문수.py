# 내 풀이 (정답)
# 회고 : 내 풀이도 빠르게 풀기엔 좋지만, matrix의 크기가 만약 10만 x 10만으로 매우 크다면 matrix_col을 따로 만드는 게 공간 복잡도가 좋지 않을 수 있음
#        따라서, "주어진 입력만을 가지고 index를 조절하며 회문을 판단"하는 정답 해설 코드를 숙지하면 좋을 것
import sys

sys.stdin = open("input.txt", "r")
matrix = [list(map(int, input().split())) for _ in range(7)]
matrix_col = list(zip(*matrix))
sections = [(0, 5), (1, 6), (2, 7)]


def check_palindrome(lst):
    return all(lst[i] == lst[-i - 1] for i in range(2))


cnt = sum(check_palindrome(row[s:e]) for row in matrix for s, e in sections)
cnt += sum(check_palindrome(col[s:e]) for col in matrix_col for s, e in sections)

with open("output11.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        # 행 : 회문 검사
        tmp = board[j][i : i + 5]
        if tmp == tmp[::-1]:
            cnt += 1
        # 열 : 회문 검사
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            cnt += 1

print(cnt)


# Test Case.
# < input >
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5

# output : 3
