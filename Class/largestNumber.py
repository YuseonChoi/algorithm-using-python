"""
<가장 큰 수>

[input #1]      [input #2]
5276823 3       9977252641 5

[output #1]     [output #2]
7823            99776

"""

""" solution-1 """

A, B = map(int, input().split())
A = list(map(int, str(A)))
stack = []

for i in A:
    while stack and B > 0 and stack[-1] < i:
        stack.pop()
        B -= 1
    stack.append(i)
if B != 0:
    stack = stack[:-B]

res = ''.join(map(str, stack))
print(res)
