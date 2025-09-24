""" <여행 경로> https://school.programmers.co.kr/learn/courses/30/lessons/43164 """

def dfs(start, tickets, visited, path, n):
    if sum(visited) == n:
        return path[:]  # 모든 티켓을 사용하면 경로 반환
    
    for idx, ticket in enumerate(tickets):
        # 출발지가 일치하면서 이전 방문 경험이 없다면
        if ticket[0] == start and visited[idx] == 0:
            visited[idx] = 1
            path.append(ticket[1])
            answer = dfs(ticket[1], tickets, visited, path, n)
            # None이 아니라 유효한 경로면 바로 반환
            if answer:
                return answer
            # 백트래킹 (어차피 문제 조건 상 모든 도시를 방문하게 되어 있음)
            path.pop()
            visited[idx] = 0
    return None
    
    
def solution(tickets):
    tickets.sort()  # 사전순 탐색을 위해 정렬
    path = ["ICN"]
    n = len(tickets)
    visited = [0]*n
    
    return dfs("ICN", tickets, visited, path, n)