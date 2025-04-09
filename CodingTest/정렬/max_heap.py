"""
[힙으로 우선순위 큐 구현하기 (Max Heap, 최대힙)]
값이 클수록 우선순위가 높은 큐를 구현하고자 함.
푸시할 때 -1을 곱하고 값을 팝할 때는 판한 값에 -1을 곱해서 반환.
"""

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, value):
        heapq.heappush(self.heap, -value)
        
    def pop(self):
        return -heapq.heappop(self.heap)
    
max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(5)
max_heap.push(20)
max_heap.push(1)

print(max_heap.heap)

while max_heap.heap:
    print(max_heap.pop())  # 값이 큰 순서대로 pop