""" <영단어 암기는 괴로워> https://www.acmicpc.net/problem/20920 """

import sys
input = sys.stdin.readline

dic = {}

N, M = map(int, input().split())
for i in range(N):
    word = input().rstrip()
    # 단어 길이가 M보다 작으면 pass
    if len(word) < M:
        continue
    # 단어가 존재하지 않으면 None을 반환
    if dic.get(word):
        dic[word][0] += 1
    else:
        dic[word] = [1, len(word), word]

res = sorted(dic.items(), key = lambda x: (-x[1][0], -x[1][1], x[1][2]))

for i in res:
    print(i[0])
