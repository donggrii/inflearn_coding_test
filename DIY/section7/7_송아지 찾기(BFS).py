# 내 풀이 (설명만 듣고 다시 풀기 -> 성공!)
# 현재 위치 기준으로 푼 내 풀이보다 다음 위치 기준으로 푼 답안이 더 좋아보임
from collections import deque


s, e = map(int, input().split())
ch = [0] * 10001
dist = [0] * 10001
q = deque([(s, 0)])
while q:
    cur, res = q.popleft()
    if cur == e:
        print(res)
        break
    if 0 <= cur <= 10000 and ch[cur] == 0:  # 현재 위치 기준
        ch[cur] = 1
        dist[cur] = res
        for i in [1, -1, 5]:
            q.append((cur + i, res + 1))


# 답안 예시
from collections import deque


n, m = map(int, input().split())
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
ch[n] = 1  # 방문 표시
dis[n] = 0
dQ = deque([n])
while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now - 1, now + 1, now + 5):  # 다음 위치 기준
        if 0 < next <= MAX and ch[next] == 0:
            dQ.append(next)
            ch[next] = 1
            dis[next] = dis[now] + 1
print(dis[m])


# Test Case.
# input : 5 14
# output : 3
