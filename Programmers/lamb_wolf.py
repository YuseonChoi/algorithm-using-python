""" <양과 늑대> https://school.programmers.co.kr/learn/courses/30/lessons/92343 """

from collections import defaultdict


answer = 0

def solution(info, edges):
    global answer
    graph = defaultdict(list)
    for n1,n2 in edges:
        graph[n1].append(n2)

    def dfs(node, to_visit, num_lamb, num_wolf):
        global answer
        # 현재 노드 방문
        if info[node] == 0:
            num_lamb += 1
            answer = max(answer, num_lamb)
        else:
            num_wolf += 1

        # 늑대가 양 이상이면 탐색 중단
        if num_wolf >= num_lamb:
            return
        
        next_nodes = to_visit[:]  # 방문할 후보군
        next_nodes.extend(graph[node])  # 현재 노드의 자식 노드도 후보군에 저장

        for n in next_nodes:
            next_to_visit = next_nodes[:]  # 후보 전체를 복사
            next_to_visit.remove(n)  # 이번 턴에 선택한 노드는 제외
            dfs(n,next_to_visit,num_lamb,num_wolf)

    dfs(0,[],0,0) 
    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))