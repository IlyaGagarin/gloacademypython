# -- coding: utf-8 
k=int(input()) #количество задач
m=int(input()) #количество задач в день
if k%m==0:
    print (k/m)
else :
    print ((k//m)+1)
    