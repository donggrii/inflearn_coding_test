# # 내 풀이 1 (일부 성공, 일부 실패)
# # Cut Edge 더 할 수 있는 방법을 모르겠음..
# def dfs(L, sum_, time):
#     global answer
#     if answer < sum_:
#         answer = sum_
#     if L == n:
#         return
#     else:
#         for i in range(n):
#             if ch[i] == 0 and time - q[i][1] >= 0:
#                 ch[i] = 1
#                 dfs(L + 1, sum_ + q[i][0], time - q[i][1])
#                 ch[i] = 0
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     q = [list(map(int, input().split())) for _ in range(n)]
#     answer = 0
#     ch = [0] * n
#     dfs(0, 0, m)
#     print(answer)


# 내 풀이 2 (5가닥이 아니라 2가닥씩 뻗으면 된다는 설명 듣고 다시 풀어보기 -> 성공!)
# (참고) DFS 문제 같으면,
# 1. 2가닥으로 해결할 수 있는지 보고,
# 2. 안될 것 같으면 여러 가닥으로 뻗는 것 생각하기
def dfs(L, sum_, time):
    global answer
    if time > m:
        return
    if L == n:
        if answer < sum_:
            answer = sum_
    else:
        dfs(L + 1, sum_ + q[L][0], time + q[L][1])
        dfs(L + 1, sum_, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    q = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    dfs(0, 0, 0)
    print(answer)


# 답안 예시
# 각각 문제를 풀 건지, 안 풀 건지 결정하는 문제 => 부분집합 만들기! (2가닥씩 뻗으면 됨)
def DFS(L, sum, time):
    """
    :param L: 문제 번호
    :param sum: 문제를 풀었다면 얻는 점수
    :param time: 문제 푸는 데 할애한 시간
    :return:
    """
    global res
    if time > m:  # 가지치기
        return
    if L == n:  # 문제를 다 적용해서 부분집합 하나가 완성됐을 때
        if sum > res:
            res = sum
    else:
        DFS(L + 1, sum + pv[L], time + pt[L])
        DFS(L + 1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()  # problem value
    pt = list()  # problem time
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)


# Test Case.
# < input >
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

# output : 41
