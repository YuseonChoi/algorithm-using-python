""" <디스크 컨트롤러> https://school.programmers.co.kr/learn/courses/30/lessons/42627#

- 요청시간이 아직 되지 않는 작업은 선택할 수 없음
"""

import heapq

def solution(jobs):
    jobs.sort()  # 요청시간 기준 정렬
    n = len(jobs)
    time = 0
    answer = 0
    job_lst = []
    i = 0

    while i < n or job_lst:
        # 현재 시간까지 들어온 작업만 힙에 넣기!
        while i < n and jobs[i][0] <= time:
            t_ask, t_spend = jobs[i]
            heapq.heappush(job_lst, (t_spend, t_ask))
            i += 1

        if job_lst:
            t_spend, t_ask = heapq.heappop(job_lst)
            time += t_spend
            answer += (time - t_ask)

        else:
            time = jobs[i][0]

    return answer // n
