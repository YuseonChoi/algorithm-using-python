import sys
sys.stdin = open("input_2001.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    ans = 0
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 시작 좌표 설정
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            cnt = 0
            # 시작좌표부터 탐색 돌입
            for si in range(i, i + M):
                for sj in range(j, j + M):
                    cnt += arr[si][sj]

            if ans < cnt:
                ans = cnt

    print(f"#{test_case}", ans)
