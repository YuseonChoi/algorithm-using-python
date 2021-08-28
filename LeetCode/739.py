""" <일일 온도> https://leetcode.com/problems/daily-temperatures/

[input]
temperatures = [73,74,75,71,69,72,76,73]

[output]
[1,1,4,2,1,1,0,0]

"""

""" solution-1 스택 값 비교 """

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            # 현재 온도가 스택 값보다 높다면 정답 처리
            while stack and temp > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer
        

a = Solution()
print(a.dailyTemperatures([73,74,75,71,69,72,76,73]))