# 내 풀이 1 (정답)
# 이 문제에선 Time Limit 걸리지 않았지만, 다른 문제에선 NlogN으로 시간 초과될 수도 있음
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

result = n_lst + m_lst
result.sort()

with open("output4.txt", "a") as f:
    for x in result:
        print(x, end=" ", file=f)


# 내 풀이 2 (정답)
# "투포인터" 이용하는 강의 설명만 듣고 시간복잡도 `N`으로 다시 풀어본 풀이
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
res = [0] * (n + m)
p, p1, p2 = 0, 0, 0

while p1 < n and p2 < m:
    if n_lst[p1] <= m_lst[p2]:
        res[p] = n_lst[p1]
        p1 += 1
    else:
        res[p] = m_lst[p2]
        p2 += 1
    p += 1
    # 둘 중 하나의 리스트라도 끝났다면, 나머지 다른 리스트 값들을 한꺼번에 결과 리스트에 넣어주기
    if p1 == n:
        res[p:] = m_lst[p2:]
        break
    elif p2 == m:
        res[p:] = n_lst[p1:]
        break

with open("output4.txt", "a") as f:
    for x in res:
        print(x, end=" ", file=f)


# 정답 해설 (중요!)
# 회고 : 내가 첫번째 푼 것처럼 단순히 두 리스트를 더해서 .sort() 하라는 문제가 아님
#        파이썬 내장함수 .sort()의 시간복잡도 : `NlogN` (퀵 정렬)
# 문제 의도 : 정렬이 이미 되어 있는 두 리스트를 합치는 건 "투포인터"를 이용해 시간복잡도 `N` 으로 끝낼 수 있음
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# 어떤 포인터가 끝까지 갔는지 확인
if p1 < n:
    c += a[p1:]
if p2 < m:
    c += b[p2:]

for x in c:
    print(x, end=" ")


# Test Case.
# < input >
# 3
# 1 3 5
# 5
# 2 3 6 7 9

# output : 1 2 3 3 5 6 7 9
