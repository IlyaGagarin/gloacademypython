# -- coding: utf-8 
x=int(input())
x1=x//1000
x2=x%1000//100
x3=x%1000%100//10
x4=x%1000%100%10
print ('У числа ', x, 'максимальная цифра равна ', max(x1, x2, x3, x4))