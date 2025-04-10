""" [섬 연결하기] https://school.programmers.co.kr/learn/courses/30/lessons/42861 """

# solution 1 - 일부 테스트케이스 불통.. 이 코드로는 사이클을 감지하지 못함
def solution(n, costs):
    answer = 0  # 총 건설 비용
    connected = set()  # 연결된 섬
    costs.sort(key=lambda x: x[2])  # costs 건설 비용 측면에서 오름차순 정렬
    
    for n1, n2, cost in costs:
        if len(connected) == n:
            return answer
        if not n1 in connected or not n2 in connected:
            connected.add(n1)
            connected.add(n2)
            answer += cost
        
        
# solution 2 - 사이클 감지
def find(x, parents):
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]


def union(r1, r2, parents, rank):
    root1 = find(r1, parents)
    root2 = find(r2, parents)
    
    if rank[root1] < rank[root2]:
        parents[root1] = root2
    elif rank[root2] < rank[root1]:
        parents[root2] = root1
    else:
        parents[root2] = root1
        rank[root1] += 1
    

def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # costs 건설 비용 측면에서 오름차순 정렬
    
    min_cost = 0
    rank = [0]*n
    parents = [i for i in range(n)]
    num_edge = 0
    
    for n1, n2, cost in costs:
        # 최소 신장 트리 속성 이용
        if num_edge == n-1:
            break
        
        # 현재 간선의 두 노드의 루트 노드 찾기
        r1 = find(n1, parents)
        r2 = find(n2, parents)
        
        # 루트 노드가 다르다면 두 집합을 합침
        if r1 != r2:
            union(r1, r2, parents, rank)
            min_cost += cost
            num_edge += 1
    return min_cost 
        