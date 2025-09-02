def solution(A):
    # Implement your solution here
    dict_cnt = {}
    for a in A:
        dict_cnt[a] = dict_cnt.get(a, 0)+1
    result = [a for a in A if dict_cnt[a]==1]
    if len(result) == 0:
        return -1
    return result[0]