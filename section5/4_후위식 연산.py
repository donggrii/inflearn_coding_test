# 답안 예시
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
