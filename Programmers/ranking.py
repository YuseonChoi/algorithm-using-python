""" <순위> https://school.programmers.co.kr/learn/courses/30/lessons/49191 """

def solution(n, results):
    answer = 0
    game = [[-1]*n for _ in range(n)]
    
    # game 초기화 (win->1,lose->0,unknown->-1)
    for win, lose in results:
        game[win-1][lose-1] = 1
        game[lose-1][win-1] = 0
    
    # 간접적으로 승리 여부 추정 (플로이드-워셜 알고리즘)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if game[i][k] == 1 and game[k][j] == 1:
                    game[i][j] = 1
                    game[j][i] = 0
                if game[i][k] == 0 and game[k][j] == 0:
                    game[i][j] = 0
                    game[j][i] = 1
                    
    # 순위를 확실히 알 수 있는 선수 찾기
    for i in range(n):
        known = 0
        for j in range(n):
            if game[i][j] != -1:
                known += 1
        # 결과가 다 나온 선수
        if known == n-1:
            answer += 1
              
    return answer