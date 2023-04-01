# 내 풀이 (정답)
import sys

sys.stdin = open("input.txt", "r")
s = input().strip()
digit = int("".join([x for x in s if x.isdigit()]))  # 숫자만 추출하고, 그 순서대로 자연수 만들기
res = set()

for i in range(1, int(digit**0.5) + 1):  # 약수 구하기
    if digit % i == 0:
        res.update([i, digit // i])

with open("output2.txt", "a") as f:
    print(digit, file=f)
    print(len(res), file=f)


# 정답 해설
# isdecimal() : 0 ~ 9까지의 숫자만 찾아주는 것
# isdigit() : 알파벳이 아닌 숫자 형태는 모두 찾아줌 (ex. 2 ^ 31 같은 수도 찾아줌)
import sys

sys.stdin = open("input.txt", "r")
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)

# cnt = sum(res % i == 0 for i in range(1, res + 1))
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1

print(res)
print(cnt)


# Test Case 1.
# input : t0e0a1c2h0er

# < output >
# 120
# 16 -> (1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120) 10.xx


# Test Case 2.
# input : g0en2Ts8eSoft

# < output >
# 28
# 6 -> (1, 2, 4, 7, 14, 28) 5.xx
