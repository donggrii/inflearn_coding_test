# 내 풀이 (설명 듣고 다시 풀어보기 -> 성공!)
# < 조건 >
# 1. 넓이가 큰 벽돌이 밑으로 가야 함
# 2. 무게가 무거운 벽돌이 밑으로 가야 함
n = int(input())
total = [list(map(int, input().split())) for _ in range(n)]  # 밑면의 넓이, 높이, 무게 (양의 정수)
total.sort(key=lambda x: x[0], reverse=True)  # 넓이 순으로 내림차순 정렬
area = [x[0] for x in total]
h = [x[1] for x in total]
w = [x[2] for x in total]

d = [0] * n
d[0] = h[0]
res = 0
for i in range(1, n):
    max_ = 0
    for j in range(i - 1, -1, -1):
        if w[j] > w[i] and d[j] > max_:
            max_ = d[j]
    d[i] = max_ + h[i]
    if d[i] > res:
        res = d[i]

print(res)


# 답안 예시
# 최대 부분 증가 수열과 같은 맥락의 문제
# (중요) 밑면의 넓이를 기준으로 내림차순 정렬하면, 우리는 무게 조건만 고려해주면 됨!
# dy[n]의 의미 : n번 벽돌이 제일 꼭대기에 있을 때의 길이
n = int(input())
bricks = []
for i in range(n):
    a, b, c = map(int, input().split())
    bricks.append((a, b, c))
bricks.sort(reverse=True)  # 어차피 0번 값 기준으로 정렬되니까 (key=lambda x: x[0]) 할 필요 X
dy = [0] * n
dy[0] = bricks[0][1]
res = bricks[0][1]
for i in range(1, n):
    max_h = 0
    for j in range(i - 1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + bricks[i][1]
    res = max(res, dy[i])
print(res)


# Test Case.
# < input >
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2

# output : 10 (d = [3, 2, 5, 4, 10])
