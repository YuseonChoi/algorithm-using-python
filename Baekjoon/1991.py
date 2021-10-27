""" <트리 순회> https://jm-codingmemo.tistory.com/22 

[input]
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

[output]
ABDCEFG
DBAECFG
DBEGFCA

"""

import sys
input = sys.stdin.readline
n = int(input())
tree = {}

for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회 - 루트, 왼쪽 자식, 오른쪽 자식
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회 - 왼쪽 자식, 루트, 오른쪽 자식
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위 순회 - 왼쪽 자식, 오른쪽 자식, 루트
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')