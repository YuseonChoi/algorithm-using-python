""" <후위표기식2> https://www.acmicpc.net/problem/1935 

[input]
5
ABC*+DE/-
1
2
3
4
5

[output]
6.20

"""

""" solution-1 """

# 계산해주는 함수
def calculator(op,s1,s2):
    if op == '+':
        return s1 + s2
    elif op == '-':
        return s1 - s2
    elif op == '*':
        return s1 * s2
    elif op == '/':
        return s1 / s2


stack = []   # 연산할 숫자를 담을 리스트
dic = {}
n = int(input())
s = input()


for i in s:
    if i.isalpha():   # 연산자가 아니라면
        if i not in dic:
            dic[i] = int(input())
        stack.append(dic[i])
    
    else:             # 연산자이면
        s2 = stack.pop()
        s1 = stack.pop()
        stack.append(calculator(i,s1,s2))
print(format(stack[0],'.2f'))
