# 내 풀이 (80% 정답, 5번 Test Case 시간 초과)
# (참고) "최댓값"을 구할 때는 정렬한 것과 안 한 것에 큰 차이가 없음
# => 7. 동전 교환 문제에서 "최소 개수"를 구할 때는 정렬하는 게 매우 중요!
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global max_weight
    if sum_ > c:  # Cut Edge, 가지치기 (시간 복잡도 개선)
        return
    if level == n:
        if sum_ > max_weight:
            max_weight = sum_
    else:
        DFS(level + 1, sum_ + weights[level])
        DFS(level + 1, sum_)


if __name__ == "__main__":
    c, n = map(int, input().split())
    weights = [int(input()) for _ in range(n)]
    max_weight = 0
    DFS(0, 0)
    print(max_weight)


# 정답 해설
# 문제 풀이는 "부분 집합 만들기"와 동일
# [내 풀이]에 추가로 Cut Edge를 더 해야 함
# -> 바둑이 전체 무게(total) - 레벨별로 판단을 이미 끝낸 무게의 합(total_sum) : 앞으로 판단해야 할 무게의 전체 합
# -> (sum_ + (total - total_sum)) : (현재 레벨까지 부분 집합에 포함한 무게 합 + 앞으로 판단해야 할 무게의 전체 합)
# -> 이 값이 result(현재까지 가능한 최대 무게)보다 작다면 Cut Edge
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_, total_sum):
    global result
    if sum_ + (total - total_sum) < result:
        return
    if sum_ > c:
        return
    if level == n:  # 부분 집합 하나가 완성됐을 경우
        if sum_ > result:
            result = sum_
    else:
        DFS(level + 1, sum_ + a[level], total_sum + a[level])
        DFS(level + 1, sum_, total_sum + a[level])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    result = -2147000000  # 최종적인 답(최대 무게)을 저장
    total = sum(a)
    DFS(0, 0, 0)
    print(result)


# Test Case.
# < input >
# 259 5
# 81
# 58
# 42
# 33
# 61

# < output >
# 242
