# -- coding: utf-8 

number1, number2= int(input()), int(input())
if number1<number2:
    for i in range(number1, number2+1):
        if i%2==0:
            print (i)
else:
    for i in range(number2, number1+1):
        if i%2==0:
            print (i)    