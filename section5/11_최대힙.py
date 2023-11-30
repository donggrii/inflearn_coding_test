# 내 풀이 (정답)
import sys
import heapq


sys.stdin = open("input.txt", "r")
heap = []
while True:
    a = int(input())
    if a == -1:
        break
    elif a == 0:
        with open("output11.txt", "a") as f:
            print(-1 if len(heap) == 0 else -heapq.heappop(heap), file=f)
    else:
        heapq.heappush(heap, -a)


# 정답 해설
import sys
import heapq as hq


sys.stdin = open("input.txt", "r")
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)


# Test Case.
# < input >
# 5
# 3
# 6
# 0
# 5
# 0
# 2
# 4
# 0
# -1

# < output >
# 6
# 5
# 5
