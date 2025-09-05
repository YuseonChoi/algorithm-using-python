""" <단어 변환> https://school.programmers.co.kr/learn/courses/30/lessons/43163 """

""" solution 1 - 내 풀이 """
# 현재 단어와 다른 단어의 문자열 차이 구하기
def diff_str(s1,s2):
    return sum(c1!=c2 for c1,c2 in zip(s1,s2))
    
# 문자열 차이가 1인 후보 단어 구하기
def find_word_one_diff(curr, words):
    return [word for word in words if diff_str(curr, word) == 1]
    
def dfs(curr, target, words, visited, depth):

    # 종료 조건 - 정답 발견
    if curr == target:
        return depth
    
    min_depth = float('inf')
    for i, word in enumerate(words):
        if not visited[i] and diff_str(curr, word) == 1:
            visited[i] = True
            result = dfs(word, target, words, visited, depth + 1)
            if result != -1:
                min_depth = min(min_depth, result)
            visited[i] = False
            
    return min_depth if min_depth != float('inf') else -1
                

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    depth = 0
    result = dfs(begin, target, words, visited, depth)
    
    return result if result != -1 else 0



""" solution 2,3 - HSK 풀이
- 2번은 DFS 방식 > 탐색 경로가 많으면 중복 재귀가 많아 비효율적
- 3번은 BFS 방식 > 최단 경로 보장 + 중복 탐색 없음 -> 훨씬 효율적
"""

def get_nstage(start, target, words, depth):
    if start == target:
        return depth
    
    min_stage = 100
    for w in words:
        if can_convert(start, w):
            nstage = get_nstage(w, target, words-set([w]), depth+1)
            min_stage = min(min_stage, nstage)
    
    return min_stage


def get_nstage2(start, target, words):
    stage = {w:0 for w in words}
    
    cur_words = [start]
    next_words = set(words)
    cur_stage = 1
    
    while next_words and (stage[target] == 0):
        candidate_words = []
        for cur_word in cur_words:
            for w in next_words:
                if can_convert(cur_word, w):
                    candidate_words.append(w)
                    stage[w] = cur_stage
            next_words -= set(candidate_words)
        cur_words = candidate_words
        cur_stage += 1
    
    return stage[target]


def can_convert(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
        if count > 1:
            return False
    return True if count == 1 else False
        

def solution(begin, target, words):
    words = set(words)
    
    if target not in words:
        return 0
    
    answer = get_nstage(begin, target, words, 0)
    if answer == 100:
        answer = 0
    
    # answer = get_nstage2(begin, target, words)
    
    return answer
