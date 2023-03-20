# # 내 풀이 (추가 Cut Edge 적용 못해서 일부 시간 초과됨)
# def dfs(L, sum_):
#     global max_weight
#     if sum_ > c:
#         return
#     if L == n:
#         if max_weight < sum_:
#             max_weight = sum_
#     else:
#         dfs(L + 1, sum_ + weight[L])
#         dfs(L + 1, sum_)
#
#
# if __name__ == "__main__":
#     c, n = map(int, input().split())
#     weight = sorted([float(input()) for _ in range(n)], reverse=True)
#     max_weight = -1
#     dfs(0, 0)
#     print(max_weight)


# 내 풀이 (강의 듣고 정렬한 것과 안 한 것의 차이를 보기 위해 수정)
# => 결론 : 최댓값을 구할 때는 정렬한 것과 안한 것에 큰 차이가 없음
# (cf) 7. 동전 교환 문제에서 최소 개수를 구할 때는 정렬하는 게 매우 중요!
def dfs(L, sum_, tsum):
    global max_weight
    if sum_ + (total - tsum) < max_weight:
        return
    if sum_ > c:
        return
    if L == n:
        if max_weight < sum_:
            max_weight = sum_
    else:
        dfs(L + 1, sum_ + weight[L], tsum + weight[L])
        dfs(L + 1, sum_, tsum + weight[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    weight = sorted([int(input()) for _ in range(n)], reverse=True)
    max_weight = -1
    total = sum(weight)
    dfs(0, 0, 0)
    print(max_weight)


# 답안 예시
# < 시간복잡도를 더 줄일 수 있지 않을까? = Cut Edge (가지치기; 백트래킹) 하는 방법이 뭘까? >
# 1. 처음 바둑이 몸무게를 입력받았을 때, 전체 몸무게의 합 total을 구하기
# 2. 상태 트리에서 포함 O or 포함 X 을 판단할 때, 누적합 total_sum을 구해놓기
# 3. total - total_sum
#    = 해당 Level까지의 모든 바둑이 몸무게의 총합을 전체 합에서 뺀 값
#    = 앞으로 적용할 지 판단할 바둑이들의 몸무게의 총합
# 4. 부분 집합에 포함시켜 누적합 해나가는 (sum_) + 남은 바둑이들의 총 무게 (total - total_sum)
#    = 부분 집합에 포함된 바둑이 + 남은 바둑이 무게 다 더한 것
# 5. sum_ + (total - total_sum) < result 인 경우 Cut Edge
def DFS(L, sum_, tsum):
    """
    :param L: (Level) a의 index
    :param sum_: 내가 만든 부분 집합의 원소 값들을 누적합 시킨 변수
    :param tsum: 해당 Level까지 적용을 이미 판단한 값들을 누적합 시킨 변수
    :return:
    """
    global result
    if sum_ + (total - tsum) < result:
        return
    if sum_ > c:
        return
    if L == n:  # 부분 집합 하나가 완성됐을 경우
        if sum_ > result:
            result = sum_
    else:
        DFS(L + 1, sum_ + a[L], tsum + a[L])
        DFS(L + 1, sum_, tsum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    result = -1  # 최종적인 답(최대 무게)을 저장
    total = sum(a)
    DFS(0, 0, 0)
    print(result)
