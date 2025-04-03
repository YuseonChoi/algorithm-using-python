"""
[깊이 우선 탐색 순회]
깊이 우선 탐색으로 모든 그래프의 노드를 순회하는 함수를 작성하세요.
시작 노드는 start로 주어지며, graph는 [출발 노드, 도착 노드] 쌍이 들어 있는 리스트입니다.
반환값은 그래프의 시작 노드부터 모든 노드를 깊이 우선 탐색으로 탐색한 노드들이 순서대로 들어있는 리스트 입니다.
"""

from collections import defaultdict

adj_list = defaultdict(list)
visited = set()
result = []

def dfs(node):
    # 현재 노드 방문 표시
    visited.add(node)
    result.append(node)

    # 인접한 노드 탐색
    for adj_node in adj_list[node]:
        # 방문하지 않았다면 호출
        if adj_node not in visited:
            dfs(adj_node)


def solution(graph, start):
    for u,v in graph:
        adj_list[u].append(v)
    dfs(start)
    return result
    

# test case 1 - ['A', 'B', 'C', 'D', 'E']
graph = [['A','B'],['B','C'],['C','D'],['D','E']]
start = 'A'

# test case 2 - ['A', 'B', 'D', 'E', 'F', 'C']
graph = [['A','B'],['A','C'],['B','D'],['B','E'],['C','F'],['E','F']]
start = 'A'


print(solution(graph, start))