# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 47. Операции со строками
 Вход: 
   нет 
 Результат:
   Привет, Вася!
   34567
   0129
   012ABC3456789
   9876543210
"""
s1 = "Привет" 
s2 = "Вася" 
s = s1 + ", " + s2 + "!" 
print ( s )

s = "0123456789"
s1 = s[3:8]
print ( s1 )
  
s = "0123456789"
s1 = s[:3] + s[9:]
print ( s1 )
  
s = "0123456789"
s1 = s[:3] + "ABC" + s[3:]
print ( s1 )

s = "0123456789"
s1 = s[::-1]
print ( s1 )


