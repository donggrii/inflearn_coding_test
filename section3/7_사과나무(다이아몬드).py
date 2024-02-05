# 내 풀이 (정답)
# 문제 : 수확한 사과의 총 개수
import sys

sys.stdin = open("input.txt", "r")

n = int(input())  # N은 홀수 (3 <= N <= 20)
matrix = [list(map(int, input().split())) for _ in range(n)]

mid = n // 2
result = sum(matrix[mid])  # 중간
for i in range(mid):
    result += sum(matrix[i][mid - i : mid + i + 1])  # 중간 위
    result += sum(matrix[-i - 1][mid - i : mid + i + 1])  # 중간 아래

with open("output7.txt", "a") as f:
    print(result, file=f)


# 정답 해설
# 0번째 행부터 마지막 행까지 다이아몬드 형태로 개수를 더해 나감
# 다이아몬드 형태 : (start - 1, end + 1) - (중간 지점) - (start + 1, end - 1)
import sys

sys.stdin = open("input.txt", "r")

n = int(input())  # N은 홀수 (3 <= N <= 20)
matrix = [list(map(int, input().split())) for _ in range(n)]
result = 0
start = end = n // 2

for i in range(n):
    for j in range(start, end + 1):
        result += matrix[i][j]
    if i < n // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(result)


# Test Case.
# < input >
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

# < output >
# 379
