# 내 풀이 (설명 듣고 풀어보기 -> 성공!)
n = int(input())
arr = list(map(int, input().split()))
d = [0] * n
d[0] = 1
for i in range(1, n):
    val = 0
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and d[j] > val:
            val = d[j]
    d[i] = val + 1

print(max(d))

# 답안 예시
# 순서는 그대로 유지하면서 증가 수열을 뽑는 것
# 막무가내로 모든 증가 수열을 구하는 게 아닌, "기준"을 잡고 해야 함!
# 0번째 값부터 "이 항이 증가 수열의 마지막 항이라면" 가능한 수열의 개수 중 가장 긴 "길이 값"을 저장
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)  # 1번 index부터 이용하기 위해서
dy = [0] * (n + 1)
dy[1] = 1
res = 0  # 최대 길이 답을 저장할 것
for i in range(2, n + 1):
    max_ = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max_:
            max_ = dy[j]
    dy[i] = max_ + 1
    if dy[i] > res:  # dy 테이블 전체의 최댓값 누적하며 찾기
        res = dy[i]
print(res)
# print(dy)  # [0, 1, 2, 2, 3, 3, 2, 4, 5, 2]

# Test Case 1.
# < input >
# 9
# 2 7 5 8 6 4 7 12 3

# output : 5 (2 5 6 7 12)

# Test Case 2.
# < input >
# 8
# 5 3 7 8 6 2 9 4

# output : 4
