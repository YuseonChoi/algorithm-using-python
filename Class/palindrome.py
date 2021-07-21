""" 
<회문 문자열 검사> 

N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다. 단 회문을 검사할 때 대소문자를 구분하지 않는다.

"""

""" solution-1 파이썬 문자열 슬라이싱 이용 """

def checkPalindrome(str):
    if str[:] == str[::-1]:
        return 'YES'
    return 'NO'


N = int(input())

for i in range(N):
    s = input()
    print(f"#{i+1}",checkPalindrome(s.upper()))



""" solution-2 직접 구현 
    0 1 2 3 4
    l e v e l 
    원소의 개수가 5개이므로 (l,l),(e,e) 2번만 반복해주면 회문인지 판별이 가능하다. """

def checkPalindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[-1-i]:
            return 'NO'
    return 'YES'


N = int(input())

for i in range(N):
    s = input()
    print(f"#{i+1}",checkPalindrome(s.upper()))
