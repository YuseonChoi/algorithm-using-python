""" <그래프 순회 DFS> """

""" solution-1 스택 구현 """

graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}


def stack_DFS(start):   # start는 출발 노드
    discovered = []     # 지나간 노드를 담음
    stack = [start]     # 탐색할 노드를 담음
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for i in graph[v]:
                stack.append(i)

    return discovered

print(stack_DFS(1))



""" solution-2 재귀 구현 """

def recursive_DFS(v, discovered=[]):
    discovered.append(v)
    for i in graph[v]:
        if i not in discovered:
            discovered = recursive_DFS(i, discovered)
    return discovered

print(recursive_DFS(1))



""" 
<두 방식의 차이점>
재귀 DFS는 사전식 순서로 방문한 데 반해 반복 DFS는 역순으로 방문했다.
스택으로 구현 시, 가장 마지막에 삽입된 노드부터 꺼내어 반복하게 되기 때문에
가장 최근에 담긴 노드, 즉 가장 마지막부터 방문하게 된다.

"""