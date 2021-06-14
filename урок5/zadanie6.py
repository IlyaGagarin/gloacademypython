# -- coding: utf-8 
x=int(input())
if x<0 or x>36:
    print ('Ошибка!')
elif x==0:
    print ('Зеленый')
elif 1<=x<=10 and (x%2)==0:
    print ('Черный')
elif 11<=x<=18 and (x%2)!=0:
    print ('Черный')
elif 19<=x<=28 and (x%2)==0:
    print ('Черный')
elif 29<=x<=36 and (x%2)!=0:
    print ('Черный')
else :
    print ('Красный')




    