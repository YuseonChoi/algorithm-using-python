""" <진법 변환> https://www.acmicpc.net/problem/2745

[input]
ZZZZZ 36

[output]
60466175

"""

""" solution-1 반복문 풀이 """

def transform(N,B):
    sum = 0
    cnt = len(N)-1
    for i in N:
        if i.isdigit():
            num = int(i)
        else:
            num = ord(i)-55
        sum += (num*(B**cnt))
        cnt -= 1
    return sum

N, B = input().split()
B = int(B)
print(transform(N,B))



""" solution-2 재귀 풀이 """

# 진법 변환 함수
def transform(i, N, B, dic):
    if i == len(N):
        return 0
    
    cnt = len(N)-1-i       # 제곱할 수 
    num = dic[N[i]]

    return num*(B**cnt) + transform(i+1, N, B, dic)


# 딕셔너리 생성 함수
def make_dict():
    dic = {}

    for i in range(36):         # 숫자 0-9(10개), A-Z(26개)
        if i < 10:
            dic[str(i)] = i               # dic[1] = 1
        else:
            dic[chr(i-10+ord('A'))] = i   # dic['A'] = 10

    return dic


N, B = input().split()
print(transform(0,N,int(B), make_dict()))