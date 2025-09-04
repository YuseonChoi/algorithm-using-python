"""
쉬운 문제인데 효율성 생각하느라 애먹음..
딕셔너리, li
"""

def solution(A):
    dict_cnt = {}
    for a in A:
        dict_cnt[a] = dict_cnt.get(a, 0)+1  # 값이 있으면 원래 값, 없으면 0 반환
    result = [a for a in A if dict_cnt[a]==1]
    if len(result) == 0:
        return -1
    return result[0]