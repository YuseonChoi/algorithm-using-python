""" <공주 구하기> - 요세푸스 문제

[input]
8 3

[output]
7

1,2,3,4,5,6,7,8 
1,2,4,5,6,7,8 - 3
1,2,4,5,7,8 - 6
2,4,5,7,8 - 1
2,4,7,8 - 5
4,7,8 - 2
4,7 - 8
7 - 4

"""

""" solution-1 """

from collections import deque

def solution(people, num):
    dq = list(range(1, people+1))
    prince = deque(dq)
    while prince:
        for i in range(num-1):
            cur = prince.popleft()
            prince.append(cur)
        prince.popleft()
        if len(prince) == 1:
            return prince[0]
    
        
people, num = map(int, input().split())
print(solution(people,num))
