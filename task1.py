#Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.

number = int(input('Введите число: '))
original_number = number
BASE = 16
hex_nums = '0123456789ABCDEF'
result_number = ''
while number:
    remains = number % BASE
    hex_num = hex_nums[remains]
    result_number = hex_num + result_number
    number //= BASE
test_number = hex(original_number)
print(f'Число {original_number} в {BASE}-ичной системе будет: {result_number}')
print(f'При проверке получилось число: {test_number}')
