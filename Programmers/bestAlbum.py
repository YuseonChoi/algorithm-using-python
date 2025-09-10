""" <베스트 앨범> https://school.programmers.co.kr/learn/courses/30/lessons/42579 """

from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_cnt = defaultdict(int)
    music_cnt = defaultdict(int)
    
    for i in range(len(genres)):
        genre_cnt[genres[i]] += (plays[i])
        music_cnt[i] += plays[i]
        
    genre_sort = sorted(genre_cnt, key=genre_cnt.get, reverse=True)
    music_sort = sorted(music_cnt, key=music_cnt.get, reverse=True)
    
    for g in genre_sort:
        cnt = 0
        for m in music_sort:
            if genres[m] == g:
                cnt += 1
                if cnt > 2:
                    break
                answer.append(m)
                
    return answer

