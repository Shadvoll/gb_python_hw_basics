# basics solution. Works only with 3 digit numbers
a = int(input("Введите трехзначное число: "))
digit1 = a % 10
a //= 10
digit2 = a % 10
a //= 10
digit3 = a % 10
print(digit1+digit2+digit3)

# more complicated solution. May work any amount of digits
a = int(input("Введите трехзначное число: "))
s = 0
while a > 0:
    s += a % 10
    a //= 10
print(s)

# recursion solution. Works on any amount of digits in the given number


def SumDigits(number):
    if number == 0:
        return 0
    return number % 10 + SumDigits(number//10)


a = int(input("Введите трехзначное число: "))
print(SumDigits(a))
