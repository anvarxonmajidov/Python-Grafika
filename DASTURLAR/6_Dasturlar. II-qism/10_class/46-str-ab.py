# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 46. Посимвольная обработка строк
 Вход: 
   аабб
 Результат:
   бббб
"""
print ( "Введите строку:" )
s = input()
s1 = ""
for c in s:
  if c == "а": c = "б"
  s1 = s1 + c
print ( s1 )



