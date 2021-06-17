# -- coding: utf-8 
number=int(input())
flag = 1
for i in range (1, number+1):
    if i % 10 == 2 or i % 10 == 9:
        flag *= i
if flag == 1:
    print (0)
else: 
    flag!=0
    print (flag)