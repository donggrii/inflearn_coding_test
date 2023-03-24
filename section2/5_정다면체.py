# 내 풀이 (정답)
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
total_sum = [i + j for i in range(1, n + 1) for j in range(1, m + 1)]
# total_sum = [i + j for i, j in itertools.product(range(1, n + 1), range(1, m + 1))]

# 주사위 눈의 합 : 빈도 수
counter = Counter(total_sum)
counter_items = counter.items()
max_freq_num = max(counter.values())
result = sorted([num for num, freq in counter_items if freq == max_freq_num])

with open("output5.txt", "a") as f:
    for r in result:
        print(r, end=" ", file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
cnt = [0] * (n + m + 3)  # cnt의 index는 주사위 두 눈의 합, value는 빈도 수를 저장 ("+3"은 여유 공간)

# 가능한 주사위 눈 조합의 빈도 수 구하기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

# 최대 빈도수 찾기
max_ = -2147000000
for i in range(n + m + 1):
    if cnt[i] > max_:
        max_ = cnt[i]

# 최대 빈도수를 갖는 index 찾기
for i in range(n + m + 1):
    if cnt[i] == max_:
        print(i, end=" ")  # 옆으로 이어붙여서 출력

# Test Case.
# input : 4 6
# output : 5 6 7
