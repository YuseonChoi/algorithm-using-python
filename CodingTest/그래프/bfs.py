"""
[너비 우선 탐색 구현]
큐와 덱을 이용한 구현
"""

from collections import deque

def bfs(start_node):
    # 방문 표시
    visited = [False for i in range(len(graph)+1)]
    visited[start_node] = True
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        print(node)
        for adj_node in graph[node]:
            # 방문하지 않았을 경우
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True


graph = {
    1: [4,5],
    2: [3],
    3: [],
    4: [2,3],
    5: [4]
}

bfs(1)  # 1 4 5 2 3 

