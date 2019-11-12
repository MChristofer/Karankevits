#1
a=int(input("1 число: "))
b=int(input("2 число: "))
if a<b:
    print(a)
elif a>b:
    print(b)
else:
    print('Числа равны')
#2
x=int(input('число: '))
if x>0:
    print(1)
elif x==0:
    print(0)
else:
    print(-1)
    
#3
a=int(input("Введи число от 1 до 8: "))
b=int(input("Введи число от 1 до 8: "))
a2=int(input("Введи число от 1 до 8: "))
b2=int(input("Введи число от 1 до 8: "))
if (a+b+a2+b2)%2==0:
    print('YES')
elif (a+b+a2+b2)%2!=0:
    print('YES')
else:
    print('NO')
#4
x=int(input('год: '))
if (x%4==0) and (x%100!=0) or (x%400==0):
    print('Висакосный')
else:
    print('Не висакосный')
    
#5
a=int(input('1 - '))
b=int(input('2 - '))
c=int(input('3 - '))
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
elif c<a and c<b:
    print(c)
else:
    print('Несколько наименьших')
#6
a=int(input('1 - '))
b=int(input('2 - '))
c=int(input('3 - '))
if a==b and a==c and a==c:
    print(3)
elif a==b or a==c or b==c:
    print(2)
else:
    print('0')
#7
x1=int(input('Введите число от 1-7'))
y1=int(input('Введите число от 1-7'))
x2=int(input('Введите число от 1-7'))
y2=int(input('Введите число от 1-7'))
if -1==(x1-x2) or -1==(y1-y2)<=1:
    print('YES')
else:
    print('NO')
#9
x1=int(input('Введите число от 1-7'))
y1=int(input('Введите число от 1-7'))
x2=int(input('Введите число от 1-7'))
y2=int(input('Введите число от 1-7'))
if x1-x2==y1-y2 or x2-x1==y2-y1:
    print('YES')
else:
    print('NO')
#10

x1=int(input('Введите число от 1-7'))
y1=int(input('Введите число от 1-7'))
x2=int(input('Введите число от 1-7'))
y2=int(input('Введите число от 1-7'))    
if (abs(x1-x2)==abs(y1-y2)) or (x1==x2 or y1==y2):
    print('YES')
else:
    print('NO')
    
#11

print('Введите 4 числа от 1 до 8')
x1=int(input('Введите число от 1-7'))
y1=int(input('Введите число от 1-7'))
x2=int(input('Введите число от 1-7'))
y2=int(input('Введите число от 1-7'))
if (abs(x1-x2)==2 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==2):
    print('YES')
else:
    print('NO')
#12
n=int(input())
m=int(input())    
k=int(input())
if (n*m)>k and ((k%n==0) or(k%m==0)):
    print('YES')
else:
    print('NO')
    
#13
n=int(input())
m=int(input())   
x=int(input())
y=int(input())
b=n-x
f=m-y
if x<y and x<b and x<f:
    print(x)
elif y<x and y<b and y<f:
    print(y)
elif b<x and b<y and b<f:
    print(b)
else:
    print(f)
    
#Угадай число
import random
a=random.randint(1, 50)
q=int(input('Сколько попыток: '))
g=0
while q>0:
    n=int(input('Введи число от 1 до 50: '))
    if n<=50:
        if n==a:
            print("Угадали!")
            g+=1
            if q!=1:
               a=random.randint(1, 50)
        elif n<a:
            print("Не угадали! Загаданное число больше!")
        else:
            print('Не угадали! Загаданное число меньше!')
    else:
        print('Вы ввели неверное число')
    q-=1
    print('осталось',q,"попыток.")
print('Загаданно было',a)
print("Вы выйграли "+ str(g)+' раз.')
















