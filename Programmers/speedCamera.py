""" <단속 카메라> https://school.programmers.co.kr/learn/courses/30/lessons/42884 """

def solution(routes):
    answer = []
    
    # routes -> [진입 시점, 진출시점]
    # 진출 시점이 빠른 순으로 정렬
    
    routes = sorted(routes, key=lambda x:x[1])
    last_camera = -300001
    
    for route in routes:
        # 현재 카메라로 커버 불가능하다면
        if last_camera < route[0]:
            last_camera = route[1]
            answer.append(last_camera)

    return len(answer)