""" <오픈채팅방> 
https://programmers.co.kr/learn/courses/30/lessons/42888 

[input]
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

[output]
["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

"""

""" solution-1 시간초과 """

def solution(record):
    res = list()   # return 출력문
    log1 = list()  # Leave 포함
    log2 = list()  # Leave 불포함
    tmp = list()

    for i in record:
        tmp = i.split()
        log1.append(tmp) 
        if tmp[0] != "Leave":
            tmp = i.split()
            log2.append(tmp)
            

    # 고유한 아이디
    id = set()
    for i in range(len(log2)):
        id.add(log2[i][1])


    # 딕셔너리 생성 {id : nickname} - 검색 편이성을 위해 생성해줌
    dic = {} 

    for i in id:
        for j in range(len(log2)):
            if i in log2[j]:
                dic[i] = log2[j][2]


    for i in range(len(log1)):
        if log1[i][0] == 'Enter':
            res.append(f"{dic[log1[i][1]]}님이 들어왔습니다.")
        elif log1[i][0] == 'Leave':
            res.append(f"{dic[log1[i][1]]}님이 나갔습니다.")

    return res



""" solution-2 코드 개선 """

def solution(record):
    res = []
    dic = {}

    for i in record:
        tmp = i.split()
        if len(tmp) == 3:
            dic[tmp[1]] = tmp[2]

    for i in record:
        tmp = i.split()
        if tmp[0] == 'Enter':
            res.append(f"{dic[tmp[1]]}님이 들어왔습니다.")
        elif tmp[0] == 'Leave':
            res.append(f"{dic[tmp[1]]}님이 나갔습니다.")

    return res



""" solution-3 매우 간편한 풀이 """

def solution(record):
    user_id = {i.split()[1]:i.split()[-1] for i in record if i.startswith('Enter') or i.startswith('Change')}  # 딕셔너리 생성
    return [f'{user_id[i.split()[1]]}님이 들어왔습니다.' if i.startswith('Enter') else f'{user_id[i.split()[1]]}님이 나갔습니다.' for i in record if not i.startswith('Change')]


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))


