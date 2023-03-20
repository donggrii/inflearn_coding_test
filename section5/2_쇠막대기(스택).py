# 내 풀이 (실패.. -> 설명 듣고 다시 해보기 -> 성공!)
import sys


input = sys.stdin.readline
s = input().rstrip()
stack = []
sum_ = 0
for i in range(len(s)):
    if s[i] == ")":
        if not stack:
            continue
        if s[i - 1] == "(":
            stack.pop()
            sum_ += len(stack)
        elif s[i - 1] == ")":
            stack.pop()
            sum_ += 1
    else:
        stack.append("(")
print(sum_)


# 답안 예시
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else:
        stack.pop()  # 밑의 if, else 부분에서 둘 다 pop()하므로 아예 여기서 한번만 작성해주기
        if s[i - 1] == "(":
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)
