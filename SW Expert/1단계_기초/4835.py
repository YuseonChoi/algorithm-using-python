import sys
sys.stdin = open("input_4835.txt", "r")

""" solution 1 - 기본 풀이 """
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 정수의 개수, 구간의 개수
    max_val = 0
    min_val = N*10000
    arr = list(map(int, input().split()))

    for i in range(0, N-M+1):
        temp = 0
        for j in range(i, i+M):
            temp += arr[j]

        if temp >= max_val:
            max_val = temp

        if temp <= min_val:
            min_val = temp

    print(f"#{test_case} {max_val-min_val}")


""" solution 2 - 한 번 본 데이터를 재사용하여 실행 시간 줄이기 """
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # 정수의 개수, 구간의 개수
    arr = list(map(int, input().split()))

    sm = max_val = min_val = sum(arr[0:M])
    for i in range(M, N):
        sm += arr[i]
        sm -= arr[i-M]

        if sm < min_val:
            min_val = sm

        if sm > max_val:
            max_val = sm

    print(f"#{test_case} {max_val-min_val}")