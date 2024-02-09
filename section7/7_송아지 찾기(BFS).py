# 내 풀이 (실패, 60점, 4 ~ 5번 TC 시간초과)
# 한 번 방문한 곳은 체크해두고 다시 방문하지 않을 때 시간 안에 풀 수 있음
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

start, end = map(int, input().split())
jumps = (1, -1, 5)

queue = deque()
queue.append((0, start))

while queue:
    count, position = queue.popleft()
    if position == end:
        print(count)
        queue.clear()
        break
    count += 1
    for i in jumps:
        queue.append((count, position + i))


# 내 풀이 2 (성공)
# 1. 강의 이론만 듣고 다시 풀어본 풀이, 처음에는 실패(80점, 5번 TC 답 안 나옴)
# 2. jumped 구할 때 (current + i)의 범위를 0 ~ 10000으로 한정해줬을 때 성공
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

start, end = map(int, input().split())
jumps = (1, -1, 5)
distance = [0] * 10001  # 직선의 좌표 점은 1부터 10,000까지 존재
check = [0] * 10001
check[start] = 1

queue = deque([start])

while queue:
    current = queue.popleft()
    if current == end:
        print(distance[current])
        break
    for i in jumps:
        jumped = (current + i) if 0 <= (current + i) <= 10000 else start
        if check[jumped] == 0:
            distance[jumped] = distance[current] + 1
            check[jumped] = 1
            queue.append(jumped)


# 정답 해설
# 거리 배열 사용
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

MAX = 10000
check = [0] * (MAX + 1)
distance = [0] * (MAX + 1)
start, end = map(int, input().split())
check[start] = 1  # 방문 표시
distance[start] = 0

queue = deque()
queue.append(start)

while queue:
    now = queue.popleft()
    if now == end:
        break
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:
            if check[next] == 0:
                queue.append(next)
                check[next] = 1
                distance[next] = distance[now] + 1

print(distance[end])


# 정답 해설 2
# for문에서 도착 지점 발견 시 바로 종료하기
import sys
from collections import deque

sys.stdin = open("input.txt", "r")

MAX = 10000
check = [0] * (MAX + 1)
distance = [0] * (MAX + 1)
start, end = map(int, input().split())
check[start] = 1
distance[start] = 0

queue = deque()
queue.append(start)
flag = False

while queue:
    now = queue.popleft()
    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX:
            if check[next] == 0:
                queue.append(next)
                check[next] = 1
                distance[next] = distance[now] + 1
                if next == end:
                    flag = True
                    break
    if flag:
        break

print(distance[end])


# Test Case.
# < input >
# 5 14

# < output >
# 3
