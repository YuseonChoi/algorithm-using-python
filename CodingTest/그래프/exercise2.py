"""
[너비 우선 탐색 순회]
너비 우선 탐색으로 모든 노드를 순회하는 함수를 작성하세요.
시작 노드는 매개변수 start로 주어집니다. graph는 (출발 노드, 도착 노드) 쌍들이 들어있는 리스트입니다.
반환값은 그래프의 시작 노드부터 모든 노드를 너비 우선 탐색으로 진행한 순서대로, 노드가 저장된 리스트입니다.
"""

from collections import defaultdict, deque

adj_list = defaultdict(list)
visited = set()
result = []

def bfs(start):
    queue = deque([start])
    visited.add(start)
    result.append(start)

    while queue:
        node = queue.popleft()
        for adj_node in adj_list[node]:
            # 방문하지 않았을 경우
            if adj_node not in visited:
                queue.append(adj_node)
                visited.add(adj_node)
                result.append(adj_node)



def solution(graph, start):
    for u,v in graph:
        adj_list[u].append(v)
    bfs(start)

    return result
    


# test case 1
graph = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(4,8),(5,8),(6,9),(7,9)]
start = 1

# test case 2
graph = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0)]
start = 1

print(solution(graph, start))