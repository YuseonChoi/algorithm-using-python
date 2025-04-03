""" [다단계 칫솔 판매] https://school.programmers.co.kr/learn/courses/30/lessons/77486 """

# solution 1 - 시간 초과 ㅠㅠ
class Node:
    def __init__(self, key, parent):
        self.value = key
        self.parents = parent
        
class Corp:
    def __init__(self):
        self.root = "Center"
        self.nodes = {}
    
    # 부모, 자식 관계 정립
    def set_dependency(self,enr,ref):
        parent = self.root if ref == "-" else ref 
        self.nodes[enr] = Node(enr, parent)
        
    def cal_amount(self,sel,amo,total):
        curr = self.nodes[sel]
        amo = amo*100
        while curr.parents != 'Center':
            curr_amo = int(amo-int(amo*0.1))
            amo = amo*0.1
            total[curr.value]+=curr_amo
            curr = self.nodes[curr.parents]
        curr_amo = int(amo-int(amo*0.1))
        amo = amo*0.1
        total[curr.value]+=curr_amo
        return total


def solution(enroll, referral, seller, amount):
    total={}
    corp = Corp()
    for i in range(len(enroll)):
        corp.set_dependency(enroll[i],referral[i])
        total[enroll[i]]=0

    for j in range(len(seller)):
        corp.cal_amount(seller[j],amount[j],total)   
        
    return list(total.values())


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

print(solution(enroll, referral, seller, amount))



# solution 2
def solution(enroll, referral, seller, amount):
    # key값으로 enroll, value로 referral을 가지는 parent dict 생성
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}
    
    for i in range(len(seller)):
        money = amount[i]*100
        cur_name = seller[i]
        # 판매자로부터 차례대로 상위 노드로 이동하며 이익 분배
        while money > 0 and cur_name != "-":
            total[cur_name] += money - money//10
            cur_name = parent[cur_name]
            # 현재 판매자를 기준으로 분배금을 계산하기 위해 업데이트
            money //=10
    
    return list(total.values())



# solution 3 - 시간 초과
class Node:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.parent = None

def solution(enroll, referral, seller, amount):
    answer = []
    nodes = {
        "center": Node("center")
    }

    # 부모, 자식 트리 구성
    for a, b in zip(enroll, referral):
        if b == "-":
            nodes[a] = Node(a)
            nodes[a].parent = nodes["center"]
        else:
            nodes[a] = Node(a)
            nodes[a].parent = nodes[b]

    for child, cost in zip(seller, amount):
        cost = cost * 100
        while True:
            nodes[child].money += cost - cost // 10
            child = nodes[child].parent.name
            cost = cost // 10

            if child == "center":
                break

    for name in enroll:
        answer.append(nodes[name].money)

    return answer




"""
파이썬 클래스를 이용해 노드를 생성하여 부모 정보를 저장하려고 했지만,
dict 자료형에 비해 처리 시간이 오래 걸린다는 단점이 있었음.
도전은 좋았다, 하지만, 웬만하면 빠른 걸 쓰도록 하자.
"""