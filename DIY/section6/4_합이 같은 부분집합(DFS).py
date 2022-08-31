# 내 풀이 (성공!)
# 1 <= N <= 10 이므로 최대 경우의 수는 2^10 = 1024가지
# N개의 원소를 각각 포함 or 포함하지 않을 때를 상태 트리로 나눠 2개의 서로소 집합을 만들고 합을 비교하는 DFS로 풀이
def dfs(v):
    if v == n:
        left = [total[i] for i in range(v) if check[i] == 1]
        right = [total[i] for i in range(v) if check[i] == 0]
        if sum(left) == sum(right):
            return "YES"
    else:
        check[v] = 1
        if dfs(v + 1) == "YES":
            return "YES"
        check[v] = 0
        if dfs(v + 1) == "YES":
            return "YES"


if __name__ == "__main__":
    n = int(input())
    total = list(map(int, input().split()))
    check = [0] * n
    if dfs(0) == "YES":
        print("YES")
    else:
        print("NO")


# 답안 예시
# 총 (2^N - 1)가지의 경우(공집합 제외)를 다 만들면서 내가 만든 부분 집합의 합을 sum_ 변수로 누적시킴
# 내가 만든 부분 집합에 포함되지 않는 원소들의 합은 전체 집합의 합에서 sum_ 변수를 뺀 값이 될 것
# 따라서, 전체 집합의 합을 total 변수에 담고, 내가 만든 부분 집합의 합(sum_)이 (total - sum_)과 같으면 됨!
# => 여기서 sum_ == (total // 2) 로 하면 안 되는 이유 : total이 홀수일 경우 "NO"가 나와야 하는데 "YES"가 나올 수도 있음
import sys


def DFS(L, sum_):
    """
    L (Level) : a의 index
    sum_ : 내가 만든 부분 집합의 원소 값들을 누적합 시킨 변수
    """
    if sum_ > total // 2:  # 시간 복잡도 개선
        return
    if L == n:  # L이 (마지막 index + 1)인 n에 도달했을 때 종료
        if sum_ == (total - sum_):
            print("YES")
            sys.exit(0)  # 프로그램을 아예 종료시킴
    else:
        DFS(L + 1, sum_ + a[L])  # 왼쪽 노드 (a의 L번째 index에 있는 값 사용 O)
        DFS(L + 1, sum_)  # 오른쪽 노드 (a의 L번째 index에 있는 값 사용 X)


if __name__ == "__main__":
    n = int(input())  # 6
    a = list(map(int, input().split()))  # 1 3 5 6 7 10
    total = sum(a)
    DFS(0, 0)
    print("NO")
