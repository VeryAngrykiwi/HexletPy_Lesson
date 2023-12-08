'''
задача: 
В этом испытании вы будете работать с «тройками» — кортежами из трех элементов. Вам предстоит реализовать две функции, которые вращают тройку влево и вправо. Как это выглядит, вы можете понять из пары примеров:
'''

#chatGPT
def rotate_left(triple):
  # Вращаем тройку влево (сдвигаем элементы на одну позицию влево)
  return triple[1:] + (triple[0],)

def rotate_right(triple):
  # Вращаем тройку вправо (сдвигаем элементы на одну позицию вправо)
  return (triple[-1],) + triple[:-1]

# Пример использования функций
original_triple = (1, 2, 3)

rotated_left = rotate_left(original_triple)
rotated_right = rotate_right(original_triple)

print(f"Исходная тройка: {original_triple}")
print(f"Тройка, вращенная влево: {rotated_left}")
print(f"Тройка, вращенная вправо: {rotated_right}")

#replit
def rotate_left(triple):
    return triple[1], triple[2], triple[0]

def rotate_right(triple):
    return triple[2], triple[0], triple[1]

print(rotate_left((1, 2, 3)))
print(rotate_right((1, 2, 3)))