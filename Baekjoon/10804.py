""" 카드 역배치 https://www.acmicpc.net/problem/10804 """

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


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for _ in range(10):
    a, b = map(int, input().split())
    nums = cardReverse(nums,a,b)

print(' '.join(map(str, nums)))
