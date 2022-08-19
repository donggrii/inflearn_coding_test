# # 내 풀이
# def solution(x):
#     from itertools import combinations
#     for i in range(1, x + 1):
#         print(list(combinations(range(1, x + 1), i)))
#
#
# def dfs(x, stack):
#     """후위 순회"""
#     if x == (n + 1):
#         return
#     else:
#         for i in range(1, len(stack)):
#             stack[i] = 1
#             dfs(i + 1, stack)
#             print(stack)
#
#
# if __name__ == "__main__":
#     n = int(input())
#     # solution(n)
#     s = [0] * (n + 1)
#     dfs(1, s)


# 답안 예시
def DFS(v):
    if v == (n + 1):  # 종착점(종료) 설정
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=" ")
        print()
    else:
        check[v] = 1  # 1로 체크되면 해당 원소를 부분 집합에 사용
        DFS(v + 1)
        check[v] = 0  # 해당 원소를 사용하지 않도록 다시 0으로 변경
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n + 1)  # 원소를 사용한다 or 안 한다 -> 신호를 줄 수 있는 체크 변수가 필요!
    DFS(1)
