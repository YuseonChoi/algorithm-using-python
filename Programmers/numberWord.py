"""
<숫자 문자열과 영단어> 

https://programmers.co.kr/learn/courses/30/lessons/81301 

"""

""" solution-1 리스트 사용 """

string = ['zero','one','two','three','four','five','six','seven','eight','nine']
number = ['0','1','2','3','4','5','6','7','8','9']

def solution(s): 
    tmp = ''
    res  = ''
    for i in s:
        if i.isdigit():
            res += i
        else:
            tmp += i
            if tmp in string:
                res += number[string.index(tmp)]
                tmp = ''  # 다시 초기화
    return int(res)



""" solution-2 딕셔너리 사용 """

keys = ('zero','one','two','three','four','five','six','seven','eight','nine')
values = ('0','1','2','3','4','5','6','7','8','9')
dic = dict(zip(keys, values))

def solution(s):
    answer = ''
    word = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            word += i
            if word in keys:
                answer += dic[word]
                word = ''
    return int(answer)



""" solution-3 dic.items() 사용 """

keys = ('zero','one','two','three','four','five','six','seven','eight','nine')
values = ('0','1','2','3','4','5','6','7','8','9')
dic = dict(zip(keys, values))

def solution(s):
    answer = s
    for key, value in dic.items():
        answer = answer.replace(key, value)
    return int(answer)



""" solution-4 enumerate() 사용"""
words = ('zero','one','two','three','four','five','six','seven','eight','nine')

def solution(s):
    answer = s
    for idx, word in enumerate(words):
        answer = answer.replace(word, str(idx))  # idx가 정수형이므로 str로 바꿔줌
    return int(answer)