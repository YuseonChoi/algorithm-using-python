"""
[1부터 N까지 숫자 중 합이 10이 되는 조합 구하기]
정수 N을 입력받아 1부터 N까지의 숫자 중에서 합이 10이 되는
조합을 리스트로 반환하는 함수를 작성하세요.
"""

def backtrack(sum, selected_nums, start, N, results):
    # 합이 10이 되면, 숫자를 더 추가할 필요가 없으므로 백트래킹
    if sum == 10:
        results.append(selected_nums)  # selected_nums는 현재 숫자 조합 리스트
        return
    
    for i in range(start, N+1):
        if sum + i <= 10:
            backtrack(
                sum+i, selected_nums+[i], i+1, N, results
            )  # 현재 숫자 이전은 체크할 필요 없음
    
    
def solution(N):
    results = []  # sum이 10이 되는 조합 결과를 담는 리스트
    backtrack(0,[],1,N,results)
    return results


# test case 1 - [[1,2,3,4],[1,4,5],[2,3,5]]
N=5

# test case 2 - []
N=2

# test case 3 - [[1,2,3,4],[1,2,7],[1,3,6],[1,4,5],[2,3,5],[3,7],[4,6]]
N=7

print(solution(N))


"""
유망 함수 조건 파악하는 게 중요한 문제.
- 조합한 숫자의 합이 10이 되면 해당 조합을 결과 리스트에 추가하기
- 조합한 숫자의 합이 10보다 크면 백트래킹(유망 함수 조건)
"""