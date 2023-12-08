'''
задача:
Реализуйте функцию is_power_of_three(), которая определяет, является ли переданное число натуральной степенью тройки.
'''
#chatGPT
def is_power_of_three2(n):
  # Проверяем, является ли число степенью тройки
  while n > 1:
      if n % 3 != 0:
          return False
      n /= 3
  return n == 1

# Пример использования функции
number = 9

result = is_power_of_three2(number)

print(f"Число {number} {'является' if result else 'не является'} степенью тройки.")

#replit
def is_power_of_three(number):
  if number == 1:
    return True
  elif number % 3 == 0:
    return is_power_of_three(number / 3)
  else:
    return False 

print(is_power_of_three(9))