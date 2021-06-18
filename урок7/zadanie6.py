# -- coding: utf-8 
number=int(input())
total=0
for i in range (number):
    if (number % 10) == 1 or number % 10 == 3 or number % 10 == 7:
        total = total + number
print (total)
        