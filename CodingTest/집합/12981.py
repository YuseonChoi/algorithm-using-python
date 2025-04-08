""" [영어 끝말잇기] https://school.programmers.co.kr/learn/courses/30/lessons/12981 """

# solution 1
def solution(n, words):
    word_list = []
    for idx, word in enumerate(words):
        # 첫 단어가 아닌 경우
        if idx > 0:
            # 현재 단어가 단어 리스트에 포함되어 있지 않은 새로운 단어 & 앞 단어의 마지막 문자로 시작
            if not word in word_list and (word_list[-1])[-1] == word[0]:
                word_list.append(word)
            else:
                return [(idx%n)+1, (idx)//n+1] 
        # 첫 단어인 경우
        else:
            word_list.append(word)
    return [0,0]
            
            
# solution 2
def solution(n, words):
    used_words = set()  # 이미 사용한 단어를 저장하는 set
    prev_words = words[0][0]  # 이전 단어의 마지막 글자 (초깃값은 첫 글자로 설정)
    
    for i, word in enumerate(words):
        # 이미 사용한 단어거나 첫 글자가 이전 단어와 일치하지 않으면
        if word in used_words or word[0] != prev_words:
            # 탈락하는 사람의 번호와 차례를 반환
            return [(i%n)+1, (i//n)+1]
        used_words.add(word)
        prev_words = word[-1]
        
    return [0,0]
            