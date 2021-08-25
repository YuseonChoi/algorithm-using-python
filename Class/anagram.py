"""
<Anagram(아나그램)>

[input]
AbaAeCe
baeeACA

[output]
YES

"""

""" solution-2 dict 자료형, get함수 사용 """

import sys
input = sys.stdin.readline

a = input()
b = input()

dicA = dict()
dicB = dict()

for i in a:
    dicA[i] = dicA.get(i,0) + 1
for i in b:
    dicB[i] = dicB.get(i,0) + 1

for i in dicA.keys():
    if i in dicB.keys():
        if dicA[i] != dicB[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")


# 참고 https://leti-lee.tistory.com/14
# if가 아닌 for, while 루프에 대한 else문
# 이 경우 else문은 for문이 중간에 break로 끊기지 않고 끝까지 수행하였거나 while문에 False를 만나서 종료될 때 실행된다. 



""" solution-2 dict 개선 """

import sys
input = sys.stdin.readline

a = input()
b = input()

dic = dict()

for i in a:
    dic[i] = dic.get(i,0) + 1
for i in b:
    dic[i] = dic.get(i,0) - 1

for i in a:
    if dic[i] > 0:
        print("NO")
        break

else:
    print("YES")



""" solution-3 defaultdict 사용 """

# 알파벳 나열 순서는 다르지만 그 구성(개수)은 똑같다.
import sys
from collections import defaultdict
input = sys.stdin.readline


def solution(a,b):
    dic = defaultdict(int)

    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in b:
        if b.count(i) != dic[i]:
            return "NO"
    return "YES"


a = input()
b = input()
print(solution(a,b))

    