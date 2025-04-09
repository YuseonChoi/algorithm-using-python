"""
[값을 한꺼번에 우선순위 큐에 넣기]
데이터가 여러 개 있으면 heapify() 메서드를 활용할 수 있음.
"""

import heapq

# 우선순위와 작업을 포함하는 리스트 생성
tasks = [(3, "작업 A"), (1, "작업 C"), (2, "작업 B")]

# 리스트를 힙으로 변환 
heapq.heapify(tasks)

# 추가 작업 삽입
heapq.heappush(tasks, (0, "작업 D"))

# 현재 힙 상태 출력 - [(0, '작업 D'), (1, '작업 C'), (2, '작업 B'), (3, '작업 A')]
print(tasks)  

# 우선순위가 높은 작업부터 pop - Min Heap이므로 작은 값부터 pop
while tasks:
    print(heapq.heappop(tasks))