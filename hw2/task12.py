product = int(input('Введите произвидение: '))
summ = int(input('Введите сумму: '))
discreminant = summ**2 - 4*product
solution1 = (summ + discreminant**(0.5))/2
# solution2 = (summ - discreminant**(0.5))/2 #  solution2 - симметричное решение
if solution1 % 1 == 0:
    print(f"Ответ: {int(solution1)}, {int(summ-solution1)}")
else:
    print("Нет решения в натуральных числах")
    print(f"Ответ: {solution1}, {summ-solution1}")

