""" <이중우선순위큐> https://programmers.co.kr/learn/courses/30/lessons/42628 """

""" solution-1 리스트 이용 """

def solution(operations):
    nums = []
    for i in operations:
        op, n = i.split()
        if op == 'I':
            nums.append(int(n))
        elif op == 'D' and n == '1':
            if nums:
                nums.remove(max(nums))
        else:
            if nums:
                nums.remove(min(nums))
    
    if nums:
        return [max(nums), min(nums)]
    else:
        return [0,0]
                


""" solution-2 논란의 여지가 있는 heap 풀이 """

import heapq as hp

def solution(operations):
    max_heap = []
    min_heap = []
    for i in operations:
        if i == 'D 1':
            if max_heap != []:
                hp.heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:  # 최소힙, 최대힙이 바닥나는 경우
                    max_heap = []
                    min_heap = []
        elif i == 'D -1':
            if min_heap != []:
                hp.heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(i[2:])
            hp.heappush(max_heap, -num)
            hp.heappush(min_heap, num)
    if min_heap == []:
        return [0,0]
    return [-hp.heappop(max_heap), hp.heappop(min_heap)]



""" solution-3 heapq 모듈의 nlargest 함수 이용 (solution-2 보완) """

import heapq as hp

def solution(operations):
    res = []
    for i in operations:
        op, n = i.split()
        if op == 'I':
            hp.heappush(res, int(n))
        elif op == 'D' and n == '1':
            if res:
                res.pop(res.index(hp.nlargest(1,res)[0]))   # 가장 큰 원소 한 개를 리스트로 리턴
        else:
            if res:
                hp.heappop(res)  # 최솟값을 빼줌
        
    if res:
        return [hp.nlargest(1,res)[0], hp.nsmallest(1,res)[0]]
    else:
        return [0,0]

# nlargest(N,lst) : lst(리스트) 안에서 가장 큰 N개의 아이템을 찾아줌
# nsmallest(N,lst) : lst(리스트) 안에서 가장 작은 N개의 아이템을 찾아줌

print(solution(["I 16","D 1"]))                                                                 # [0,0]
print(solution(["I 7","I 5","I -5","D -1"]))                                                    # [7,5]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))    # [333, -45]
print(solution(["I 2","I 4","D -1", "I 1", "D 1"]))                                             # [1,1]

