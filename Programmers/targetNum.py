""" <타겟 넘버> https://school.programmers.co.kr/learn/courses/30/lessons/43165 """

""" solution 1 - DFS 풀이 """

def dfs(numbers, target, idx, value):
    global cnt
    
    # 마지막 원소이면서 타겟 넘버일 경우
    if idx == len(numbers) and value == target:
        cnt += 1
        return
    
    # 마지막 원소인데 타겟 넘버가 아닐 경우
    if idx == len(numbers):
        return 
    
    dfs(numbers, target, idx+1, value + numbers[idx])
    dfs(numbers, target, idx+1, value - numbers[idx])
    

def solution(numbers, target):
    
    global cnt
    cnt = 0
    dfs(numbers, target, 0, 0)
    
    return cnt



""" solution 2 - BFS 풀이 """

def solution(numbers, target):
    leaves = [0]
    cnt = 0
    
    for num in numbers:
        tmp = []
        
        # 자손 노드
        for leaf in leaves:
            tmp.append(leaf + num)  # 더하는 경우
            tmp.append(leaf - num)  # 빼는 경우
            
        leaves = tmp
        
    # 모든 경우의 수 계산 후 target과 같은지 확인
    for leaf in leaves:
        if leaf == target:
            cnt += 1

    return cnt