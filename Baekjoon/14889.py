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






