""" <회의실 배정> https://www.acmicpc.net/problem/1931 """

""" solution-1 """

import sys
input = sys.stdin.readline

N = int(input())
time = [[0]*2 for _ in range(N)]
res = 1

for i in range(N):
    start, end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end

# 빨리 끝나는 회의, 빨리 시작하는 회의 정렬
time.sort(key=lambda x:(x[1],x[0]))

end_time = time[0][1]
for i in range(1,len(time)):
    if end_time <= time[i][0]:
        end_time = time[i][1]
        res += 1

print(res)
