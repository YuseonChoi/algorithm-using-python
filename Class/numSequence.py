"""
<수들의 합>

N개의 수로 된 수열 A[1], A[2], ... , A[N]이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + ... + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

[input]
8 3
1 2 1 3 1 1 1 2

[output]
5

"""

""" solution-1 시간초과... """
N, M = map(int, input().split())
A = list(map(int, input().split()))

def numSequence(A, M):
    cnt, sum = 0, 0
    for i in range(len(A)): # 순서대로 리스트 A 원소들에 접근
        sum = A[i]
        for j in range(i+1,len(A)):
            if sum == M:  
                cnt += 1
                sum = 0
                break
            elif sum > M:
                sum = 0
                break
            else:         
                sum += A[j]
                if sum == M:
                    cnt += 1
                    sum = 0
                    break
    return cnt

# 마지막 원소는 for문 바로 밑에 있는 비교 if문이 실행되지 않기 때문에 else문에서 동일한 역할을 수행하는 if문을 다시 작성해주었다.

print(numSequence(A, M))



""" solution-2 """
N, M = map(int, input().split())
A = list(map(int, input().split()))

lt = 0
rt = 1
sum = A[0]
cnt = 0

while True:
    if sum < M:
        if rt < n:
            sum += A[rt]
            rt += 1
        else:
            break
    elif sum == m:
        cnt += 1
        sum -= A[lt]
        lt += 1
    else:
        sum -= A[lt]
        lt += 1
print(cnt)

