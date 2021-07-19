"""
<유효한 괄호>  https://leetcode.com/problems/valid-parentheses/

괄호로 된 입력값이 올바른지 판별하라.

"""

class Solution(object):
    def isValid(self, s):
        stack = []
        table = {
            # key-value
            ')':'(',
            '}':'{',
            ']':'[',
        }

        for i in s:
            if i not in table:
                stack.append(i)
            elif not stack or table[i] != stack.pop():
                return False
        return len(stack) == 0
        

s = "()[]"

a = Solution
print(a.isValid(a,s))


"""
<해설>

table 안에 주어진 문자 1개가 들어가 있지 않다면 stack에 추가한다.
반대로, table 안에 문자가 들어있을 때 stack이 비어 있거나 table의 value값과 stack의 마지막 값이 일치하는지 확인한다.
두 조건 중 하나라도 일치한다면, False를 반환한다. s 안의 모든 문자들을 돌고 나서 stack이 비어있다면 True를 반환한다.

"""