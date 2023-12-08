'''
задача:
Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно. При этом:

Если число делится без остатка на 3, то вместо него выводится слово Fizz
Если число делится без остатка на 5, то вместо него выводится слово Buzz
Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
В остальных случаях в строку добавляется само число
Функция принимает параметры begin и end, которые определяют начало и конец диапазона включительно. Функция возвращает пустую строку, если диапазон пуст — в случае, когда begin > end.
'''
#chatGPT
def fizz_buzz(begin, end):
  # Проверка на пустой диапазон
  if begin > end:
      return ""

  result = []
  for num in range(begin, end + 1):
      # Проверка условий и формирование строки
      if num % 3 == 0 and num % 5 == 0:
          result.append("FizzBuzz")
      elif num % 3 == 0:
          result.append("Fizz")
      elif num % 5 == 0:
          result.append("Buzz")
      else:
          result.append(str(num))

  # Объединяем элементы списка в строку с пробелами
  return ' '.join(result)

# Пример использования функции
begin_range = 11
end_range = 20

result_string = fizz_buzz(begin_range, end_range)

print(result_string)

'''
пояснения:

Проверка на пустой диапазон:
if begin > end:
  return ""
Если начальное значение begin больше конечного значения end, то функция возвращает пустую строку, так как диапазон некорректен.

Инициализация пустого списка result для хранения результатов:
result = []

Цикл для прохода через числа в диапазоне:
for num in range(begin, end + 1):
Функция использует range(begin, end + 1), чтобы включить последнее значение в диапазон.

Проверка условий и формирование строки:
if num % 3 == 0 and num % 5 == 0:
  result.append("FizzBuzz")
elif num % 3 == 0:
  result.append("Fizz")
elif num % 5 == 0:
  result.append("Buzz")
else:
  result.append(str(num))
Если число делится на 3 и 5 без остатка, добавляется "FizzBuzz".
Если число делится на 3 без остатка, добавляется "Fizz".
Если число делится на 5 без остатка, добавляется "Buzz".
В остальных случаях добавляется само число, преобразованное в строку.

Объединение элементов списка в строку с пробелами:
return ' '.join(result)
Функция использует метод join для объединения элементов списка в строку, разделяя их пробелами.

Пример использования функции:
begin_range = 1
end_range = 20

result_string = fizz_buzz(begin_range, end_range)

print(result_string)
Здесь приведен пример использования функции для диапазона от 1 до 20. Функция возвращает строку, содержащую числа и соответствующие им значения "Fizz", "Buzz" и "FizzBuzz" в соответствии с условиями.
'''

#replit
def fizz_buzz(begin, end):
  if begin > end:
    return ''
  result = ''
  for i in range(begin, end + 1):
    if i % 3 == 0 and i % 5 == 0:
      result += 'FizzBuzz '
    elif i % 3 == 0:
      result += 'Fizz '
    elif i % 5 == 0:
      result += 'Buzz '
    else:
      result += str(i) + ' '
  return result

print(fizz_buzz(11, 20))