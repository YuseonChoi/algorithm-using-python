""" <균형잡힌 세상> https://www.acmicpc.net/problem/9012 """

def validParenthesis(s):
    table = {
        # Key-Value
        ')':'(',
        ']':'[',

    }
    stack = []

    for i in s:
        if i in [')','(',']','[']:
            if i not in table: # Key 값의 여부 판단
                stack.append(i)
            elif not stack or table[i] != stack.pop():
                return 'no'
    if len(stack) == 0:
        return 'yes'


s = input()
while True:
    if s == '.':
        break
    else:
        print(validParenthesis(s))