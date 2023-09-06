# 내 풀이 1 (과거)(정답)
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())

queue = deque(list(range(1, n + 1)))
cnt = 0
while queue:
    p = queue.popleft()
    cnt += 1
    if cnt == k:
        cnt = 0
        if len(queue) == 1:
            print(queue[0])
            break
    else:
        queue.append(p)


# 내 풀이 2 (최근)(정답) : 순환하는 자료구조 => 큐 활용
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())

queue = deque(range(1, n + 1))
tmp = deque()
i = 0
while True:
    while queue:
        i += 1
        if i % k != 0:
            tmp.append(queue.popleft())
        else:
            queue.popleft()

    # queue가 비면 queue = tmp, 동시에 tmp 길이가 1이면 stop하고 출력
    if len(tmp) != 1:
        queue = tmp
        tmp = deque()
    else:
        break

with open("output5.txt", "a") as f:
    print(tmp[0], file=f)


# 정답 해설
# 큐(Queue) : FIFO (First In First Out)
# (cf) 스택(Stack) : LIFO (Last In First Out)
# 내 풀이 2(최근)과 달리 queue 1개만 사용하므로 공간 복잡도 ↓
# for문으로 (K-1)번 순환하도록 popleft(), append() 한 후 → K번째에 popleft()만 함
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, k = map(int, input().split())

dq = list(range(1, n + 1))
dq = deque(dq)
while dq:  # queue가 빌 때까지
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()  # while문 조건에 걸려서 종료되도록


# Test Case.
# < input >
# 8 3

# < output >
# 7
