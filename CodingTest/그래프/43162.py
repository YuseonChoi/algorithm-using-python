""" [네트워크] https://school.programmers.co.kr/learn/courses/30/lessons/43162 """

from collections import defaultdict

def dfs(computers, visited, node):
    visited[node] = True
    for idx, connected in enumerate(computers[node]):
        # 연결되어있는데 방문하지 않은 노드일 경우
        if connected and not visited[idx]:
            dfs(computers, visited, idx)

            
def solution(n, computers):
    answer = 0  # DFS 함수 호출 횟수
    visited = [False] * n  # 방문 여부를 저장하는 리스트
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer +=1 

    return answer