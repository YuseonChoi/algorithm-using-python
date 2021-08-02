""" 카드2 https://www.acmicpc.net/problem/2164 """

""" solution-1 list 사용, 시간 초과 """

N = int(input())
cards = [i+1 for i in range(N)]

while True:
    if len(cards) == 1:
        break
    cards.pop(0)
    cards.append(cards.pop(0))

print(cards[0])

# 리스트에서 pop(0)을 수행할 때마다 뒤의 내용을 한 칸씩 앞당기기 때문에 O(n) 만큼 걸림 



""" solution-2 deque() 사용 """

import collections
N = int(input())
q = collections.deque()

for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])

# deque()를 사용하면 양쪽 추가 삭제가 모두 O(1)

