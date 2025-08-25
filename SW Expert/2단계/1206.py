import sys
sys.stdin = open('input_1206.txt', 'r')

""" solution 1 - 내 풀이 """
for t in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2):
        if i == 2:
            max_rval = max(arr[i+1], arr[i+2])  # 오른쪽만 조망권 확인
            num_val = arr[i] - max_rval  # 조망권 확보된 세대수
            if num_val > 0: cnt += num_val
        elif i == (n-1)-2:
            max_lval = max(arr[i-1], arr[i-2])  # 왼쪽만 조망권 혹인
            num_val = arr[i] - max_lval
            if num_val > 0: cnt += num_val
        else:
            max_val = max(arr[i+1], arr[i+2], arr[i-1], arr[i-2])  # 좌우 조망권 확인
            num_val = arr[i] - max_val
            if num_val > 0: cnt += num_val

    print(f"#{t}", cnt)


""" solution 2 - 참고용 """
T = 10
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        mx = lst[i-2]
        for j in range(i-1, i+3):
            if j == i:
                continue
            else:
                if mx < lst[j]:
                    mx = lst[j]
        if lst[i] > mx:
            ans += lst[i] - mx
    print(f"#{test_case}", ans)
