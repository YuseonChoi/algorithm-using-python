def solution(P, C):
    num_match = P//2
    if num_match >= C:
        return C
    return num_match