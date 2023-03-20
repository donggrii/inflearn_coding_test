# 내 풀이 (설명만 듣고 풀어보기 -> 성공!)
n, m = map(int, input().split())
n = list(str(n))
stack = []
idx = 0
while m > 0 and idx < len(n):
    if not stack:
        stack.append(n[idx])
    else:
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
    stack = stack[:-1]

print(int(''.join(stack)))

# 답안 예시
# 각 숫자들의 임무 : 나보다 앞에 있는 숫자가 나보다 작으면 안된다! -> m번 내에서 지우기
# 스택 : LIFO (Last In First Out) 나중에 들어간 게 먼저 나온다.
#        들어가는 입구와 나오는 출구가 1곳밖에 없음
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
res = ''.join(map(str, stack))
print(res)
