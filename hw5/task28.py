def sum_rec(a,b):
    if a == 0:
        return b
    return sum_rec(a-1,b+1)

number1 = int(input('Первое слагаемое: '))
number2 = int(input('Второе слагаемое: '))
print(f'Результат суммирования: {sum_rec(number1,number2)}')