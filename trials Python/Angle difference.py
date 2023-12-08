'''
задача:
Напишите функцию diff, которая принимает два угла (int) и возвращает наименьшую разницу между ними.
'''

#chatGPT
def angle_diff(angle1, angle2):
  # Нормализуем углы в пределах от 0 до 359 градусов
  angle1 = angle1 % 360
  angle2 = angle2 % 360

  # Находим абсолютную разницу между углами
  absolute_diff = abs(angle1 - angle2)

  # Находим минимальную разницу между углами (учитываем переход через 360 градусов)
  min_diff = min(absolute_diff, 360 - absolute_diff)

  return min_diff

# Пример использования функции
angle1 = 30
angle2 = 330
result = angle_diff(angle1, angle2)
print(f"Наименьшая разница между углами {angle1} и {angle2}: {result} градусов")

#replit
def diff_angle(a, b):
  if a > b:
    return a - b
  else:
    return b - a

print(diff_angle(0, 45))