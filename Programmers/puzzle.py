""" <퍼즐 조각 채우기> https://school.programmers.co.kr/learn/courses/30/lessons/84021 """

from collections import deque

# 상하좌우 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# BFS로 덩어리 추출
def get_shapes(board, target):
    N = len(board)
    visited = [[False]*N for _ in range(N)]
    shapes = []

    for r in range(N):
        for c in range(N):
            if board[r][c] == target and not visited[r][c]:
                q = deque()
                q.append((r,c)) 
                visited[r][c] = True
                shape = []

                while q:
                    cr, cc = q.popleft()
                    shape.append((cr, cc))
                    for i in range(4):
                        nr, nc = cr + dr[i], cc + dc[i]  # 상하좌우 이동 좌표
                        if 0 <= nr < N and 0 <= nc < N:  # 이동한 좌표가 table, game board 범위 안에 있는 경우
                            if board[nr][nc] == target and not visited[nr][nc]:
                                visited[nr][nc] = True
                                q.append((nr, nc))
                shapes.append(normalize(shape))
    return shapes


# 원점 기준 재배치
def normalize(shape):
    min_r = min(x[0] for x in shape)  # 최소 row 값
    min_c = min(x[1] for x in shape)  # 최소 column 값
    normalized = sorted([(r - min_r, c - min_c) for r, c in shape])  # 원점 좌표에서 시작하여 재배치
    return normalized


# 90도 회전
def rotate(shape, N):
    rotated = [(c, N-1-r) for r,c in shape]
    return normalize(rotated)


def solution(game_board, table):
    N = len(game_board)
    answer = 0

    # 1. 빈 공간과 퍼즐 조각 추출
    empty_spaces = get_shapes(game_board, 0)
    pieces = get_shapes(table, 1)

    used = [False]*len(pieces)

    # 2. 빈 공간 하나씩 검사
    for empty in empty_spaces:
        for i, piece in enumerate(pieces):
            # 이미 사용한 조각이면 넘어감
            if used[i]:
                continue
            matched = False
            # 4회 회전 확인
            rotated_piece = piece
            for _ in range(4):
                if empty == rotated_piece:
                    # 빈 공간과 회전 조각의 모양이 일치해야 match로 판단
                    answer += len(piece)
                    used[i] = True
                    matched = True
                    break
                rotated_piece = rotate(rotated_piece, N)
            if matched:
                break

    return answer


print(solution(
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
    [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
))

print(solution(
    [[0,0,0],[1,1,0],[1,1,1]],
    [[1,1,1],[1,0,0],[0,0,0]]
))