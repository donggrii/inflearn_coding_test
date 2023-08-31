# 내 풀이 (정답)
# [문제] : 후위연산식이 주어지면 연산한 결과를 출력

# [아이디어]
# 1. 숫자는 스택에 append
# 2. 연산자가 나오면, 스택에서 순서대로 pop으로 뽑은 a, b
#    ⇒ result = (b (연산자) a)를 stack에 다시 append
#    ⇒ eval() 사용, int 반환값을 str으로 다시 변환
# 3. for문이 끝나면 stack에 남아있는 하나의 값이 최종 연산 결과
import sys

sys.stdin = open("input.txt", "r")
expr = input()

stack = []
for x in expr:
    if x.isdecimal():
        stack.append(x)
    else:
        a = stack.pop()
        b = stack.pop()
        result = eval(b + x + a)
        stack.append(str(result))

result = stack[0]
with open("output4.txt", "a") as f:
    print(result, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
a = input()

stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == "+":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == "-":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == "*":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == "/":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)

print(stack[0])


# Test Case.
# input : 352+*9-
# output : 12
