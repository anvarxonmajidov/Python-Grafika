# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 33. Ввод элементов массива с клавиатуры и
                 поэлементный вывод
 Вход: 
   1 
   2 
   3 
   4 
   5
 Результат:
   Исходный массив:
   1 2 3 4 5 
   1 2 3 4 5
   Массив задом наперёд:
   5 4 3 2 1 
"""
N = 5
A = [0] * N
print ( "Введите элементы массива:" )
for i in range(N):
  print("A[", i, "]=", sep="", end="")
  A[i] = int( input() )

print ( "Исходный массив:" )
for x in A:
  print ( x, " ", sep="", end="" )    
print()  

print ( " ".join( [ str(x) for x in A] ) )

print ( "Массив задом наперёд:" )
for i in range(N-1,-1,-1):
  print ( A[i], " ", sep="", end="" )    
print()  
