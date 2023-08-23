# 내 풀이 1 (정답)
# 아이디어 : 역수열을 뒤집어서, 가장 큰 수에 해당하는 값부터 거꾸로 보면, 원래 수열에서 그 숫자값의 위치를 알 수 있음
#            => 큰 숫자 순서대로 역수열을 보면, 현재 숫자가 앞에 있는지 뒤에 있는지 알 수 있기 때문
#            => insert()로 삽입해주기
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
lst = list(map(int, input().split()))  # 역수열(원래 수열 내에서 현재 숫자값보다 앞에 위치하는 큰 숫자의 개수)
rev_lst = sorted(enumerate(lst, start=1), reverse=True)  # (숫자값, 역수열 값) : 숫자값 기준 내림차순 정렬 [(8, 0), (7, 1), ..., (1, 5)]

result = []
for num, rev_cnt in rev_lst:
    result.insert(rev_cnt, num)  # result.insert(0, 8), result.insert(1, 7), ..., result.insert(5, 1)

with open("output10.txt", "a") as f:
    for x in result:
        print(x, file=f, end=" ")


# 내 풀이 2 (정답) : 강의에서 풀이 방향에 대한 설명만 듣고 직접 구현해보기
# 결과 리스트 길이만큼 0으로 초기화하여 생성한 seq에, 앞에 위치한 0의 개수를 세서 직접 최종적인 위치에 숫자값 채워넣기
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
lst = list(map(int, input().split()))

seq = [0] * n
for x, target in enumerate(lst, start=1):  # (1부터 N까지 오름차순 정렬된 값, 역수열 값) [(1, 5), (2, 3), ..., (8, 0)]
    cnt = 0
    for i in range(n):
        if seq[i] == 0:
            if cnt == target:
                seq[i] = x
                break
            else:
                cnt += 1

with open("output10.txt", "a") as f:
    for x in seq:
        print(x, file=f, end=" ")


# 정답 해설
# 1부터 N까지 "오름차순 정렬"된 상태로 원래 수열에 값을 넣는 거라는 걸 명심할 것!
# 즉, 정렬된 상태이므로 뒤에 나올 값은 나보다 무조건 큰 값 => 자리를 비워놔야 함!
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))  # 역수열
a.insert(0, 0)  # 1부터 N까지 indexing하기 위해
seq = [0] * n  # 원래 수열
for i in range(1, n + 1):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:  # 자기 자리 찾아 들어가는 경우
            seq[j] = i
            break
        elif seq[j] == 0:  # 아직 자기 자리 찾지 못한 경우
            a[i] -= 1

for x in seq:
    print(x, end=" ")


# Test Case.
# < input >
# 8
# 5 3 4 0 2 1 1 0

# < output >
# 4 8 6 2 5 1 3 7
