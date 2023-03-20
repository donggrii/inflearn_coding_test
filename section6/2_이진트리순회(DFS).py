# 1. 전위순회 (대부분 일반적인 DFS) : 부모 - 왼쪽 자식 - 오른쪽 자식
#    -> 자식 노드를 재귀 호출하기 전, 자기 본연의 일을 먼저 수행하고 재귀 호출 (ex. print)
# 2. 중위순회 (거의 X) : 왼쪽 자식 - 부모 - 오른쪽 자식
# 3. 후위순회 (약간 쓰임) : 왼쪽 자식 - 오른쪽 자식 - 부모
#    -> 대표적인 게 "병합 정렬"
# (cf) 부모 노드 값(x), 왼쪽 자식 노드 값(2 * x), 오른쪽 자식 노드 값(2 * x + 1)
def dfs_front(v):
    """전위 순회"""
    if v > 7:
        return
    else:
        print(v, end=' ')  # 함수 본연의 일(방문)을 먼저 처리
        dfs_front(v * 2)
        dfs_front(v * 2 + 1)


def dfs_mid(v):
    """중위 순회"""
    if v > 7:
        return
    else:
        dfs_mid(v * 2)
        print(v, end=' ')  # 왼쪽 자식의 일이 모두 처리되고 부모가 중간에서 처리됨
        dfs_mid(v * 2 + 1)


def dfs_back(v):
    """후위 순회"""
    if v > 7:
        return
    else:
        dfs_back(v * 2)
        dfs_back(v * 2 + 1)
        print(v, end=' ')  # 부모 함수 본연의 일이 왼쪽 자식과 오른쪽 자식의 일을 모두 처리한 뒤 수행됨


if __name__ == "__main__":
    dfs_front(1)
    print()
    dfs_mid(1)
    print()
    dfs_back(1)
