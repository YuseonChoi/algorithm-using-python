"""
[벨만-포드 알고리즘]
num_vertices는 정점의 개수입니다.
N이 주어진다면, 0~(N-1)값을 갖는 정점이 있습니다.
edges는 간선 정보로, [시작 정점, 끝 정점, 가중치]와 같이 구성되어 있습니다.
source는 시작 정점입니다. 최단 거리를 담은 distance 배열을 반환하면 됩니다.
만약 음의 순환이 있다면 [-1]을 반환하세요. 음의 순환이란 순환할수록 가중치의 합이 적어지는 순환을 말합니다.
"""

INF = 9999999999

def solution(num_vertices, edges, source):
    # 간선 정보를 활용해 인접 리스트 생성
    graph = [[] for _ in range(num_vertices)]
    for edge in edges:
        from_vertex, to_vertex, weight = edge
        graph[from_vertex].append((to_vertex, weight))
        
    # 현재까지 구한 최소 비용을 INF로 설정 (시작 노드 제외)
    distance = [INF] * num_vertices
    distance[source] = 0
    
    # 정점의 개수 -1 만큼 최소 비용을 갱신
    for _ in range(num_vertices -1):
        for u in range(num_vertices):
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                     
    # 음의 순환이 있는지 확인
    for u in range(num_vertices):
        for v, weight in graph[u]:
            if distance[u] + weight < distance[v]:
                return [-1]
            
    return distance
        

# test case 1
num_vertices = 5
edges = [[0,1,4],[0,2,3],[0,4,-6],[1,3,5],[2,1,2],[3,0,7],[3,2,4],[4,2,2]]
source = 0

# test case 2
num_vertices = 4
edges = [[0,1,5],[0,2,-1],[1,2,2],[2,3,-2],[3,0,2],[3,1,6]]
source = 0

print(solution(num_vertices, edges, source))