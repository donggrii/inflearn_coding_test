# 내 풀이 (실패)
import sys

sys.stdin = open("input.txt", "r")
n = int(input())  # 총 회의 수
meetings = [list(map(int, input().split())) for _ in range(n)]  # (start, end)
meetings = sorted(meetings, key=lambda x: x[1])  # 회의 종료 시간 기준으로 정렬

cnt = 1
end_time = meetings[0][1]
for idx in range(1, n):
    start, end = meetings[idx]
    if start >= end_time:
        cnt += 1
        end_time = end

with open("output5.txt", "a") as f:
    print(cnt, file=f)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0
for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)


# Test Case.
# < input >
# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7

# < output >
# 3
