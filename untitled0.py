#Примеры применения циклов FOR (1)
'''-------------------------------'''
for linn in 'narva', 'toila', 'oru':
    print(linn)
print()        

i=1
for linn in 'narva', 'toila', 'oru':
    print(i,linn)
print()


for i in 1,2,3,'üks',"kaks", 'kolm':
    print(i)
print()
'''-------------------------------'''
sum=0
for i in 10,12,13,20,5,8:
    sum=sum+i
    print(i)
print('Сумма всех чисел =', sum)
print('-'*20)      
'''-------------------------------'''
#Примеры применения циклов FOR (2)
#range - интервал
a='Tere tulemast'
for i in range(5):
    print(a)
print('')

a='Tere'
for i in range(5):
    print(i,a)
print('')

a='Привет'
for i in range(1,5):
    print(i,a)
print('')

a='Добро пожаловать!'
for i in range(1,6):
    print(i,a)
print('')

for k in range(2,5):
    print('k=',k)
print('Цикл выполнен \n')

for i in range(1,100,10):
    print(i)
print('')
#Эквивалентно
print('='*25)
for i in range(0,21,2):
    print(i)
print('='*25)
for i in range(21):
    if i%2==0:
        print(i)
print()
'''-------------------------------'''   
#Циклы и печать
#Настройка функции print()
print(1,2,3)
print(4,5,6)  
print(1,2,3, sep=', ',end='. ')
print(4,5,6, sep=', ',end='. ')
print()
print(1,2,3, sep='', end='--')
print(4,5,6, sep=' * ', end='.')
print()
print('-'*20)
#применение циклов
a=3
for i in range(5):
    print(a,'', end='')
print('')

a=10
for i in range(5):
    print(a,'', end='')
print('Tere')

for i in range(10):
    print('-',i,end='')
print()
print('-'*20)

print('Сумма чисел от 1 до 5')
print('Число сумма')
sum=0
n=5
for i in range(1,n+1):
    sum+=1
    print(i,'\t', sum) #Сумма с накоплением
print('-'*20)    
print('Итого сумма =',sum)
'''----------------------------------------''' 
import random
max=0
arv=random.randint(0,50)
print('Последовательность случайных чисел:')

while arv!=0:
    print(arv)
    if max<arv:
        max=arv
    arv=random.randint(0,50)
print("Максимальный элемент последовательности: ",max)
'''-----------------------------------------------------''' 
import random
count=0
max=0
arv=random.randint(0,50)
print('Последовательность случайных чисел')

while count<=20:
    count+=1
    if arv==0: #Выход из цикла
        break
    else:
        if max<arv:
            max=arv
        print(arv)
        arv=random.randint(0,50)
print('Максимальный элемент последовательности: ',max)
print('Количество элементов в последовательности: ',count-1)

