""" <단어 변환> https://school.programmers.co.kr/learn/courses/30/lessons/43163 """

""" solution 1 - 내 풀이 """
def find_word_one_diff(curr, word):
    cnt = 0
    for c1, c2 in zip(curr, word):
        if c1 != c2:
            cnt += 1
    return cnt

def dfs(curr, target, words, visited, depth):
    if curr == target:
        return depth
    
    min_depth = 100
    for idx, word in enumerate(words):
        if not visited[idx] and find_word_one_diff(curr, word) == 1:
            visited[idx] = True
            result = dfs(word, target, words, visited, depth + 1)
            min_depth = min(min_depth, result)
            visited[idx] = False  # 백트래킹, 이후 다시 방문 가능하게 고치기
            
    return min_depth
        

def solution(begin, target, words):
    depth = 0
    if target not in words:
        return 0
    
    visited = [False]*len(words)
    result = dfs(begin, target, words, visited, depth)

    return 0 if result == 100 else result



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
