"""
[부분 배낭 문제]
무게와 가치가 있는 짐 items와 배낭 weight_limit이 주어질 때,
부분 배낭 문제 (짐을 쪼갤 수 있음)를 푸는 함수를 작성하세요.
"""

# 각 물건의 단위 무게당 가치를 계산하여 items 리스트에 추가
def calculate_unit_value(items):
    for item in items:
        item.append(item[1]/item[0])
    return items


# 단위 무게당 가치가 높은 순으로 물건을 정렬
def sort_by_unit_value(items):
    items.sort(key=lambda x: x[2], reverse=True)
    return items


def knapsack(items, weight_limit):
    total_value = 0  # 선택한 물건들의 총 가치를 저장하는 변수
    remaining_weight = weight_limit  # 남은 무게의 한도를 저장하는 변수

    for item in items:
        if item[0] <= remaining_weight:
            # 물건을 통째로 선택
            total_value += item[1]
            remaining_weight -= item[0]
            print(total_value)
        else:
            # 남은 무게 한도가 물건의 무게보다 작으면 쪼개서 일부분만 선택
            fraction = remaining_weight / item[0]
            total_value += item[1] * fraction
            print(item[1]*fraction)
            break
    return total_value


def solution(items, weight_limit):
    items = calculate_unit_value(items)
    items = sort_by_unit_value(items)
    return round(knapsack(items, weight_limit),2)
    

# test case 1
items = [[10,19],[7,10],[6,10]]
weight_limit = 15

# test case 2
items = [[10,60],[20,100],[30,120]]
weight_limit = 50

print(solution(items, weight_limit))