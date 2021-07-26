# s1 = [1,2,3,4,5]
# s1.extend(s1*2000)
# print(len(s1))

# s2 = [ 2, 1, 2, 3, 2, 4, 2, 5]
# s2.extend(s2*1250)
# print(len(s2))

# s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# s3.extend(s3*1000)
# print(len(s3))

dic = {'s1':1, 's2':2,'s3':2}
res = max(dic.values())
for key, value in dic.items():
    if res == value:
        print(key)