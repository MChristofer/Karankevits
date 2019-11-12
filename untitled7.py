#1. Задача "делаем срезы".
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))
#2. Задача "Кол-во строк"
print(input().count(' ')+1)
#3. Задача "Две половинки"
s=input()
x=len(s)
l1= x-x // 2
print(s[l1:] + s[:l1])
#4. Задача "Переставить два слова"
s=input()
a = s[s.find(' ')+1:len(s)]+' '+5[0:s.find(' ')]
print(a)
#5. Задача "Первое и последнее вхождение"
s=input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))
#6. Задача "Второе вхождение"
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
#7. Задача "Удалеие фрагмента"
s=input()
s=s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)
#8. Задача "Обращение фрагмента"
s=input
a=s[:s.find('h') + 1]
b=s[s.find('h'):s.rfind('h') + 1]
c=s[s.rfind('h') + 1:]
s=a + b[::-1] + c
print(s)
