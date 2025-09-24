""" <최소 직사각형> https://school.programmers.co.kr/learn/courses/30/lessons/86491 """

""" solution 1 - 내 풀이 """

def solution(sizes):
    
    a_lst = []  # (가로/세로) 구하기
    
    for i,j in sizes:
        a_lst.append(i)
        a_lst.append(j)
    max_num1 = max(a_lst)
    
    b_lst = []  # 나머지 값(세로/가로) 찾기
    c_lst = []  # 최댓값이 여러 개 있을 때 후보군 처리
    
    for i,j in sizes:
        if i == max_num1:
            c_lst.append(j)
            continue
        elif j == max_num1:
            c_lst.append(i)
            continue
        else:
            min_num = min(i,j)
            b_lst.append(min_num)
            
    b_lst.extend(c_lst)  # 후보군 병합  -> 쓸데 없이 조건문 넣으면 런타임 에러남..
        
    max_num2 = max(b_lst)
    
    return max_num1 * max_num2



""" solution 2 - 다른 사람 풀이 """

def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col