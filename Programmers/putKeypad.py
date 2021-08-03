"""
<키패드 누르기> 

https://programmers.co.kr/learn/courses/30/lessons/67256

"""

""" solution-1 dict 사용 """

def solution(numbers, hand):
    # 왼쪽, 오른쪽 포인터
    L_pt = '*'
    R_pt = '#'
    answer = ''

    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            L_pt = i

        elif i in [3,6,9]:
            answer += 'R'
            R_pt = i

        elif i in [2,5,8,0]:
            # 왼쪽, 오른쪽 거리
            L_dt = distance(L_pt, i)
            R_dt = distance(R_pt, i)
            if L_dt < R_dt:
                answer += 'L'
                L_pt = i
            elif R_dt < L_dt:
                answer += 'R'
                R_pt = i
            elif L_dt == R_dt:
                if hand == 'right':
                    answer += 'R'
                    R_pt = i
                else:
                    answer += 'L'
                    L_pt = i

    return answer


def distance(pt, target):
    pt = str(pt)
    target = str(target)
    pt_x, pt_y = keypad[pt]
    target_x, target_y = keypad[target]
    return abs(pt_x - target_x) + abs(pt_y - target_y)
    

global keypad
keypad = {'1':(0,0), '2':(0,1), '3':(0,2),
          '4':(1,0), '5':(1,1), '6':(1,2),
          '7':(2,0), '8':(2,1), '9':(2,2),
          '*':(3,0), '0':(3,1), '#':(3,2)}

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))



""" solution-2 거리를 모두 계산 """

def solution(numbers, hand):
    l = 10
    r = 11
    answer = ""
    p = [[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
         [4, 0, 1, 2, 0, 2, 3, 0, 3, 4],
         [3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
         [4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
         [3, 0, 2, 3, 0, 1, 2, 0, 2, 3],
         [2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
         [3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
         [2, 0, 3, 4, 0, 2, 3, 0, 1, 2],
         [1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
         [2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
         [1, 0, 4, 5, 0, 3, 4, 0, 2, 3],
         [1, 5, 4, 0, 4, 3, 0, 3, 2, 0]]
    for i in numbers:
        if i in [1, 4, 7]:
            l = i
            answer += "L"
        elif i in [3, 6, 9]:
            r = i
            answer += "R"
        else:
            if p[l][i] < p[r][i]:
                l = i
                answer += "L"
            elif p[l][i] > p[r][i]:
                r = i
                answer += "R"
            elif hand == "left":
                l = i
                answer += "L"
            else:
                r = i
                answer += "R"
    return answer