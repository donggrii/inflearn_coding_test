# [1. Bottom-Up : 동적 계획법 (Dynamic Programming)]
# < 아이디어 >
# (ex) 4m 네트워크 선을 자른다면,
#      1. 자를 때, 맨 마지막 토막이 1m인 경우, 앞에 남은 건 3m짜리 선이고, 이 경우는 d[3]에 구해져 있음
#      2. 자를 때, 맨 마지막 토막이 2m인 경우, 앞에 남은 건 2m짜리 선이고, 이 경우는 d[2]에 구해져 있음
# => 점화식 : f(n) = f(n - 1) + f(n - 2)

# 내 풀이
n = int(input())  # 7
d = [0] * 46
d[1] = 1
d[2] = 2
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])


# 답안 예시
n = int(input())  # 7
dy = [0] * (n + 1)
dy[1] = 1
dy[2] = 2
for i in range(3, n + 1):
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n])


# [2. Top-Down : 재귀, 메모이제이션] -> 넓은 의미에서의 동적 계획법 (Dynamic Programming)
# DFS 전위순회 상태 트리로 해결 가능
# 메모이제이션 : 재귀를 돌릴 때, 이미 1번 구해진 값은 기록해서 다음 호출됐을 때 가지를 뻗지 않고 Cut Edge 하는 기법
#                => 불필요한 재귀 호출을 방지

# 답안 예시
def DFS(len):
    if dy[len] > 0:  # Cut Edge
        return dy[len]
    if len == 1 or len == 2:  # 종료 조건
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)  # 메모이제이션 (기록)
        return dy[len]


if __name__ == "__main__":
    n = int(input())  # 7
    dy = [0] * (n + 1)
    print(DFS(n))
