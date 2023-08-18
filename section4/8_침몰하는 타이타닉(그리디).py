# 내 풀이 (정답)
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort(reverse=True)
queue = deque(weights)

cnt = 0
while queue:
    if len(queue) >= 2:
        if (queue[0] + queue[-1]) > m:  # 한 사람만 타고 가는 경우
            queue.popleft()
        else:  # 두 사람이 타고 가는 경우
            queue.popleft()
            queue.pop()
        cnt += 1
    else:
        cnt += 1
        break

with open("output8.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)
cnt = 0

while p:
    if len(p) == 1:
        cnt += 1
        break
    if p[0] + p[-1] > limit:  # 한 사람만 타고 가는 경우
        p.pop()
        cnt += 1
    else:  # 두 사람이 타고 가는 경우
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)


# Test Case.
# < input >
# 5 140
# 90 50 70 100 60

# < output >
# 3
