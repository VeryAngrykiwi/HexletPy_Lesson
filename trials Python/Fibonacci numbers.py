'''
Задача:
Реализуйте функцию fib(), находящую положительные Числа Фибоначчи. Аргументом функции является порядковый номер числа.
'''

#chatGPT

def fib(n):
  if n <= 0:
      return "Номер числа Фибоначчи должен быть положительным"

  fib_sequence = [0, 1]

  while len(fib_sequence) < n:
      next_number = fib_sequence[-1] + fib_sequence[-2]
      fib_sequence.append(next_number)

  return fib_sequence[:n]

# Пример использования функции
ordinal_number = 10  # Задайте желаемый порядковый номер
result = fib(ordinal_number)
print(result)

'''
объяснение:

def fib(n):

  if n <= 0:
      return "Номер числа Фибоначчи должен быть положительным"
Определение функции fib:
def fib(n):: Объявляет функцию fib с одним параметром n, который представляет собой порядковый номер числа Фибоначчи.
if n <= 0:: Проверяет, что порядковый номер положителен. Если нет, функция возвращает сообщение об ошибке.
fib_sequence = [0, 1]
Инициализация списка:
fib_sequence = [0, 1]: Создает начальный список fib_sequence, включая первые два числа Фибоначчи.

while len(fib_sequence) < n:
next_number = fib_sequence[-1] + fib_sequence[-2]
fib_sequence.append(next_number)
Построение последовательности Фибоначчи:
while len(fib_sequence) < n:: Использует цикл while для продолжения построения последовательности до тех пор, пока длина списка fib_sequence не достигнет заданного порядкового номера n.
next_number = fib_sequence[-1] + fib_sequence[-2]: Вычисляет следующее число Фибоначчи, которое является суммой двух предыдущих чисел в последовательности.
fib_sequence.append(next_number): Добавляет новое число в конец списка fib_sequence.

return fib_sequence[:n]
Возвращение результата:
return fib_sequence[:n]: Возвращает список, содержащий первые n чисел Фибоначчи.

ordinal_number = 10  # Задаем порядковый номер
result = fib(ordinal_number)
print(result)

'''

# replit
def fib(n):
  if n == 0:
      return 0
  elif n == 1:
      return 1
  else:
      return fib(n-1) + fib(n-2)

print(fib(3))