""" [게임 맵 최단거리] https://school.programmers.co.kr/learn/courses/30/lessons/1844 """

# 거리의 최적값 = 너비 우선 탐색 (BFS)
from collections import deque

def solution(maps):
    moves = [[-1,0],[1,0],[0,-1],[0,1]]  # 상하좌우 이동 방향
    
    # maps 크기 저장 변수
    n = len(maps)  # 행
    m = len(maps[0])  # 열
    
    # 거리를 저장하는 배열 dist를 -1로 초기화
    dist = [[-1]*m for _ in range(n)]  # n*m 배열
    
    # bfs 함수 선언
    def bfs(start):
        # 시작 위치를 deque에 추가
        q = deque([start])
        dist[start[0]][start[1]] = 1  # 방문 표시
        
        # deque가 빌 때까지 반복
        while q:
            here = q.popleft()
            # 현재 위치에서 이동할 수 있는 모든 방향
            for direction in moves:
                row, column = here[0] + direction[0], here[1] + direction[1]
                
                # 이동한 위치가 map을 벗어난 경우 다음 방향으로 넘어감
                if row < 0 or row >= n or column < 0 or column >= m:
                    continue
                    
                # 이동한 위치에 벽이 있는 경우 다음 방향으로 넘어감
                if maps[row][column] == 0:
                    continue
                    
                # 이동한 위치가 처음 방문하는 경우, deque에 추가하고 거리 갱신
                if dist[row][column] == -1:
                    q.append([row, column])
                    dist[row][column] = dist[here[0]][here[1]] + 1
    
        # 거리를 저장하는 배열 dist 반환
        return dist
    

    bfs([0,0])  # 시작 위치    

    # 목적지까지의 거리 반환, 목적지에 도달하지 못한 경우 -1 반환
    return dist[n-1][m-1]
