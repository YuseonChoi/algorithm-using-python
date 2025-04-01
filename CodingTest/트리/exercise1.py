"""
[트리 순회]
이진 트리를 표현한 리스트 nodes를 인자로 받습니다.
해당 이진 트리에 대하여, 전위/중위/후위 순회 결과를 반환하세요.

여기서 루트 인덱스는 0.
고로, 왼쪽 자식 노드 배열 인덱스는 (부모 노드 * 2 + 1)
오른쪽 자식 노드 배열 인덱스는 (부모 노드 * 2 + 2)

N이 노드의 개수라고 했을 때,
전위/중위/후위 연산 모두 각 노드를 한 번씩 방문하므로
시간 복잡도는 O(N)
"""

## 전위 순회 (루트 -> 왼쪽 자식 -> 오른쪽 자식)
def preorder(nodes, idx):
    # idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        ret = str(nodes[idx])+" "
        ret += preorder(nodes, idx*2+1)  # 왼쪽 자식
        ret += preorder(nodes, idx*2+2)  # 오른쪽 자식
        return ret
    # idx >= len(nodes)일 때는 빈 문자열 반환
    else:
        return ""


## 중위 순회 (왼쪽 자식 -> 루트 -> 오른쪽 자식)
def inorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx*2+1)
        ret += str(nodes[idx])+" "
        ret += inorder(nodes, idx*2+2)
        return ret
    else:
        return ""


## 후위 순회 (왼쪽 자식 -> 오른쪽 자식 -> 루트)
def postorder(nodes, idx):
    if idx < len(nodes):
        ret = postorder(nodes, idx*2+1)
        ret += postorder(nodes, idx*2+2)
        ret += str(nodes[idx])+" "
        return ret
    else:
        return ""


def solution(nodes):
    return [
        # 마지막 공백 제거
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1],
    ]

print(solution([1,2,3,4,5,6,7]))