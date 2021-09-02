""" <후위표기식> https://www.acmicpc.net/problem/1918 

[input]   A*(B+C)
[output]  ABC+*

"""

import sys
input = sys.stdin.readline

def postfix(s):
    stack = []
    answer = ''

    for i in s:
        # 대문장일 경우
        if i.isupper():
            answer+=i
        else:
            # 열린 괄호일 경우
            if i=='(':
                stack.append(i)
            # 우선순위 높은 '*','/'일 경우
            elif i=='*' or i=='/':
                while stack and (stack[-1]=='*' or stack[-1]=='/'):
                    answer+=stack.pop()
                stack.append(i)
            # 우선순위 낮은 '+','-'일 경우
            elif i=='+' or i=='-':
                while stack and stack[-1]!='(':
                    answer+=stack.pop()
                stack.append(i)
            # 닫힌 괄호일 경우           
            elif i==')':
                while stack and stack[-1]!='(':
                    answer+=stack.pop()   # 연산자 빼줌
                stack.pop()               # 열린괄호 빼줌

    # 스택에 남아있는 연산자들을 모두 빼줌            
    while stack: 
        answer+=stack.pop()

    return answer
    

s = input().rstrip()
print(postfix(s))


"""
<추가 설명>
현재 문자열의 우선순위가 stack 마지막의 문자열 우선순위보다 낮거나 같을 경우 stack의 마지막 문자열 값을 빼준다.
'*','/'는 우선순위가 높기 때문에 같은 '*','/'가 나올 때 뺄 수 있다.
'+','-'는 우선순위가 낮기 때문에 같은 '+','-','*','/'가 나올 때 뺄 수 있다.

"""