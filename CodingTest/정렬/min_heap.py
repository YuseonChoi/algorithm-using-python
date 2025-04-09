"""
[힙으로 우선순위 큐 구현하기 (Min Heap, 최소힙)]
우선순위 큐의 핵심 동작은 우선순위가 높은 데이터를 먼저 팝하는 것입니다.
대부분의 정렬 알고리즘의 경우,
매번 새로 정렬하는 데 드는 시간 복잡도가 O(NlogN)입니다.
하지만, 힙은 한 번 구축하면 새 원소가 삽입되고,
다시 힙을 구축하는 시간 복잡도가 O(logN)으로 효율적입니다.
"""

# min heap으로 구현되어 있음
import heapq

# 빈 리스트 생성
heap = []

# 값을 우선순위 큐에 삽입 (heappush 사용)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

# 현재 우선순위 큐의 상태 출력
print(heap)

# 우선순위 큐에서 가장 작은 요소 확인 및 제거 (heappop 사용)
while heap:
    print(heapq.heappop(heap))  # [1,5,10,20]

