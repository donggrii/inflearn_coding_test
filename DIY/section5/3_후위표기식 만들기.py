# 답안 예시
# 스택 자료구조를 이용하여 중위표기식 -> 후위표기식(연산자가 피연산자 뒤에 있는 표기식)
# 연산 우선순위 : (*, /) -> (+, -)
# *, /를 만나면 스택에 있는 연산 중 *, / 연산을 처리해주기 (우선순위가 빠르지 않다면, 꺼내지 않음)
# +, -를 만나면 스택에 있는 연산들을 모두 처리 (스택이 비어 있으면 append)
# => +, -보다 후순위인 연산은 없고, 스택에 있다는 건 더 먼저 나온 연산자인 것!
# => 피연산자(숫자)는 다른 str 변수에 누적시키기
# "(" : 여는 괄호는 무조건 append
# -> ")" : 닫는 괄호 만났을 때 여는 괄호 꺼내야 함
a = input()
stack = []
res = ""  # 출력을 누적
for x in a:
    if x.isdecimal():  # 피연산자(숫자)인지 확인
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()  # "(" 빼주기
while stack:  # for문이 다 돌았을 때도 stack에 값이 남아 있다면 전부 꺼내서 더해주기
    res += stack.pop()
print(res)


# Test Case 1.
# input = 3+5*2/(7-2)
# output : 352*72-/+

# Test Case 2.
# input = 3*(5+2)-9
# output : 352+*9-
