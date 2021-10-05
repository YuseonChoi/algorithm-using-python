""" <앵무새> https://www.acmicpc.net/problem/14713 """

""" soluton-X 반례까지 찾고 열심히 풀었지만.. 틀린 풀이 """

from collections import deque

n = int(input())
qlist = list()

for i in range(n):
    qlist.append(deque(map(str, input().split())))

# print(qlist[0])   # deque(['i', 'want', 'to', 'see', 'you'])
# print(qlist[1])   # deque(['next', 'week'])
# print(qlist[2])   # deque(['good', 'luck'])

res = list(input().split())
tmp = res.copy()  # res가 직접 바뀌면 안되므로 tmp 생성
# tmp = res, 얕은 복사 : 원본 객체의 주소값을 복사
# tmp = res.copy(), 깊은 복사 : 참조된 객체 자체를 복사

flag = True
for i in res:
    for q in qlist:
        if i in q:
            tmp.remove(i)
            if i == q.popleft():
                break
            else:
                flag=False
                break

sum = 0
for q in qlist:
    sum += len(q)


if not tmp and flag and len(res)==sum:
    print('Possible')
else:
    print('Impossible')



""" solution-1 deque() 활용 

[input]
3
i want to see you
next week
good luck
i want next good luck week to see you

[output]
Possible

"""

from collections import deque

n = int(input())  # 앵무새 수
qlist = list()    # 문장을 담을 리스트

for i in range(n):
    qlist.append(deque(map(str, input().split())))

# print(qlist[0])   # deque(['i', 'want', 'to', 'see', 'you'])
# print(qlist[1])   # deque(['next', 'week'])
# print(qlist[2])   # deque(['good', 'luck'])

res = deque(map(str, input().split()))
# print(res)        # deque(['i', 'want', 'next', 'good', 'luck', 'week', 'to', 'see', 'you'])

def possible(res, qlist):
    cnt = 0   # 오류 감지  
    i = 0     # qlist 인덱스 숫자
    while res:
        if qlist[i] and res[0] == qlist[i][0]:
            qlist[i].popleft()
            res.popleft()
            cnt = 0
        else:
            if cnt == n:
                return False
            cnt += 1
        i = (i+1) % n
    sum = 0
    for i in range(n):
        if len(qlist[i]) == 0:
            sum += 1
    
    if not res and sum == n:
        return True
    else:
        return False
    
if possible(res, qlist):
    print('Possible')
else:
    print('Impossible')


