'''
описание:
Реализуйте функцию is_happy_number(), которая возвращает True, если число счастливое, и False — если нет. Количество итераций процесса поиска необходимо ограничить числом 10.
'''

#chatGPT

def is_happy_number(number):
  def square_sum(n):
      return sum(int(digit) ** 2 for digit in str(n))

  for _ in range(10):  # Ограничиваем количество итераций 10
      number = square_sum(number)
      if number == 1:
          return True  # Число счастливое
  return False  # Число не является счастливым после 10 итераций

# Пример использования функции
happy_number = 19
result = is_happy_number(happy_number)
print(result)

'''
def is_happy_number(number):
  def square_sum(n):
      return sum(int(digit) ** 2 for digit in str(n))
Определение функции is_happy_number:
def is_happy_number(number):: Объявляет функцию is_happy_number с одним параметром number, представляющим собой число, которое мы проверяем на "счастье".
def square_sum(n):: Вложенная функция square_sum принимает число n и возвращает сумму квадратов его цифр. Эта функция будет использоваться в основной функции для вычисления следующего числа в последовательности.

for _ in range(10):  # Ограничиваем количество итераций 10
  number = square_sum(number)
  if number == 1:
      return True  # Число счастливое
return False  # Число не является счастливым после 10 итераций
# Пример использования функции
happy_number = 19
result = is_happy_number(happy_number)
print(result)
Цикл проверки на "счастье":
for _ in range(10):: Цикл выполняется 10 раз (ограничение по числу итераций).
number = square_sum(number): На каждой итерации число заменяется на сумму квадратов его цифр.
if number == 1:: После каждой итерации проверяется, стало ли число равным 1 (число стало "счастливым"). Если да, то функция возвращает True.
Возвращение результата:
return True: Если число стало "счастливым" в течение 10 итераций.
return False: Если число не стало "счастливым" после 10 итераций.

happy_number = 19
result = is_happy_number(happy_number)
print(result)
В данном примере функция проверяет, является ли число 19 "счастливым" и возвращает результат (True или False).
'''


#replit
def is_happy_number(number):
    for _ in range(10):
        number = str(sum(int(digit) ** 2 for digit in number))
        if number == '1':
            return True
    return False

print(is_happy_number('7'))

