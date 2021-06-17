# -- coding: utf-8 
n = int(input())
minimum = int(input())
maximum = int(input())
if n>=2:
    for i in range (n-2):
        number=int(input())
        if number>maximum:
            maximum=number
        else:
            number=minimum
print ('Минимум равен ', minimum)
print ('Максимум равен ', maximum)
            
     



        
    
        


        
        