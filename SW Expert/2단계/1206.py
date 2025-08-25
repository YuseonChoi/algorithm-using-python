import sys
sys.stdin = open('input_1206.txt', 'r')

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
