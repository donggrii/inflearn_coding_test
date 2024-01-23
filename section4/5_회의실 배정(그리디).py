# 내 풀이 (성공)
# 정리 : https://ddonggrii.tistory.com/2
import sys

sys.stdin = open("input.txt", "r")

# 총 회의 수 입력받기
num_of_meetings = int(input())

# 주어진 회의 개수만큼 각각 (시작 시간, 종료 시간)으로 입력받아 저장
# 원본 데이터가 추후에 변경되지 않도록 튜플로 저장
meetings = [tuple(map(int, input().split())) for _ in range(num_of_meetings)]

# (★) 회의 종료 시간을 기준으로 오름차순 정렬
meetings.sort(key=lambda x: x[1])
# (★) 회의 종료 시간을 기준으로 오름차순 정렬하고, 같은 종료 시간에 대해서는 시작 시간이 빠른 순서로 정렬
# meetings.sort(key=lambda x: (x[1], x[0]))

# 가장 이른 시간에 종료되는 0번째 index의 회의를 예약하고, 그 종료 시간을 변수에 저장
last_time = meetings[0][1]  # 마지막으로 예약된 회의의 종료 시간을 저장할 변수
count = 1  # 예약된 회의의 수를 저장할 변수

# 0번째 index의 회의를 예약했으므로, 1번째 index부터 반복문 시작
for idx in range(1, num_of_meetings):  # 각 회의에 대해 index로 접근하여 순서대로 확인
    start, end = meetings[idx]
    # 해당 회의의 시작 시간이 마지막으로 예약된 회의의 종료 시간과 같거나 늦다면
    if start >= last_time:
        # 해댱 회의를 예약하고, 마지막으로 예약된 회의의 종료 시간을 갱신
        last_time = end
        count += 1

print(count)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
meeting = []
for _ in range(n):
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
