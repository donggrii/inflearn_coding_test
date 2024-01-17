# 내 풀이 (성공)
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global result
    if level == k:
        if 1 <= sum_ <= total_weights:
            result.add(sum_)
    else:
        DFS(level + 1, sum_ + weights[level])
        DFS(level + 1, sum_ - weights[level])
        DFS(level + 1, sum_)


if __name__ == "__main__":
    k = int(input())
    weights = list(map(int, input().split()))
    total_weights = sum(weights)
    result = set()
    DFS(0, 0)
    cnt = 0
    for i in range(1, total_weights + 1):
        if i not in result:
            cnt += 1
    print(cnt)


# 정답 해설
# 포인트 1 : '추의 사용 여부'로 상태트리를 만들 때, 왼쪽(+)/오른쪽(-)/사용 X(0) 세 가닥으로 뻗어나가기
# 포인트 2 : 음수의 경우는 대칭적으로 반드시 양수의 경우가 존재하기 때문에, 양수일 때만 고려해줘도 됨
#            (ex) (왼) 1, 5, 그릇 | (오) 7 : -1
#                 (왼) 7 | (오) 1, 5, 그릇 : 1
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, sum_):
    global result
    if level == k:
        if 0 < sum_ <= total_weights:
            result.add(sum_)
    else:
        DFS(level + 1, sum_ + weights[level])  # 추를 왼쪽에 둔 경우 (빈 그릇을 오른쪽에 둔 경우)
        DFS(level + 1, sum_ - weights[level])  # 추를 오른쪽에 둔 경우 (빈 그릇을 왼쪽에 둔 경우)
        DFS(level + 1, sum_)  # 추를 사용하지 않는 경우


if __name__ == "__main__":
    k = int(input())
    weights = list(map(int, input().split()))
    total_weights = sum(weights)
    result = set()
    DFS(0, 0)
    print(total_weights - len(result))


# Test Case.
# < input >
# 3
# 1 5 7

# < output >
# 2
