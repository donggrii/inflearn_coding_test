# 내 풀이 (정답)
# 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 최대합 출력
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix_col = list(zip(*matrix))
result = -2147000000  # 최대값

for i in range(n):
    result = max(result, sum(matrix[i]))  # (1) 각 행의 합
    result = max(result, sum(matrix_col[i]))  # (2) 각 열의 합

# (3) 두 대각선의 합
diag0, diag1 = 0, 0
for i in range(n):
    diag0 += matrix[i][i]  # [0, 0], [1, 1], ..., [4, 4]
    diag1 += matrix[i][-i - 1]  # [0, -1], [1, -2], ..., [4, -5]

result = max(result, diag0, diag1)

with open("output6.txt", "a") as f:
    print(result, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]  # 행의 합
        sum2 += a[j][i]  # 열의 합
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)


# Test Case.
# < input >
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# output : 155
