# 내 풀이 (성공!)
from collections import deque


n, k = map(int, input().split())  # 8, 3
queue = deque(list(range(1, n + 1)))
cnt = 0
while queue:
    p = queue.popleft()
    cnt += 1
    if cnt == k:
        cnt = 0
        if len(queue) == 1:
            print(queue[0])  # 7
    else:
        queue.append(p)


# 답안 예시
# 큐 자료구조 (FIFO : First In First Out) <-> 스택 자료구조 (LIFO : Last In First Out)
from collections import deque


n, k = map(int, input().split())  # 8, 3
dq = deque(list(range(1, n + 1)))
while dq:
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
