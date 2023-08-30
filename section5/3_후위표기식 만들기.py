# 정답 해설
# [문제] : 중위표기식 → 후위표기식(연산자가 피연산자 뒤에 있는 표기식) 변환
#          (참고) 컴퓨터는 순차처리를 하기 때문에 중위표기식을 처리하기 어려움
#           ⇒ 컴퓨터는 후위 표기식을 더 처리하기 쉬움

# [아이디어] : 스택 자료구조를 이용해 연산자 처리, 피연산자(숫자)는 문자열 변수에 누적
# 1. 연산 우선순위 : (*, /) > (+, -)
#    a. *, / 를 만나면 스택에 있는 연산자 중 *, / 연산자 먼저 처리 (우선순위가 빠르지 않다면, 꺼내지 않음)
#    b. +, - 를 만나면 스택에 있는 연산자를 모두 처리
#       ⇒ +, -보다 후순위인 연산은 없고, 같은 +, - 라도 스택에 있다는 건 더 먼저 나온 연산자인 것!
#    c. 스택이 비어 있으면 연산자를 append
# 2. "(" : 여는 괄호는 무조건 append
#    ⇒ ")" : 닫는 괄호 만났을 때, "("가 나올 때까지 연산자 모두 붙여주고, "("를 꺼내야 함

# [Tip] : if문을 쓸 때, "우선순위가 높은 것"부터 써주는 게 효율적임
import sys

sys.stdin = open("input.txt", "r")
a = input()  # 중위표기식

stack = []
res = ""  # 출력을 누적
for x in a:
    if x.isdecimal():  # 피연산자(숫자)인 경우
        res += x
    else:  # 연산자인 경우
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":  # 스택이 빌 때까지 or (가 나오기 전까지
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":  # 스택이 빌 때까지 or (가 나오기 전까지
                res += stack.pop()
            stack.pop()  # "(" 빼주기

while stack:  # for문이 다 돌았을 때도 stack에 연산자가 남아 있다면, 전부 꺼내서 더해주기
    res += stack.pop()

print(res)


# 정답 해설 Refactoring
import sys

sys.stdin = open("input.txt", "r")
a = input()  # 중위표기식

stack = []
res = ""  # 출력을 누적
for x in a:
    if x.isdecimal():  # 피연산자(숫자)인 경우
        res += x
    # 연산자인 경우
    elif x == "(":
        stack.append(x)
    elif x in ["*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            res += stack.pop()
        stack.append(x)
    elif x in ["+", "-"]:
        while stack and stack[-1] != "(":  # 스택이 빌 때까지 or (가 나오기 전까지
            res += stack.pop()
        stack.append(x)
    elif x == ")":
        while stack and stack[-1] != "(":  # 스택이 빌 때까지 or (가 나오기 전까지
            res += stack.pop()
        stack.pop()  # "(" 빼주기

while stack:  # for문이 다 돌았을 때도 stack에 연산자가 남아 있다면, 전부 꺼내서 더해주기
    res += stack.pop()

print(res)


# Test Case 1.
# input : 3+5*2/(7-2)
# output : 352*72-/+

# Test Case 2.
# input : 3*(5+2)-9
# output : 352+*9-
