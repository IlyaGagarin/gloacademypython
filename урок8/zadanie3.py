# -- coding: utf-8 
number=int(input())
number1=number
total=0
while number!=0:
    last_digit = number % 10
    total = total + last_digit
    number=number//10
if number1%total==0:
    print ('YES')
else:
    print ('NO')

            
     



        
    
        


        
        