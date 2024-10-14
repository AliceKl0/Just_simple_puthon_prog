'''
11) Напишите программу: а) для сортировки (по возрастанию и убыванию)
словаря по значению; б) для объединения двух словарей и суммирующую
значения для общих ключей; в) для проверки наличия нескольких ключей
в словаре.
'''

# а)
alph={'Вася':10,'Лена':12,'Игорь':14,'Марина':7}
alph_up=sorted(alph.items(), key = lambda x: x[1])
# alph_down=alph_up[::-1]
alph_down=sorted(alph.items(), key = lambda x: x[1], reverse = True)
print ("По возрастанию значений:", alph_up)
print ("По убыванию значений:", alph_down)

# б)
alph1={'Вася':10,'Лена':12,}
alph2={'Игорь':14,'Марина':7,'Вася':15}
alph3={k: alph1.get(k,0) + alph2.get(k,0) for k in set(alph1) | set(alph2)}
print ("Объединённый словарь:", alph3)

# в)
alph={'Вася':10,'Лена':12,'Игорь':14,'Марина':7}
kkey=input("Введите ключ для поиска: ")
if alph.get(kkey) is not None:
    print ("Ключ присутствует в словаре.")
else:
    print ("Ключ отсутствует в словаре.")

'''
12) Напишите программу: а) для создания кортежа; б) для преобразования
кортежа в словарь.
'''

# а)
from random import *
cort=tuple(tuple(randint (-1000,1000) for i in range (2)) for j in range (10,20))
print ("Кортеж:", cort)

# б)
alph=dict(cort)
print ("Словарь из кортежа:", alph)

# *б) (В каждом "внутреннем" кортеже более двух элементов. Первый берём за ключ, остальные берём за значения.)
cort=tuple(tuple(randint (-1000,1000) for i in range (10,20)) for j in range (10,20))
alph={}
for i in range (len(cort)):
    alph[cort[i][0]]=[j for j in cort[i][1::]]
print (cort)
print ("Словарь из кортежа:", alph)

'''
13) Дана непустая последовательность символов. Построить и напечатать
множества, элементами которых являются встречающиеся в последова-
тельности: а) цифры от «0» до «9» и знаки арифметических операций;
б) буквы от «A» до «F» и от «X» до «Z».
'''

from random import *
alph=list('1234567890*+-/QWERTYUIOPASDFGHJKLZXCVBNM')
s=''
for i in range (8):
    s+=choice(alph)
print ("Символы:",s)

# а)
alph_chisla='0123456789*+-/'
s_chisla=set()
for i in s:
    if i in alph_chisla:
        s_chisla.add(i)
print ("Множество чисел:", s_chisla)

# б)
alph_AF=list('ABCDEF')
alph_XZ=list('XYZ')
s_AF=set()
s_XZ=set()
for i in s:
    if i in alph_AF:
        s_AF.add(i)
    elif i in alph_XZ:
        s_XZ.add(i)
print ("Множество A-F:", s_AF, "\nМножество X-Z:", s_XZ)