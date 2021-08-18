"""
<크레인 인형뽑기 게임> https://programmers.co.kr/learn/courses/30/lessons/64061

[input]
board  [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]

moves  [1,5,3,5,1,2,1,4]


[output]
4

"""

""" solution-1 스택 이용 """

def solution(board, moves):
    n_doll = 0  # 터진 인형의 개수
    doll_list = [0]  # 인형이 담기는 리스트

    for i in moves:
        for j in range(len(board)):

            # 인형뽑기
            if board[j][i-1] == 0:
                continue
            else:
                tmp = board[j][i-1]
                board[j][i-1] = 0
                if tmp == doll_list[-1]:
                    doll_list.pop()
                    n_doll += 2
                else:
                    doll_list.append(tmp)
                break
        
    return n_doll

# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))



""" solution-2 스택 이용, 간결한 풀이 """

def solution(board, moves):
    doll_list = []
    n_doll = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:  # 열 고정, 행만 변화
                doll_list.append(board[j][i-1])
                board[j][i-1] = 0

                if len(doll_list) > 1:
                    if doll_list[-1] == doll_list[-2]:
                        doll_list.pop(-1)
                        doll_list.pop(-1)
                        n_doll += 2
                break

    return n_doll



""" solution-3 파이썬 only, 신박한 풀이 """

def solution(board, moves):
    cols = list(map(lambda x: list(filter(lambda y: y > 0, x)), zip(*board)))
    n_doll, doll_list = 0, [0]

    for m in moves:
        if len(cols[m - 1]) > 0:
            if (d := cols[m - 1].pop(0)) == (l := doll_list.pop()):
                n_doll += 2
            else:
                doll_list.extend([l, d])

    return n_doll



"""
<코드 해설>
zip(*board)를 이용해 열마다 원소들을 묶어주고,
filter 함수와 그 조건을 이용하여 열 값이 0보다 큰 것만 살려준다.

board =
[ [0,0,0,0,0],
  [0,0,1,0,3],
  [0,2,5,0,1],
  [4,2,4,4,2],
  [3,5,1,3,1] ]

zip(*board) -> [0,0,0,4,3],[0,0,2,2,5],[0,1,5,4,1],[0,0,0,4,3],[0,3,1,2,1]
여기에서 0을 제거한 리스트가 곧 cols 이다. cols에서 0번째 원소에는 첫 번째 열에 위치한 인형들이 넣어지게 되고, 1번째 원소에는 두 번째 열에 위치한 인형들이 넣어지게 된다.

빈 리스트에서 doll_list.pop()을 하면 에러가 발생하기 때문에 그걸 방지하기 위해 doll_list에 [0]을 넣어주었다.

cols 안의 첫 번째 열을 나타내는 리스트의 첫 번째 원소는 그림 상으로 위에 위치해있는 인형이고 마지막 원소는 가장 바닥에 있어야 할 인형이다. 

cols[m-1].pop(0)을 하여 위에 있는 인형을 빼준다.
doll_list.pop()을 하여 버킷 안에서 맨 위에 있는 인형을 빼준다.

격자 상에서 가져오는 인형과 버킷 안에서 위에 담겨있던 인형의 값을 비교해준다. 
같으면, 인형이 터지는 것이므로 n_doll에 2를 더해준다.
다르면, 현재 버킷의 맨 위에 있던 것을 빼왔기 때문에 그 인형이 버킷의 더 깊은 곳에 있어야 하므로 l을 앞에 두고, 이번에 뽑은 인형 d를 뒤에 두어 [l,d]로 만들어서 기존 버킷에 다시 추가해준다.

"""

"""
<참고>
- filter 함수 사용법  https://wikidocs.net/22803
- 대입표현식(바다코끼리 연산자)이란?  https://www.itworld.co.kr/news/142374

"""