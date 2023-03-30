# 내 풀이 (오답)
# 회고 : 소수 prime에 다 구해놨는데, x가 2 이상일 경우만으로 제한두지 않았음
#        "x가 1일 경우도 출력한 경우"만 오답이었음
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
total = list(map(int, input().split()))
thres = 100000
prime = [1] * (thres + 1)
prime[0], prime[1] = 0, 0

# prime에 에라토스테네스 체 적용
for i in range(2, int(thres**0.5) + 1):
    if prime[i] == 1:
        k = 2
        while i * k <= thres:
            prime[i * k] = 0
            k += 1


def reverse(x):
    x = reversed(str(x))
    x = int("".join(x))
    return x


def isPrime(x):
    return prime[x] == 1


with open("output8.txt", "a") as f:
    for x in total:
        x = reverse(x)
        if isPrime(x):
            print(x, end=" ", file=f)


# 정답 해설
# reverse() 함수가 핵심!!
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x //= 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True


for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")


# Test Case.
# < input >
# 5
# 32 55 62 3700 250

# < output >
# 23 73
