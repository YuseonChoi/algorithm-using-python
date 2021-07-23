""" 
<두 리스트 합치기>

오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.

[input]
3
1 3 5
5 
2 3 6 7 9

[output]
1 2 3 3 5 6 7 9

"""

""" solution-1 """

N = int(input())
N_list = map(int, input().split())
M = int(input())
M_list = map(int, input().split())

res = []
res.extend(N_list)
res.extend(M_list)
print(' '.join(map(str,sorted(res))))
# list.sort() 메서드는 목록을 제자리에서 수정하고 None을 반환한다.
# sorted(list)를 써주면 정렬된 목록을 반환할 수 있다.



""" solution-2 배열만 사용 """

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

res = [None for _ in range(N+M)]
i,j,k = 0,0,0


while i < N and j < M: 
    if N_list[i] < M_list[j]:
        res[k] = N_list[i]
        i+=1
        k+=1
    elif N_list[i] > M_list[j]:
        res[k] = M_list[j]
        j += 1
        k += 1
    else:
        res[k],res[k+1] = N_list[i],M_list[j]
        i+=1
        j+=1
        k+=2

if i < N:
    for n in range(i,N):
        res[k] = N_list[n]
        k+=1

if j < M:
    for n in range(j,M):
        res[k] = M_list[n]
        k+=1


print(' '.join(map(str,res)))



""" solution-3 문자열 슬라이싱 이용 """

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

res = []
i,j = 0,0
while i < N and j < M:
    if N_list[i] <= M_list[j]:
        res.append(N_list[i])
        i+=1
    else:
        res.append(M_list[j])
        j+=1

if i < N:
    res += N_list[i:]
if j < M:
    res += M_list[j:]

print(' '.join(map(str,res)))