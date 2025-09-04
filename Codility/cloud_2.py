"""
- 숫자 N을 입력받아 주어진 조건을 달성하는 함수 작성
- 길이가 N인 A 배열이 있고, A 배열 안의 원소로 절댓값이 N이하의 정수가 원소가 될 수 있음
- A 안의 모든 원소는 유일한 절댓값을 가져야 함
- A안의 원소 X는 X나 -X로 배열에 다시 등장하면 안됨
- A배열 안의 모든 원소 합은 0이 되어야 함

    예시를 주자면 N=4일 때,
    [-1,0,4,-3] 또는 [0,-1,4,-3] 하나라도 리턴해야 함

    또 예시를 주자면 N=5일 떄, 
    [-4,-2,5,0,1] 또는 [0,1,5,-2,-4]
    
"""


def build_array(N: int):
    num_lst = list(range(-N, N + 1)) 
    result = []

    def dfs(path, flag_abs, total):
        if len(path) == N:
            if total == 0:
                return path
            return None
        
        for n in num_lst:
            if abs(n) in flag_abs:
                continue
            new_path = path + [n]
            
            new_used = set(flag_abs) 
            new_used.add(abs(n))

            new_total = total + n
            
            ans = dfs(new_path, new_used, new_total)
            if ans:
                return ans
        return None

    return dfs([], set(), 0)

print(build_array(4))