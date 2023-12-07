'''
описание:
Вам предстоит написать программу, которая шифрует сообщения по следующему алгоритму: она берёт текст и переставляет в нем каждые два подряд идущих символа.
Если количество символов нечетное, то последний символ остается на своем месте:

задача:
Реализуйте функцию encrypt(), который принимает на вход исходное сообщение и возвращает зашифрованное.
'''
#chatGPT

def encrypt(message):
  # Преобразуем строку в список символов для удобства манипуляций
  chars = list(message)

  # Проходим по символам с шагом 2 и меняем местами каждую пару
  for i in range(0, len(chars) - 1, 2):
      chars[i], chars[i + 1] = chars[i + 1], chars[i]

  # Преобразуем список обратно в строку
  encrypted_message = ''.join(chars)

  return encrypted_message

# Пример использования функции
original_message = "Hello, World!"
encrypted_message = encrypt(original_message)
print(encrypted_message)

'''
объяснение
def encrypt(message):
# Преобразуем строку в список символов для удобства манипуляций
chars = list(message)

# Проходим по символам с шагом 2 и меняем местами каждую пару
for i in range(0, len(chars) - 1, 2):
    chars[i], chars[i + 1] = chars[i + 1], chars[i]
Этот блок кода использует цикл for, чтобы пройти по списку chars с шагом 2 (то есть, начиная с 0 и до предпоследнего символа). Внутри цикла происходит обмен значениями каждой пары символов.

# Преобразуем список обратно в строку
encrypted_message = ''.join(chars)
Здесь происходит обратное преобразование списка chars в строку encrypted_message с использованием метода join. Таким образом, мы получаем зашифрованное сообщение.
return encrypted_message
'''


#replit
def encrypt(message):
    result = ''
    for i in range(1, len(message), 2):
        result += message[i]
        result += message[i-1]
    if len(message) % 2 != 0:
        result += message[-1]
    return result

print(encrypt('move'))  # 'tcakat'
