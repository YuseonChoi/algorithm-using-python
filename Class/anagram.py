"""
<Anagram(아나그램)>

[input]
AbaAeCe
baeeACA

[output]
YES

"""

""" solution-1 dict 해쉬, get함수 사용 """

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



""" solution-2 dict 해쉬 개선 """

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
    if dic[i] != 0:
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

    

""" solution-4 list 해쉬 """

import sys
input = sys.stdin.readline
# readline 그대로 사용하면 IndexError 발생
# readline()은 개행문자(줄 바꿈 문자)를 포함하고 있기 때문에 제거해줘야 한다.
# 따라서, 오른쪽 공백을 제거해주는 rstrip 사용

a = input().rstrip()
b = input().rstrip()

# 영어 대소문자 26+26=52 
lstA = [0]*52
lstB = [0]*52

for i in a:
    if i.isupper():
        lstA[ord(i)-65] += 1  # A(65)가 0번째 인덱스
    else:
        lstA[ord(i)-71] += 1  # a(97)가 26번째 인덱스

for i in b:
    if i.isupper():
        lstB[ord(i)-65] += 1
    else:
        lstB[ord(i)-71] += 1

for i in range(52):
    if lstA[i] != lstB[i]:
        print('NO')
        break

else:
    print('YES')



