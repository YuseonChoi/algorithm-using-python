"""
[다익스트라 알고리즘]
주어진 그래프와 시작 노드를 이용하여 다익스트라 알고리즘을 구현하는 함수를 작성하세요.
시작 노드 start, 노드의 개수 numNodes, [시작 노드, 도착 노드, 가중치] 형태로
간선 정보를 담은 배열 edges가 인수로 주어집니다.
edges에 [2,1,9]가 있다면, 시작 노드 2에서 도착 노드 1까지 가중치가 9인 간선이 있다는 뜻입니다.
시작 노드 start부터 각 노드까지 최소 비용을 담은 벡터를 반환하는 함수를 구현하세요.
"""

import heapq
from collections import defaultdict, deque

INF = 9999999999

def solution(start, num_nodes, edges):
    # 그래프 초기화 (인접 리스트)
    graph = defaultdict(list)
    for from_node, to_node, weight in edges:
        graph[from_node].append((to_node, weight))
        
    # 최단 경로 및 방문 이력 초기화
    distances = [INF] * numNodes
    visited = [False] * numNodes
    distances[start] = 0
    
    # 우선순위 큐 
    priority_queue = [(0, start)]  # (거리, 노드)
    
    while priority_queue:
        # 현재 노드 찾기
        current_distance, current_node = heapq.heappop(priority_queue)  # 거리가 최소인 값을 pop함
        
        # 이미 방문한 노드를 무시
        if visited[current_node]:
            continue
        
        # 현재 노드 방문 처리
        visited[current_node] = True
        
        # 인접 노드에 대한 거리 업데이트
        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
        
    return distances
        
    

# test case 1 - [0, 4, 3]
start = 0
numNodes = 3
edges = [[0,1,9],[0,2,3],[1,0,5],[2,1,1]]

# test case 2 - [0, 1, 6, 7]
start = 0
numNodes = 4
edges = [[0,1,1],[1,2,5],[2,3,1]]

print(solution(start, numNodes, edges))


"""
인접 리스트를 생성하는 부분은 간선 개수만큼 인접 리스트를 생성하므로 시간 복잡도는 O(E),
이후, 최소 비용의 노드를 찾는 부분에서 while문은 정점 개수 V번 수행하고,
우선순위 큐의 pop() 메서드를 수행하므로 시간 복잡도는 O(VlogV).
인접 노드에 대해 거리를 업데이트 하는 부분은 간선 개수만큼 수행하므로 O(E).
최종 시간 복잡도는 O(E+VlogV).
"""