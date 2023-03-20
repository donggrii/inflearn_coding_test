# 내 풀이 (성공!)
# 최대 부분 증가 수열과 동일한 코드
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
d = [0] * (n + 1)
d[1] = 1
for i in range(2, n + 1):
    max_ = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and max_ < d[j]:
            max_ = d[j]
    d[i] = max_ + 1

print(max(d))


# Test Case.
# < input >
# 10
# 4 1 2 3 9 7 5 6 10 8

# output : 6
