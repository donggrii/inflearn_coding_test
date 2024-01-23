# # 내 풀이 (실패, RecursionError(무한 루프))
# # [회고]
# # - 상태트리가 2갈래(한 자리 수의 경우, 두 자리 수의 경우)로 뻗어나가는 방식 (두 자리 수가 1 ~ 26 범위의 수인지 확인)
# # - 하지만 이 방식으로 했을 때, 0이 입력된 경우 종료 처리를 해결하지 못했음
# # - 또한, `code[level : level + 2]`와 같은 슬라이싱 방식은 인덱스가 넘어가도 에러가 나지 않기 때문에, level이 length를 넘어가도 계속 진행되어 RecursionError 발생
# import sys

# sys.stdin = open("input.txt", "r")


# def DFS(level, result):
#     global cnt
#     if level == length:
#         tmp = ""
#         for x in result:
#             tmp += book[x]
#         print(tmp)
#         cnt += 1
#     else:
#         if code[level : level + 1] == "0":
#             DFS(level + 1, result)
#         else:
#             DFS(level + 1, result + [code[level : level + 1]])
#             # if code[level + 1 : level + 2] == "0":
#             if 1 <= int(code[level : level + 2]) <= 26:
#                 DFS(level + 2, result + [code[level : level + 2]])


# if __name__ == "__main__":
#     code = input()
#     cnt = 0
#     length = len(code)
#     # book : {key: range(1, 27), value: chr(65) ~ chr(90)}
#     book = {str(i): chr(64 + i) for i in range(1, 27)}
#     DFS(0, [])
#     print(cnt)


# 정답 해설
# [정답 코드 해석]
# 1. 굳이 dictionary를 만들 필요 없이, chr() 함수에 아스키 코드 값을 넘겨서 바로 출력
# 2. 상태트리는 매번 26가지(1~26, A~Z)씩 뻗어나감
# 3. 26까지 뻗어나가는 동안 한 자리 수를 DFS로 다 처리하고 나면, 다시 돌아와서 두 자리 수를 판별하게 됨
# 4. 두 자리 수를 판별할 때, 10으로 나눈 몫과 나머지를 활용
# 4. position은 result 변수에 결과를 담을 때의 위치를 지정하는 것으로, 항상 +1로 진행됨
# 5. level은 문제에서 주어진 숫자 코드의 위치 값을 나타냄. 따라서 종료 조건은 (level == n)일 때임
# [문제에서 헷갈리는 표현 해석]
# 표현 : "첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길이는 최대 50이다) `0이 입력되면 입력종료를 의미한다.`"
# 해석 : 0이 있다고 가정해보자.
#        A가 1부터 시작하기 때문에 0은 한 자리 수 판별에도 해당되지 않고, 두 자리 수 판별에서도 10 ~ 26(i)를 10으로 나눈 몫이 1 또는 2이기 때문에 해당되지 않는다.
#        따라서 `level`의 위치가 가리키는 값이 0이 되는 경우는 그 밑의 상태트리가 뻗어나가지 못하고 끝나게 된다. (즉, DFS 진행이 되지 않는다.)
#        이 경우를 나타내는 말이 "0이 입력되면 입력종료를 의미한다"인 것이다.
# 예시 : code = "3102"라면, 결과는 CJB (3, 10, 2) 1개밖에 출력되지 않는다. CA (3, 1, ..) 가 되는 경우가 나타나면 자동으로 종료되어 그 이후는 진행되지 않는다.
import sys

sys.stdin = open("input.txt", "r")


def DFS(level, position):
    global cnt
    if level == n:
        cnt += 1
        for j in range(position):
            print(chr(result[j] + 64), end="")
        print()
    else:
        for i in range(1, 27):
            # 한 자리 수
            if code[level] == i:
                result[position] = i
                DFS(level + 1, position + 1)
            # 두 자리 수
            elif i >= 10 and code[level] == i // 10 and code[level + 1] == i % 10:
                result[position] = i
                DFS(level + 2, position + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    # 맨 끝에 -1을 넣는 이유 : IndexError(list index out of range)를 방지하기 위해!
    # (ex) 만약 이처럼 -1과 같은 값을 넣지 않았을 때, 마지막 값인 code[-1]이 0, 1, 2 중 하나라면 두 자리 수 판별 조건문 내의 `code[level + 1]`을 확인할 때 IndexError가 발생함
    # (cf) -1이 사용된다면 `code[level + 1] == i % 10` 부분의 `code[level + 1]`일텐데, 10 ~ 26(i)을 10으로 나눈 나머지 즉 0 ~ 9가 -1과 같을 수는 없으므로 참인 경우는 없음
    code.insert(n, -1)
    result = [0] * (n + 3)  # (n + 3)인 이유는 좀 더 여유 공간을 잡기 위해서. 그냥 n으로 잡아도 문제 없음
    cnt = 0
    DFS(0, 0)
    print(cnt)


# Test Case 1.
# < input >
# 25114

# < output >
# BEAAD
# BEAN
# BEKD
# YAAD
# YAN
# YKD
# 6

# Test Case 2.
# < input >
# 115213102

# < output >
# AAEBACJB
# AAEBMJB
# AAEUCJB
# AOBACJB
# AOBMJB
# AOUCJB
# KEBACJB
# KEBMJB
# KEUCJB
# 9
