# 내 풀이 (정답)
# 1. (i번째 환자, 위험도)로 만들어서 queue로 만들기
# 2. queue에서 popleft() : 현재값
#    2-1. 남은 값 중 위험도 더 큰 게 있으면 현재값은 뒤로 append()
#    2-2. 더 큰 값이 없으면 cnt + 1, (i번째 환자 == m) 일 경우 cnt 출력하고 종료
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
dq = list(map(int, input().split()))
dq = deque(enumerate(dq))  # (i번째 대기 환자, 위험도)

cnt = 0
while dq:
    i, danger = dq.popleft()
    for a, b in dq:
        if b > danger:
            dq.append((i, danger))
            break
    else:
        cnt += 1
        if i == m:
            print(cnt)
            break


# 정답 해설
# [주의할 점]
# - "내림차순 정렬해서 순서 따지면 되지 않나?"라고 생각할 수 있지만, 그렇지 않음!
# - Test Case 2. 경우처럼 동일한 위험도들이 주어질 때, 같은 위험도의 환자만 남는다고 해서 처음에 0번째에 있던 환자가 바로 진료받을 수 있는 게 아니기 때문!

# [배울 점]
# - 현재보다 위험도가 높은 사람이 있는지 확인할 때, for문보다 any() 함수 사용한 것
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
# Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = list(enumerate(map(int, input().split())))
Q = deque(Q)

cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):  # any(expression) : 단 하나라도 expression이 True인 값이 있다면, 결과값은 True
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break


# Test Case 1.
# < input >
# 5 2
# 60 50 70 80 90

# < output >
# 3

# Test Case 2.
# < input >
# 6 0
# 60 60 90 60 60 60

# < output >
# 5
