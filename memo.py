from collections import deque

def solution(maps):
    moves = [[-1,0],[1,0],[0,-1],[0,1]]  # 상하좌우 이동 방향
    
    n = len(maps)
    m = len(maps[0])
    
    dist = [[-1]*m for _ in range(n)]
    
    def bfs(start):
        q = deque([start])
        dist[start[0]][start[1]] = 1
        
        while q:
            here = q.popleft()
            for direction in moves:
                row, column = here[0] + direction[0], here[1] + direction[1]
                
                if row < 0 or row >= n or column < 0 or column >= n:
                    continue
                if maps[row][column] == 0:
                    continue
                
                if dist[row][column] == -1:
                    q.append([row, column])
                    dist[row][column] = dist[here[0]][dist[here[1]]]+1
                    
        return dist
    
    bfs([0,0])
    
    return dist[n-1][m-1]