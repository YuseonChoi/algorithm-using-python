""" <쇠막대기> https://www.acmicpc.net/problem/10799 

[input] 
()(((()())(())()))(())

[output]
17

"""

""" solution-1 """

# import sys
# input = sys.stdin.readline
# stack.pop()할 때, IndexError 발생 !!!

s = input()
stack = []
sum = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            sum += len(stack)
        else:
            sum += 1

print(sum)
