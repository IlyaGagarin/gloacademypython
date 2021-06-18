counter=0
n=int(input())
for i in range(n):
    number=int(input())
    if number%2==0:
        counter+=1
if counter==0:
    print ('YES')
else:
    print ('NO')