""" 
<부분집합> 

자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 깊이우선탐색 전위순회방식(왼쪽->오른쪽)으로 출력

[input]
3

[output]
123
12
13
1
23
2
3

"""

""" solution-1 DFS 풀이 """

import sys
input = sys.stdin.readline

def DFS(v):
    if v==n+1:  # 정점이 끝에 도달했다면
        for i in range(1, n+1):
            if node[i]==1:
                print(i, end=' ')
    else:
        node[v]=1
        DFS(v+1)
        node[v]=0
        DFS(v+1)


n = int(input())
node = [0] * (n+1)
DFS(1)


