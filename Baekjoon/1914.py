""" <하노이 탑> https://www.acmicpc.net/problem/1914 

1. 1번 기둥에 위치한 N개의 원판 중, 위에 있는 N-1개의 원판을 2번 기둥으로 옮긴다.
2. 1번 기둥에 남아있는 1개의 원판을 3번 기둥으로 옮긴다.
3. 2번 기둥에 있는 N-1개의 원판을 3번 기둥으로 옮긴다.

P(n) = 2P(n-1) + 1
P(1) = 1
P(2) = 2 P(1) + 1 = 2 + 1 = 3
P(3) = 2 P(2) + 1 = 2 x 3 + 1 = 4 + 2 + 1 = 7
P(4) = 2 P(3) + 1 = 2 x 7 + 1 = 8 + 4 + 2 + 1 = 15

등비수열 공식 이용,
P(n) = 2**n-1

"""

def hanoi(n,a,b,c):
    if n == 1:
        print(a,c,sep=" ")
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)

n = int(input())
print(2**n-1)
if n <= 20:
    hanoi(n,1,2,3)