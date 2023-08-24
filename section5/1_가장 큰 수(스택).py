# 내 풀이 (설명만 듣고 풀어보기 -> 성공!)
# 문제 : 주어진 숫자, 제거 횟수를 활용해 가장 큰 수 만들기 (숫자의 순서는 유지)
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())

n = list(str(n))
stack = []
idx = 0
while m > 0 and idx < len(n):
    while stack and n[idx] > stack[-1]:
        stack.pop()
        m -= 1
        if m == 0:
            stack += n[idx:]
            break
    stack.append(n[idx])
    idx += 1

if m > 0:
    stack = stack[:-m]
elif m == 0:
    stack = stack[:-1]  # 17 line에서 break 해도 18 line에서 n[idx]를 또 append하기 때문

with open("output1.txt", "a") as f:
    print("".join(stack), file=f)


# 정답 해설
# [아이디어]
# 큰 숫자가 앞으로 갈수록 좋음

# [각 숫자의 임무]
# - (중요) 나보다 작은 값이 나보다 앞에 있으면 안 됨!
#   → 즉, 나보다 앞에 있는 값은 모두 나보다 커야 함 (내림차순)
# - 나보다 작은 값이 앞에 있으면 그 작은 값을 stack.pop(), 그리고 자신을 append()
# ⇒ 이렇게 이전 것을 지우고 다음 것을 앞으로 "자리 이동"하는 것
# ⇒ 스택 자료구조!

# [스택이란?]
# LIFO(Last In First Out)
# 들어가는 입구와 나오는 출구가 한 곳!
import sys

sys.stdin = open("input.txt", "r")
num, m = map(int, input().split())

num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:  # m > 0인 상태로 끝났을 경우
    stack = stack[:-m]
res = "".join(map(str, stack))
print(res)


# Test Case 1.
# < input >
# 5276823 3

# output : 7823

# Test Case 2.
# < input >
# 9977252641 5

# output : 99776
