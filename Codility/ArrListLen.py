def solution(A):
    ans = 0
    i = 0
    while True:
        if A[i] == -1:
            break
        else:
            ans += 1
            i = A[i]
    ans += 1

    return ans