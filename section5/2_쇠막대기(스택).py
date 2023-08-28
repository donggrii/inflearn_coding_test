# 내 풀이 (정답)
# 구해야 하는 것 : 잘려진 쇠막대기 조각의 총 개수

# [핵심 로직] : 스택을 활용
# 1. ( 는 무조건 append
# 2. ) 가 나오면 pop()으로 stack의 top을 하나 빼기
#    a. 레이저로 자를 때, 스택에 있는 모든 ( 개수 더하기
#       -> 레이저는 연속된 괄호 "()"로 알 수 있음
#    b. 쇠막대기가 끝날 때, + 1 해주기
#    => 그렇다면, a, b를 어떻게 구분하는가?
#       => 1번은 바로 직전에 ( 가 등장, 2번은 바로 직전에 ) 가 등장
import sys

sys.stdin = open("input.txt", "r")
total = input()

stack = []
cnt = 0
for i, x in enumerate(total):
    if x == "(":
        stack.append(x)
    else:
        stack.pop()
        cnt += len(stack) if total[i - 1] == "(" else 1

with open("output2.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
s = input()

stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == "(":
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)


# Test Case 1.
# < input >
# ()(((()())(())()))(())

# < output >
# 17

# Test Case 2.
# < input >
# (((()(()()))(())()))(()())

# < output >
# 24
