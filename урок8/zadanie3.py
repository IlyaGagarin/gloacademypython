# -- coding: utf-8 
number=int(input())
maximum=0
minimum=9
while number != 0:
    last_digit = number % 10
    number=number//10
    if maximum<last_digit:
        maximum=last_digit
    if last_digit<minimum:
        minimum=last_digit
    
print ('Максимальная цифра равна ', maximum)
print ('Минимальная цифра равна ', minimum)
            
     



        
    
        


        
        