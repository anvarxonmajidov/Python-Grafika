# -*- coding: utf-8 -*-
"""
 Программа к учебнику информатики для 10 класса
 К.Ю. Полякова и Е.А. Еремина.
 Глава 8.
 Программа № 53. Рекурсивный перебор
 Вход: 
   нет 
 Результат: 
   <64 слова>
"""
def TumbaWords ( A, w, L ):
  if len(w) == L:
    print ( w )
    return
  for c in A:
    TumbaWords ( A, w + c, L );

TumbaWords("ЫШЧО", "", 3)

