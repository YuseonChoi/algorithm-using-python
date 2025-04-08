"""
[간단한 유니온-파인드 알고리즘 구현하기]
상호배타적 집합을 표현하고 관리하는 데 2가지 연산(union, find)이 필요합니다.
- union(x,y): x와 y가 속한 두 집합을 합칩니다.  
- find(x): x가 속한 집합의 대표 원소를 찾습니다.
operations 배열에 있는 연산을 모두 수행하고, 파인드 연산 결과를 순서에 맞춰
배열에 담아 반환하는 함수를 구현하세요. 단, 모든 파인드 연산은 유니온 연산 뒤에 옵니다.
"""

def find(x, parents):
    # x가 속한 집합의 대표 원소를 찾음
    if parents[x] != x:
        parents[x] = find(parents[x], parents)  # 경로 압축
    return parents[x]


def union_set(x, y, parents, rank_data):
    # x와 y가 속한 두 집합을 합침
    root1 = find(x, parents)
    root2 = find(y, parents)
    
    # 랭크 알고리즘
    if root1 != root2:
        # 랭크가 더 큰 노드를 랭크가 작은 노드의 부모 노드로 바꿈
        if rank_data[root1] < rank_data[root2]:
            parents[root1] = root2
        elif rank_data[root1] > rank_data[root2]:
            parents[root2] = root1
        else:
            parents[root2] = root1
            rank_data[root1] += 1
            

def solution(k, operations):
    # 초기의 각 부모 노드의 값은 현재 노드(인덱스)로 설정
    parents = list(range(k))
    rank_data = [0]*k
    
    results = []
    for op in operations:
        if op[0] == 'u':
            x = int(op[1])
            y = int(op[2])
            union_set(x,y,parents,rank_data)
        elif op[0] == 'f':
            x = int(op[1])
            y = int(op[2])
            # 파인드 연산을 통해 x,y의 루트노드가 같은지 확인해서 결과 저장
            results.append(find(x,parents) == find(y,parents))

    return results



# test case 1 
k=3
operations = [['u','0','1'],['u','1','2'],['f','0','2']]  # [true]

# test case 2
k=4
operations = [['u','0','1'],['u','2','3'],['f','0','1'],['f','0','2']]  # [true, false]

print(solution(k, operations))