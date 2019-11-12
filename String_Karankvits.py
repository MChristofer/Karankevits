#1
a=input('Введите строку ')
print(a[2])
print(a[5])
print(a[0:5])
print(a[:-2])
print(a[0:7:2])
print(a[1:7:2])
print(a[::-1])
print(a[::-2])
print(len(a))
#2
a=input('Введите строку ')
print(a.count(' ')+1)
#3
a=input('Введите строку ')
print(a[(len(a) + 1) // 2:] + a[:(len(a) + 1) // 2])
#4
a=input()
first_word = a[:a.find(' ')]
second_word = a[a.find(' ') + 1:]
print(second_word + ' ' + first_word)
#5
a=input()
if a.count('f') == 1:
    print(a.find('f'))
elif a.count('f') >= 2:
    print(a.find('f'), a.rfind('f'))
#6
a=input()
if a.count('f') == 1:
    print(-1)
elif a.count('f') < 1:
    print(-2)
else:
    print(a.find('f', a.find('f') + 1))
#7
a=input()
a=a[:a.find('h')] + a[a.rfind('h') + 1:]
print(a)
#8
a = input()
b = a[:a.find('h')] 
c = a[a.find('h'):a.rfind('h') + 1]
d = a[a.rfind('h') + 1:]
a = b + c[::-1] + d
print(a)
