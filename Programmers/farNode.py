""" <가장 먼 노드> https://school.programmers.co.kr/learn/courses/30/lessons/49189?gad_source=1&gad_campaignid=22681436564&gbraid=0AAAAAC_c4nDGczD64bX4kfw7ydV-CV7Ap&gclid=CjwKCAjw2vTFBhAuEiwAFaScwhH5a3e6LgqqsSigo4tYTrwCXKZEVYZkwD_ANWjEQxj-EHGqOPQ0CxoCxIsQAvD_BwE """

from collections import defaultdict, deque

def bfs(start, graph, n):
    # 거리 배열 초기화 (-1 -> 방문 X)
    dist = [-1] * (n+1)
    dist[start] = 0
    
    q = deque([start])
    
    while q:
        node = q.popleft()
        for next in graph[node]:
            if dist[next] == -1:
                dist[next] = dist[node] + 1
                q.append(next)
                
    return dist
        
def solution(n, edge):
    graph = defaultdict(list)
    
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)
            
    dist = bfs(1, graph, n)  # 1번 노드부터 BFS
    max_dist = max(dist[1:])  # 가장 먼 거리

    return dist.count(max_dist)  # 가장 먼 거리에 있는 노드 개수