#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

def reduction(denominator,numerator,denumer):
    counter = 2
    while counter < denominator:
        if numerator % counter == 0 and denumer % counter == 0:
            numerator = int(numerator/counter)
            denumer = int(denumer/counter)
        else:
            counter += 1         
    return (f'{numerator}/{denumer}')
    
first_fraction = input('Введите первую дробь a/b: ').split('/')
second_fraction = input('Введите вторую дробь a/b: ').split('/')
flag = True
first_denominator = int(first_fraction[1])
second_denominator = int(second_fraction[1])
first_numerator = int(first_fraction[0])
second_numerator = int(second_fraction[0])
max_denominator = int(max(first_denominator, second_denominator))
while flag:
    if max_denominator%first_denominator == 0 and max_denominator%second_denominator == 0:
        flag = False
    else:
        max_denominator += 1
first_add_multiplier = max_denominator / first_denominator
second_add_multiplier = max_denominator / second_denominator
res_numerator  = first_numerator * int(first_add_multiplier) + second_numerator * int(second_add_multiplier)
print(f'\nРезультат сложение дробей: {reduction(max_denominator, res_numerator,max_denominator)}')
numerator_multiply = first_numerator * second_numerator
denominator_multiply = first_denominator * second_denominator
max_num = max(numerator_multiply,denominator_multiply)
print(f'Результат умножения дробей: {reduction(max_num, numerator_multiply,denominator_multiply)}')
first_test = Fraction(first_numerator, first_denominator)
second_test = Fraction(second_numerator, second_denominator)
print('='*20)
print(f'Результаты проверки:\nСумма: {first_test + second_test}\nПроизведение: {first_test * second_test}')
