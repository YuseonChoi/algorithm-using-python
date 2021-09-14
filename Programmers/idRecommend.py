""" <신규 아이디 추천> https://programmers.co.kr/learn/courses/30/lessons/72410 """

""" solution-1 파이썬 내장 함수 이용 """

def solution(new_id):
    str = ''
    # 1단계 - 대문자를 소문자로 치환
    new_id = new_id.lower()
    for i in new_id:
        # 2단계 - 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자를 제거
        if i.isalpha() or i.isdigit() or i in ['-','_','.']:
            # 3단계 - 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환
            if i == '.' and str and str[-1] == '.':
                continue
            str += i
            
    # 4단계 - 마침표(.)가 처음이나 끝에 위치한다면 제거
    if str[0] == '.':
        if len(str) > 1:
            str = str[1:]
        else:
            str = '.'
    if str[-1] == '.':
        str = str[:-1]
    
    # 5단계 - 빈 문자열이라면, "a"를 대입
    if not str:
        str += 'a'
        
    # 6단계 - 문자열 길이가 16자 이상이면, 첫 15개 문자를 제외한 나머지를 제거
    if len(str) >= 16:
        str = str[:15]
        if str[-1] == '.':
            str = str[:-1]
        
    # 7단계 - 문자열 길이가 2자 이하면, 길이가 3이 될 때까지 마지막 문자 반복
    while len(str) < 3:
        str += str[-1]
    
    return str



""" solution-2 정규표현식 이용 

re.sub(정규 표현식, 치환 문자 , 대상 문자열)

정규 표현식 - 검색 패턴을 지정
치환 문자 - 변경하고 싶은 문자
대상 문자열 - 검색 대상이 되는 문자열

"""

import re

def solution(new_id):
    str = new_id
    # 1단계 - 대문자를 소문자로 치환 
    str = str.lower()

    # 2단계 - 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자를 제거
    str = re.sub('[^a-z0-9\-_.]', '', str)

    # 3단계 - 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환
    str = re.sub('\.+', '.', str)

    # 4단계 - 마침표(.)가 처음이나 끝에 위치한다면 제거
    str = re.sub('^[.]|[.]$', '', str)

    # 5단계 - 빈 문자열이라면, "a"를 대입
    # 6단계 - 문자열 길이가 16자 이상이면, 첫 15개 문자를 제외한 나머지를 제거
    str = 'a' if len(str) == 0 else str[:15]

    # 슬라이싱 이후 마지막이 마침표인 경우 처리
    str = re.sub('[.]$', '', str)

    # 7단계 - 문자열 길이가 2자 이하면, 길이가 3이 될 때까지 마지막 문자 반복
    str = str if len(str) > 2 else str + "".join([str[-1] for i in range(3-len(str))])

    return str


""" <참고> 

* 정규표현식 패턴
https://highcode.tistory.com/6
https://yurimkoo.github.io/analytics/2019/10/26/regular_expression.html

"""