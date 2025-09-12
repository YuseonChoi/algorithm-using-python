""" <단어 변환> https://school.programmers.co.kr/learn/courses/30/lessons/43163 """

""" solution 1 - DFS 풀이 """
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



""" solution 2 - BFS 풀이 """

def find_word_one_diff(curr, word):
    cnt = 0
    for c1, c2 in zip(curr, word):
        if c1 != c2:
            cnt += 1
    return cnt


def bfs(start, target, words):
    depth = {word:0 for word in words}
    
    curr_words = [start]
    next_words = set(words)
    curr_depth = 1
    
    # 아직 방문하지 않은 단어가 있고 target에 도달하지 않은 경우 반복
    while next_words and (depth[target]==0):
        candidate_words = []
        for curr_word in curr_words:
            for next_word in next_words:
                if find_word_one_diff(curr_word, next_word) == 1:
                    candidate_words.append(next_word)
                    depth[next_word] = curr_depth  # 현재 depth 기록
            next_words -= set(candidate_words)
        curr_words = candidate_words
        curr_depth += 1
        
    return depth[target]
        

def solution(begin, target, words):

    if target not in words:
        return 0
    
    answer = bfs(begin, target, words)
    
    return answer
