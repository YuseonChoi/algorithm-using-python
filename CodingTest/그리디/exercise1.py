"""
[거스름돈 주기]
당신은 상점에서 계산을 마치고 거스름돈을 돌려받아야 합니다.
다만 거스름돈을 최소한의 화폐수로 받고 싶어졌습니다.
거스름돈 amount가 있을 때 화폐 단위 [1,10,50,100]을 최소한으로
사용한 화폐 리스트를 반환하는 함수를 반환하세요.
"""

# solution 1
def solution(amount):
    answer = []
    while amount != 0:
        if amount >= 100:
            tmp = amount // 100
            amount = amount - tmp*100
            for i in range(tmp):
                answer.append(100)
                
        if amount >= 50:
            tmp = amount // 50
            amount = amount - tmp*50
            for i in range(tmp):
                answer.append(50)
                
        if amount >= 10:
            tmp = amount // 10
            amount = amount - tmp*10
            for i in range(tmp):
                answer.append(10)
                
        if amount >= 1:
            tmp = amount // 1
            amount = amount - tmp*1
            for i in range(tmp):
                answer.append(1)
    
    return answer



# solution 2
def solution(amount):
    denominations = [100,50,10,1]
    change = []
    for coin in denominations:
        # 현재 화폐 단위로 최대한 거슬러 줄 수 있는 동전의 갯수를 구함
        count = amount // coin
        change.extend([coin]*count)
        # 정산이 완료된 거스름돈을 제외함
        amount %= coin
    return change
    

# test case 1
amount = 123

# test case 2
amount = 350

print(solution(amount))