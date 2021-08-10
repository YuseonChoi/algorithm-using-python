""" <카드 역배치> https://www.acmicpc.net/problem/10804 """

""" solution-1 파이썬 문자열 슬라이싱 이용 """

def cardReverse(nums,a,b): 
    res = []
    n = nums[a-1:b] 
    n = n[::-1]

    for i in range(a-1):
        res.append(nums[i])
    for j in range(len(n)):
        res.append(n[j])
    for k in range(b,len(nums)):
        res.append(nums[k])
    return res


nums = list(range(1,21))
for _ in range(10):
    a, b = map(int, input().split())
    nums = cardReverse(nums,a,b)

print(' '.join(map(str, nums)))



""" solution-2 직접 구현 """

nums = list(range(0,21))
for _ in range(10):
    a,b = map(int, input().split())

    for i in range((b-a)//2+1):
        nums[a+i], nums[b-i] = nums[b-i], nums[a+i]
nums.pop(0)
print(' '.join(map(str, nums))) 



""" solution-3 직접 구현 """
nums = list(range(1,21))
for _ in range(10):
    a,b = map(int, input().split())

    for i in range((b-a)//2+1):
        nums[a+i-1], nums[b-i-1] = nums[b-i-1], nums[a+i-1]

print(' '.join(map(str, nums))) 

