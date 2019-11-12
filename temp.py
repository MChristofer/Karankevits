#Задача 1
n=int(input())
i=1
while i**2<=n:
    print(i**2)
    i+=1


#Задача 2
n=int(input())
i=2
while n % i !=0:
    i+=1
print(i)


#Задача 3
n=int(input())
z=0
i=1

while i<=n:
    i=i*2
    z+=1
print(z-1,i-i//2)


#Задача 4
x=int(input())
y=int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)


#Задача 5
x=int(input())
p=int(input())
y=int(input())
i = 0
while x < y:
    x += x*(p / 100)
    i += 1
print(i)


#Задача 6
import random
a=1

b = 0
while a != 0:
    a=random.randint(2,20)
    print(a)
    b = b+1
    
print(b)


#Задача 7
import random
x=1
sum=0
while x!=0:
    x=random.randint(0,20)
    sum+=x
    print(x)
print('Сумма -',sum)    


#Задача 8
import random
x=1
y=0
sum=0
max=0
while x!=0:
    x=random.randint(0,10)
    print('число ',x)
    sum+=x
    y+=1
    if max<=x:
        max=x
print('Среднее: ',sum/y,"Максимальное: ",max)


#Задача 9
import random
x=1
y=0
max=0
index=0
while x!=0:
    x=random.randint(0,10)
    print(x)
    y+=1
    if max<=x:
        max=x
        index=y
print('Индекс-',index,'число-',max)


#Задача 10
import random
x=1
y=0
max=0
y=0
while x!=0 and y<20:
    x=random.randint(0,20)
    print(x)
    y+=1
    if max<=x:
        max=x
    
print('max-',max,'len-',y)

#Таблица умножения
x=1
y=1
while y<=10:
    print(x,'*',y,'=',x*y)
    x+=1 
    while x>10:
        x=1
        y+=1
        print('='*15)

        
        
for x in range(1,11):
    for y in range(1,11):
        print('*',end='')
    print('')
    
        
        
        

for x in range (1,11):    
    for y in range(1,11):
        print ('{0:>3}'.format(y*x),end=' ')
    print()
        
        
        
        
        
'координаты:{latitude},{longitude}'.format(latitude='37.24N',longitude='-115.81W')

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


