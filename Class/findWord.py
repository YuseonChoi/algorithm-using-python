"""
<단어 찾기>

[input]
5
big
good
sky
blue
mouse
sky
good
mouse
big

[output]
blue


"""

""" solution-1 딕셔너리 사용 """

dic = {}
N = int(input())
for _ in range(N):
    a = input()
    dic[a] = 0

for _ in range(N-1):
    b = input()
    if b in dic:
        dic[b] += 1

for key, value in dic.items():
    if value == 0:
        print(key)