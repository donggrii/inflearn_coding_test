# 내 풀이 (정답) (but, 45분 소요)
# 문제 : 총 감의 개수 구하기
#        회전 명령 정보 -> (행 번호, 방향(0: 왼쪽, 1: 오른쪽), 회전하는 격자의 수)
import sys

sys.stdin = open("input.txt", "r")
n = int(input())  # N은 홀수 (3 <= N <= 20)
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
command = [list(map(int, input().split())) for _ in range(m)]


def rotate(row, direction, count):
    result = row.copy()
    if direction == 0:  # 왼쪽
        index = list(map(lambda x: x - count, range(n)))
    else:  # 오른쪽
        index = list(map(lambda x: (x + count) % n, range(n)))

    for i in range(n):
        result[index[i]] = row[i]

    return result


for x, d, c in command:
    c %= n
    matrix[x - 1] = rotate(matrix[x - 1], d, c)

mid = n // 2
result = matrix[mid][mid]  # 중간
for i in range(1, mid + 1):
    result += sum(matrix[mid - i][mid - i : mid + i + 1])  # 중간 위
    result += sum(matrix[mid + i][mid - i : mid + i + 1])  # 중간 아래

with open("output8.txt", "a") as f:
    print(result, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())  # N은 홀수 (3 <= N <= 20)
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for _ in range(m):
    h, t, k = map(int, input().split())
    if t == 0:  # 왼쪽
        for _ in range(k):  # k만큼 회전
            a[h - 1].append(a[h - 1].pop(0))  # 1번의 회전
    else:  # 오른쪽
        for _ in range(k):
            a[h - 1].insert(0, a[h - 1].pop())

res = 0
s = 0
e = n - 1

for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)


# Test Case.
# < input >
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4

# output : 362
