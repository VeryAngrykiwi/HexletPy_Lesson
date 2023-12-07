'''
Задача:
В рамках этого испытания вы реализуете небольшой набор функций, работающих с отрезками прямых на двухмерной плоскости. Отрезок в нашем случае будет кодироваться в виде пары пар и выглядеть как-то так: ((x1, y1), (x2, y2)) (вложенные пары — это концы отрезка). Вам нужно реализовать четыре функции:

is_degenerated() должна возвращать истину, если отрезок вырожден в точку (начало и конец совпадают)
is_vertical() должна возвращать истину, если отрезок — вертикальный
is_horizontal() должна возвращать истину, если отрезок — горизонтальный
is_inclined() должна возвращать истину, если отрезок — наклонный (не вертикальный и не горизонтальный)
'''
#chatGPT

def is_degenerated(segment):
  # Используем сравнение координат начала и конца отрезка
  return segment[0] == segment[1]

def is_vertical(segment):
  # Вертикальный отрезок, если x1 и x2 совпадают
  return segment[0][0] == segment[1][0]

def is_horizontal(segment):
  # Горизонтальный отрезок, если y1 и y2 совпадают
  return segment[0][1] == segment[1][1]

def is_inclined(segment):
  # Наклонный отрезок, если не вертикальный и не горизонтальный
  return not is_vertical(segment) and not is_horizontal(segment)

# Пример использования функций
segment1 = ((1, 2), (1, 5))  # Вертикальный отрезок
segment2 = ((2, 3), (5, 3))  # Горизонтальный отрезок
segment3 = ((1, 2), (3, 4))  # Наклонный отрезок
segment4 = ((1, 2), (1, 2))  # Вырожденный отрезок

print(is_degenerated(segment4))  # True
print(is_vertical(segment1))  # True
print(is_horizontal(segment2))  # True
print(is_inclined(segment3))  # True



#replit

def is_degenerated(line):
    return line[0] == line[1]

def is_vertical(line):
    return line[0][0] == line[1][0]

def is_horizontal(line):
    return line[0][1] == line[1][1]

def is_inclined(line):
    return line[0][0] != line[1][0] and line[0][1] != line[1][1]
