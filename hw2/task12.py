product = int(input('Введите произвидение: '))
summ = int(input('Введите сумму: '))
discreminant = summ**2 - 4*product
solution1 = (summ + discreminant**(0.5))/2
# solution2 = (summ - discreminant**(0.5))/2
print(f"Решение 1: {solution1}, {summ-solution1}")
# print(f"Решение 2: {solution2}, {summ-solution2}")
# solution2 - симметричное решение
