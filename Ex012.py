'''Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате 
по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна 
их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и 
их произведение P. Помогите Кате отгадать задуманные Петей числа.
Пример:
4 4 -> 2 2
5 6 -> 2 3'''

from random import randint
s, p = randint(0, 1000), randint(0, 1000)
print(s, p)
D = s**2 - 4*p
print(f'D {D}')
if D >= 0:
    y1 = (s + D**(1/2))/2
    # y2 = (s - D**(1/2))/2 # второй корень можно здесь не учитывать, тк с ним получим зеркальное решение:
    # например, если для y1=2 получим x=6, то для y2= 6 будем иметь x = 2.
    # print(y1, y2)
else:
    print('неверная подсказка')
if y1 > 0:
    x = round(s - y1)
print(f'x {x}, y {round(y1)}') 
# Т.к. случайным образом трудно добиться корректных чисел одновременно для суммы и произведения, 
# необходимо уточнение числа для произведения.
print(f'Уточнение чисел. Подсказка для Кати: сумма равна {s} произведение {round(x*y1)}')


