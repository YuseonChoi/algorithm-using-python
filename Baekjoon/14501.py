""" <퇴사> https://www.acmicpc.net/problem/14501 """

""" 틀린 풀이, Greedy적 접근법으로는 최적해를 보장하지 못함, 반례는 아직 못찾음 """
N = int(input())
lst = []
aval = [0] * (N+1)  # 스케줄 유효성 검증, (0: 비어있음, 1: 이미 다른 스케줄이 있음)
ans = []  # 유효한 스케줄의 가격
for i in range(1, N+1):
    T, P = map(int, input().split())
    lst.append((i, T, P))

lst = sorted(lst, key=lambda x:x[1], reverse=False)  # time 순으로 오름차순 정렬
lst = sorted(lst, key=lambda x:x[2], reverse=True)  # price 순으로 내림차순 정렬

for n in range(1, N+1):
    idx = lst[n-1][0]
    time = lst[n-1][1]
    price = lst[n-1][2]
    flag = True  # 유효성 체크
    for j in range(idx, idx+time):
        if j <= N:
            if aval[j] == 1:  # 이미 스케줄이 있다면
                flag = False
        else:
            flag = False

    if flag == True:
        ans.append(price)
        for j in range(idx, idx+time):  # 스케줄 확정 후 유효성 없앰
            if j <= N:
                aval[j] = 1
        # print(idx, time, price)

print(sum(ans))


""" solution 1 - 백트래킹 """

def dfs(n,sm):
    global ans
    # [1] 종료 조건 : 가능한 n(종료)에 관련된 것으로 정의
    if n>= N:
        ans = max(ans, sm)
        return

    # [2] 하부 호출 : 화살표 개수만큼 호출
    if n+T[n] <= N: # 상담하는 경우(퇴사일 전 완료 가능할 것!)
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)  # 상담하지 않는 경우(항상 가능), 조건 붙이면 망함

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

ans = 0
# 제일 이전 함수를 불러줌
dfs(0, 0)
print(ans)





