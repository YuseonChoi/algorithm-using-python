""" <시험 감독> https://www.acmicpc.net/problem/13458 """

"""
solution 1 - 내 풀이, dp활용
* 주어진 공식 테스트케이스는 모두 통과했지만 제출하면 틀렸다고 나온다.
* 반례 찾는 연습을 해야할 것 같다.

[풀이에 도움이 되었던 반례들]
counter_ex1)
 2
 1000000 1
 999999 1
 
counter_ex2)
1
1
6 2
"""

N = int(input())
app = list(map(int, input().split()))
asp, bsp = map(int, input().split())

dp = [-1]*1000001
ans = 0
for i in app:
    if dp[i] != -1:
        ans += dp[i]  # 저장된 값을 사용
        continue
    tmp = 0

    if (i-asp) < 0:
        ans += 1
        continue

    if (i-asp)%bsp == 0:
        if (i-asp) < 0:  # 더 이상 감독할 필요가 없음
            ans += 1
            continue
        else:
        # print(i, (1 + (i-asp)//bsp))
            tmp = (1 + (i-asp)//bsp)
        # print((i-asp)//bsp)
    else:
        tmp = (1 + (i - asp) // bsp) + 1

    ans += tmp
    dp[i] = tmp

print(ans)


""" solution 2 """
N = int(input())
app = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N
for i in app:
    if i-B > 0:  # 부감독관이 필요한 경우
        ans += ((i-B) + (C-1))//C

print(ans)

