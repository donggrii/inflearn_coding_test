# 내 풀이 (정답)
# 회고 : index를 뒤에서부터 세는 방법
#        1. s[len(s) - i - 1]
#        2. s[-1 - i]
#        (ex) 5면 0,1 range(2) | 6이면 0,1,2 range(3)
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
total = [input().lower().strip() for _ in range(n)]

with open("output1.txt", "a") as f:
    for k in range(n):
        tmp = total[k]
        for i in range(len(tmp) // 2):
            j = len(tmp) - i - 1
            if tmp[i] != tmp[j]:
                print(f"#{k + 1} NO", file=f)
                break
        else:
            print(f"#{k + 1} YES", file=f)


# 정답 해설 1
# 코딩 인텨뷰 혹은 손코딩 시에는 이런 식으로 정석으로 풀기
import sys

sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size // 2):
        if s[j] != s[-1 - j]:
            print(f"#{i + 1} NO")
            break
    else:
        print(f"#{i + 1} YES")


# 정답 해설 2 (pythonic)
# 온라인 코딩테스트 때는 이 방식으로 빠르게 풀기
import sys

sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")


# Test Case.
# < input >
# 5
# level
# moon
# abcba
# soon
# gooG

# < output >
# #1 YES
# #2 NO
# #3 YES
# #4 NO
# #5 YES
