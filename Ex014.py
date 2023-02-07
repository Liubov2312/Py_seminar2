'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k ), 
не превосходящие числа N.
10 -> 1 2 4 8'''

from random import randint
N = randint(0, 10)
print(N)
a = 0
for i in range(0, N):
    a = 2**i
    if a < N:
        print(a, end=' ')
        

