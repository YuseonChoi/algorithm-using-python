""" <DFS와 BFS> https://www.acmicpc.net/problem/1260 """

import sys
from collections import defaultdict, deque

input = sys.stdin.readline
graph = defaultdict(list)
n,m,v = map(int, input().split())  # 노드(정점), 간선, 시작 노드

# graph 만들기
for i in range(m):
    a,b = map(int, input().split())
    # 간선은 양방향
    graph[a].append(b)
    graph[b].append(a)

# 방문할 수 있는 노드가 여러 개인 경우 노드 번호가 작은 것을 먼저 방문
for i in graph:
    graph[i].sort()


# DFS(깊이우선탐색) - 스택
def Stack_DFS(v, visited=[]):
    stack = [v]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack.extend(sorted(graph[n], reverse=True))
    return visited


# DFS(깊이우선탐색) - 재귀
def DFS(v, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if i not in visited:
            visited = DFS(i, visited)
    return visited


# BFS(너비우선탐색)
def BFS(v, visited=[]):
    queue = deque([v])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return visited
        

print(*Stack_DFS(v))
print(*DFS(v))
print(*BFS(v))


"""
<참고>
https://ye333.tistory.com/78

"""