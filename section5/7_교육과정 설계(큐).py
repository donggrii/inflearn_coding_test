# 내 풀이 1 (오답) : 수업계획서를 queue로 설정
# 정답률 80% (4/5)
# ⇒ 수업계획서 상에서 필수과목 순서상 뒤에 있는 과목이 앞에 있는 과목보다 먼저 나오면 안 됨..
# ⇒ (ex) 필수과목 : AKDEF, 수업계획서 : AFKDEF
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
crit = input()
n = int(input())
lst = [input() for _ in range(n)]

crit_len = len(crit)
for i in range(n):
    dq_lst = deque(lst[i])
    result = [False] * crit_len
    for j in range(crit_len):
        x = crit[j]
        while dq_lst:
            y = dq_lst.popleft()
            if x == y:
                result[j] = True
                break
    if all(result):
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")


# 내 풀이 2 (정답) : 필수과목을 queue로 설정
# 문제 풀이 방향에 대한 강의만 듣고 다시 풀어봤을 때, 정답을 맞췄음
# (cf) 필수과목 이수 안 한 경우도 존재할 수 있음
# ⇒ (ex) 필수과목 : AKDEF, 수업계획서 : AYKGDHEJ
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
crit = input()
n = int(input())
lst = [input() for _ in range(n)]

for i in range(n):
    dq = deque(crit)
    plan = lst[i]
    for x in plan:
        if x in dq:  # 필수과목인지 확인
            y = dq.popleft()
            if x != y:  # 순서가 맞지 않을 경우
                dq.append(y)
                break
    if len(dq) == 0:
        print(f"#{i + 1} YES")
    else:  # 순서가 맞지 않았거나, 필수 과목을 전부 이수하지 않은 경우
        print(f"#{i + 1} NO")


# 정답 해설
# [확인해야 할 것]
# 1. 필수과목의 "순서"가 맞는지
# 2. 필수과목을 "전부" 수업계획서에 넣었는지
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq and x != dq.popleft():  # 필수과목인지 확인 and 순서가 맞지 않을 경우
            print("#%d NO" % (i + 1))
            break
    else:  # 순서가 모두 맞았다면
        # 필수과목을 전부 수업계획서에 넣었는지 확인
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))


# Test Case 1.
# < input >
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA

# < output >
# #1 YES
# #2 NO
# #3 YES

# Test Case 2.
# < input >
# AFC
# 1
# AFFDCCFF

# < output >
# #1 YES
