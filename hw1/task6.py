def SumDigits(number):
    if number == 0:
        return 0
    return number % 10 + SumDigits(number//10)


number = int(input("Введите номер билета: "))
leftPart = number // 1000
rightPart = number % 1000
if SumDigits(leftPart) == SumDigits(rightPart):
    print("yes")
else:
    print("no")
