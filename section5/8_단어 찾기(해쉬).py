# 내 풀이 (정답)
# 구해야 하는 것 : 시에 쓰지 않은 한 개의 단어를 출력

# (cf) N개의 단어 중 중복된 단어가 있을 수도 있음 (ex) 2번 나온 "sky"는 2번 나와야 함
#      ⇒ set()이 아닌 dict()를 사용
import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
n = int(input())
note = defaultdict(int)

for _ in range(n):
    note[input()] += 1

for _ in range(n - 1):
    note[input()] -= 1

note = sorted(note.items(), key=lambda x: x[1], reverse=True)
result = note[0][0]

with open("output8.txt", "a") as f:
    print(result, file=f)


# 정답 해설
# (cf) 해설에서는 중복된 단어가 없다는 가정을 하고, 1과 0으로만 판단
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break


# Test Case.
# < input >
# 5
# big
# good
# sky
# blue
# mouse
# sky
# good
# mouse
# big

# < output >
# blue
