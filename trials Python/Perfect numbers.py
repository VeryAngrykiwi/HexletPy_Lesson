'''
задача:
Реализуйте функцию is_perfect(), которая принимает число и возвращает True, если оно совершенное, и False — в ином случае.

Совершенное число — это положительное целое число, равное сумме его положительных делителей (не считая само число). Например, 6 — совершенное число, потому что 6 = 1 + 2 + 3.
'''
#chatGPT
def is_perfect(number):
  # Проверяем, что число положительное
  if number <= 0:
      return False

  # Находим положительные делители числа
  divisors = [i for i in range(1, number) if number % i == 0]

  # Проверяем, равна ли сумма делителей числу
  return sum(divisors) == number

# Пример использования функции
number1 = 6
number2 = 28
number3 = 12

print(is_perfect(number1))  # True
print(is_perfect(number2))  # True
print(is_perfect(number3))  # False


#replit
def is_perfect(number):
    if number < 2:
        return False
    divisors = [1]
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors) == number

print(is_perfect(6))
