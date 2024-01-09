# 내 풀이 (수정) (실패 : 2 ~ 5번 TC 시간초과 or 오답)
# 전체 집합 중 조건에 맞는 부분 집합 만들기 => DFS 적용
# 회고 : 각 문제를 선택할 지 말 지 하나씩(level) 선택하면 되기 때문에, for문을 사용할 필요가 없음
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, total_score, total_time, judged_score):
    """
    Args:
        level (int): 문제 번호
        total_score (int): 문제를 풀었다면 얻는 점수
        total_time (int): 문제 푸는 데 할애한 시간
        judged_score (int): 부분 집합에 포함할 지 판단 여부가 끝난 총 점수
    """
    global max_score
    if total_time > m:
        return
    if (sum_total_score - judged_score) + total_score < max_score:
        return
    if level == n:
        max_score = max(max_score, total_score)
    else:
        # for score, time in probs:
        #     DFS(level + 1, total_score + score, total_time + time, judged_score + score)
        #     DFS(level + 1, total_score, total_time, judged_score + score)
        DFS(
            level + 1,
            total_score + probs[level][0],
            total_time + probs[level][1],
            judged_score + probs[level][0],
        )
        DFS(level + 1, total_score, total_time, judged_score + probs[level][0])


if __name__ == "__main__":
    n, m = map(int, input().split())
    probs = sorted([tuple(map(int, input().split())) for _ in range(n)], reverse=True)
    sum_total_score = sum(score for score, _ in probs)
    max_score = 0
    DFS(0, 0, 0, 0)
    print(max_score)


# 정답 해설
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_, time):
    global result
    if time > m:  # 가지치기
        return
    if level == n:  # 부분집합 하나가 완성됐을 때
        if sum_ > result:
            result = sum_
    else:
        DFS(level + 1, sum_ + prob_value[level], time + prob_time[level])
        DFS(level + 1, sum_, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    prob_value = []
    prob_time = []
    for _ in range(n):
        score, time = map(int, input().split())
        prob_value.append(score)
        prob_time.append(time)
    result = -2147000000
    DFS(0, 0, 0)
    print(result)


# 다른 풀이 (조합 푸는 방식)
import sys

sys.stdin = open("input.txt", "r")


def DFS(start, total, time):
    global grade
    if time > m:
        return
    if total > grade:
        grade = total
    for i in range(start, n):
        DFS(i + 1, total + ques[i][0], time + ques[i][1])


n, m = map(int, input().split())
ques = []
for _ in range(n):
    a, b = map(int, input().split())
    ques.append((a, b))
grade = 0
DFS(0, 0, 0)
print(grade)


# Test Case.
# < input >
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

# < output >
# 41
