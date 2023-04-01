# 내 풀이 (정답) (45분 소요)
# 1. 각 학생 점수에서 평균 점수를 빼고 절대값 씌우기
# 2. |점수-평균| 가장 낮은 index만 추출해서, 그 index에 해당하는 실제 점수만 추출
# 3. 추출한 점수 모두 같을 때 -> 빠른 학생 번호 출력
# 4. 추출한 점수 다를 때
#   4-1. 높은 점수만 남겨서 빠른 학생 번호 출력
import sys

sys.stdin = open("input.txt", "r")

n = int(input())
scores = list(map(int, input().split()))
mean_score = int((sum(scores) / n) + 0.5)  # mean_score = int(round((sum(scores) / n), 0)) -> (X)

lst = list(map(lambda x: abs(x - mean_score), scores))  # |점수-평균|
min_lst = min(lst)

zip_lst = list(zip(range(1, n + 1), scores, lst))  # 학생번호, 점수, |점수-평균|
index_lst = [index for index in range(n) if min_lst == zip_lst[index][2]]  # |점수-평균|가 가장 낮은 index
score_lst = [zip_lst[index][1] for index in index_lst]  # |점수-평균|가 가장 낮은 index에 해당하는 실제 점수

with open("output4.txt", "a") as f:
    if len(set(score_lst)) == 1:
        print(mean_score, index_lst[0] + 1, file=f)
    else:
        max_score_lst = max(score_lst)
        result = [i for i, s in enumerate(score_lst) if s == max_score_lst]
        print(mean_score, index_lst[result[0]] + 1, file=f)


# 정답 해설
# 오류 수정 : python에서 round()는 round_half_even 방식이므로, 반올림 계산 시 사용하면 X
#   round_half_even 방식 : 소수점 첫번째 자리가 정확히 0.5인 경우 올림하는 것이 아니라 "짝수"쪽에 근사시킴
#   (ex) round(4.5) = 4, round(5.5) = 6, round(4.51) = 5
#   따라서 round(a) 대신, int(a + 0.5) 사용할 것!
import sys

sys.stdin = open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))

ave = int((sum(a) / n) + 0.5)  # ave = round(sum(a) / n) -> (X)

min_ = 2147000000  # int형으로 표현할 수 있는 (4byte = 2 ^ 31) 정도 되는 가장 큰 수

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min_:
        min_ = tmp
        score = x
        res = idx + 1
    elif tmp == min_:
        if x > score:  # (중요) 문제에서 더 늦은 학생 번호를 출력하라고 하면, 여기에 등호(=) 추가
            score = x
            res = idx + 1

print(ave, res)

# Test Case.
# < input >
# 10
# 45 73 66 87 92 67 75 79 75 80

# < output >
# 74 7
