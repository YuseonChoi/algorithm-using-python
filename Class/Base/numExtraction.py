"""
<숫자만 추출하기>

문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다. 만약 't0e0a1c2h0er'에서 숫자만 추출하면 0,0,1,2,0이고 이것을 자연수를 만들면 120이 됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120을 출력하고, 다음 줄에 120의 약수의 개수를 출력하면 됩니다.

"""
#############################################################################

""" solution-1 """

# 문자열에서 숫자를 추출
def changeNum(s):
    nums = ''
    flag = False
    for i in s:
        if i.isdigit():
            if int(i) > 0:
                flag = True
            if flag:
                nums += i
    return int(nums)


# 약수 구하기
def divisor(num):
    cnt = 0
    sqrt_num = int(num ** 0.5)
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            cnt += 1
            if i != int(num/i):
                cnt += 1
    return cnt
        

s = input()
print(changeNum(s))
print(divisor(changeNum(s)))


""" solution-2 """

s = input()
res = 0
for i in s:
    if i.isdecimal():
        res = res * 10 + int(i)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
