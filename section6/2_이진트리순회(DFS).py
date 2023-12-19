# '부모 노드' 수행 위치에 따라 이름이 달라짐
# 1. 전위순회 (일반적인 DFS) : 부모 - 왼쪽 자식 - 오른쪽 자식
#    -> 자식 노드를 재귀 호출하기 전, 자기 본연의 일을 먼저 수행하고 재귀 호출
# 2. 중위순회 (거의 안 쓰임) : 왼쪽 자식 - 부모 - 오른쪽 자식
# 3. 후위순회 (약간 쓰임) : 왼쪽 자식 - 오른쪽 자식 - 부모
#    -> 대표적으로 "병합 정렬"에 사용됨
# (cf) 부모 노드 값(x), 왼쪽 자식 노드 값(2 * x), 오른쪽 자식 노드 값(2 * x + 1)
def dfs_front(v):
    """전위 순회"""
    if v > 7:
        return
    else:
        print(v, end=" ")  # 함수 본연의 일(방문)을 먼저 처리
        dfs_front(v * 2)
        dfs_front(v * 2 + 1)


def dfs_mid(v):
    """중위 순회"""
    if v > 7:
        return
    else:
        dfs_mid(v * 2)
        print(v, end=" ")  # 왼쪽 자식의 일이 모두 처리되고 부모가 중간에서 처리됨
        dfs_mid(v * 2 + 1)


def dfs_back(v):
    """후위 순회"""
    if v > 7:
        return
    else:
        dfs_back(v * 2)
        dfs_back(v * 2 + 1)
        print(v, end=" ")  # 왼쪽 자식과 오른쪽 자식의 일을 모두 처리한 뒤, 부모 함수 본연의 일을 수행


if __name__ == "__main__":
    dfs_front(1)  # 전위 순회(DFS) : 1 2 4 5 3 6 7
    print()
    dfs_mid(1)  # 중위 순회 : 4 2 5 1 6 3 7
    print()
    dfs_back(1)  # 후위 순회 : 4 5 2 6 7 3 1
