""" <보물> https://www.acmicpc.net/problem/1026 """

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
sum = 0
for i in range(len(b)):
    sum += a[i]*b[i]
print(sum)
