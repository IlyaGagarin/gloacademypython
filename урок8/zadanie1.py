# -- coding: utf-8 
number=int(input())
total=0
while number != 0:
    last_digit = number % 10
    if last_digit==5:
        total += 1
    number = number//10
    
print (total)
            
     



        
    
        


        
        