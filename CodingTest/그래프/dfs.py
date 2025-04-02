"""
[깊이 우선 탐색 구현]
시스템 스택을 이용한 재귀 함수로 구현
"""

def dfs(current_node):
    # 현재 노드 방문
    visited[current_node] = True
    print(current_node)

    # 인접한 노드 탐색
    for adj_node in graph[current_node]:
        # 방문하지 않았다면 호출
        if not visited[adj_node]:
            dfs(adj_node)

graph = {
    1: [4,5],
    2: [3],
    3: [],
    4: [2,3],
    5: [4]
}

visited = [False for i in range(len(graph)+1)]

dfs(1)  # 1 4 2 3 5
