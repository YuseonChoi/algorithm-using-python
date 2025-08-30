""" <스타트와 링크> https://www.acmicpc.net/problem/14889 """

""" 시간초과 - 테스트케이스는 통과 """
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

R = N // 2
min_score = 100

# 팀 내 조합 구하기
all_combs = list(combinations(range(1, N+1), R))
for comb in all_combs:
    match_comb = [c for c in all_combs if set(c).isdisjoint(comb)][0]

    sum_comb = 0
    sum_match_comb = 0
    # print(comb)
    for i in range(len(comb)):
        for j in range(i+1, len(comb)):
            # print(comb[i], comb[j])
            sum_comb += (arr[comb[i]-1][comb[j]-1] + arr[comb[j]-1][comb[i]-1])

    # print(match_comb)
    for i in range(len(match_comb)):
        for j in range(i+1, len(match_comb)):
            # print(match_comb[i], match_comb[j])
            sum_match_comb += (arr[match_comb[i]-1][match_comb[j]-1] + arr[match_comb[j]-1][match_comb[i]-1])

    if min_score > abs(sum_comb-sum_match_comb):
        min_score = abs(sum_comb-sum_match_comb)

    # print(sum_comb, sum_match_comb, min_score)

print(min_score)


"""
solution - 백트래킹
* 이진 트리 형태로 구성한다면 2^20 = 10^6
* yes no 형태의 이진트리인지 멀티트리인지 복잡도 계산해보기
* 다양한 아이디어를 내기 보다는 백트래킹으로 풀이해보는 게 좋음
* 백트래킹 : 가능한 모든 경우
"""

# 빈번하게 계산을 해야한다면 함수 호출보다는 dfs 안에 구성하는 게 빠를 수 있음
# 가지치기는 호출 횟수는 줄일 수 있으나 실행 시간을 줄일 수 있을지 여부는 알 수 없 -> 테스트케이스에 따라 다름
def cal(alst, blst):
    asm = 0
    bsm = 0
    for i in range(0, M):
        for j in range(0, M):
            asm += arr[alst[i]][alst[j]]
            bsm += arr[blst[i]][blst[j]]
    return abs(asm - bsm)

def dfs(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):  # 같은 인원 수로 팀을 구성
            ans = min(ans, cal(alst, blst))
        return

    # A팀 선택
    dfs(n+1, alst+[n], blst)
    # B팀 선택
    dfs(n + 1, alst, blst+[n])

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

M = N//2
ans = 100*M*M
dfs(0, [], [])
print(ans)




