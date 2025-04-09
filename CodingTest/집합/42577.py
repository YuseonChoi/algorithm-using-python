""" [전화번호 목록] https://school.programmers.co.kr/learn/courses/30/lessons/42577# """

# solution 1 - 일부 test case 불통.. 이유가 뭘까..
def solution(phone_book):
    phone_set = set()
    phone_set.add(phone_book[0])
    for idx in range(1,len(phone_book)):
        for num in phone_set:
            phone_len = len(num)
            if phone_book[idx][:phone_len] == num:
                return False
    return True
        

# solution 2
def solution(phone_book):
    # 사전 순으로 정렬
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
        