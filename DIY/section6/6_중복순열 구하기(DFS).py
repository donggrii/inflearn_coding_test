# # 내 풀이 (실패)
# def dfs(L):
#     if sum(total) > m:
#         for i in range(1, len(total) + 1):
#             print(total[i] * i)
#     else:
#
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     total = [0] * (n + 1)  # [0, 0, 0, 0]
#     dfs(1)


# 답안 예시
# < N개의 수를 M번 중복해서 뽑으려면 상태 트리를 어떻게 뻗어나가야할까? >
# => DFS(0)에서 시작해서 N개의 가지를 뻗어나가면 됨!

# < DFS(0) 함수가 할 일 >
# 1. M 크기 만큼의 result[L] = i를 넣어줌
# 2. D(L + 1) 호출
# 3. 종료 지점 : (L == m)일 때 result 출력
import sys


input = sys.stdin.readline  # 대량의 데이터를 받을 때 빠르게 받아올 수 있음!
# s = input().rstrip()  # "문자열"을 input으로 받을 땐, 반드시 rstrip()으로 개행문자 제거해줘야 함!!


def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0  # 마지막에 총 경우의 수를 출력해야 하므로
    DFS(0)
    print(cnt)

