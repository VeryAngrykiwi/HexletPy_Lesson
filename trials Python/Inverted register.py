'''
задача:
Реализуйте функцию invert_case(), которая меняет в строке регистр каждой буквы на противоположный.
'''

#chatGPT
def invert_case(input_string):
  # Меняем регистр каждой буквы на противоположный
  inverted_string = ''.join(char.lower() if char.isupper() else char.upper() for char in input_string)
  return inverted_string

# Пример использования функции
original_string = "Hello, World!"

inverted_result = invert_case(original_string)

print(f"Исходная строка: {original_string}")
print(f"Строка с инвертированным регистром: {inverted_result}")


#replit
def invert_case(text):
  result = ''
  for char in text:
    if char.isupper():
      result += char.lower()
    else:
      result += char.upper()
  return result 

print(invert_case('Hello, World!'))

def invert_case2(text):
    return text.swapcase()

print(invert_case2('I love Python'))

