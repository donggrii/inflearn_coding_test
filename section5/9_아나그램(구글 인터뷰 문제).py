# 내 풀이 (정답)
# 아나그램(Anagram) : 두 문자열이 알파벳의 나열 순서는 다르지만 구성이 일치하는 것
#                     즉, 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것
# 회고 : 실전 코테라면 [내 풀이]처럼 빠르게 푸는 게 중요하겠지만, 면접 코테라면 자료구조 활용해서 [정답 해설]처럼 풀어야 함
import sys

sys.stdin = open("input.txt", "r")
first = list(input())
second = list(input())

first.sort()  # ['A', 'A', 'C', 'a', 'b', 'e', 'e']
second.sort()  # ['A', 'A', 'C', 'a', 'b', 'e', 'e']
result = "YES" if first == second else "NO"

with open("output9.txt", "a") as f:
    print(result, file=f)


# 정답 해설 1 (딕셔너리 해쉬)
# 핵심 코드 : str1['A'] = str1.get('A', 0) + 1
import sys

sys.stdin = open("input.txt", "r")
a = input()
b = input()
str1 = dict()  # {'A': 2, 'b': 1, 'a': 1, 'e': 2, 'C': 1}
str2 = dict()  # {'A': 2, 'b': 1, 'a': 1, 'e': 2, 'C': 1}

for x in a:
    str1[x] = str1.get(x, 0) + 1

for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")


# 정답 해설 2 (딕셔너리 해쉬 개선)
import sys

sys.stdin = open("input.txt", "r")
a = input()
b = input()
sH = dict()

for x in a:
    sH[x] = sH.get(x, 0) + 1

for x in b:
    sH[x] = sH.get(x, 0) - 1

for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")


# 정답 해설 3 (리스트 해쉬 like C++)
# Ascii Number 이용 => ord(x) : Ascii Number 반환
import sys

sys.stdin = open("input.txt", "r")
a = input()
b = input()

# 알파벳 대문자 26개 (Ascii : 65 ~ 90), 소문자 26개 (Ascii : 97 ~ 122)
str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1  # A : 0번 index에 매핑
    else:
        str1[ord(x) - 71] += 1  # a : 26번 index에 매핑

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1  # A : 0번 index에 매핑
    else:
        str2[ord(x) - 71] += 1  # a : 26번 index에 매핑

for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")


# Test Case.
# < input >
# AbaAeCe
# baeeACA

# < output >
# YES
