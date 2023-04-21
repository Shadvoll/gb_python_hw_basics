def power_rec(base,power):
    def power_pos(base,power):
        if power == 0:
            return 1
        return power_pos(base,power-1)*base
    if power >= 0:
        return power_pos(base,power)
    else:
        return 1/power_pos(base,-power)

number = int(input("Введите основание: "))
power = int(input("Степень числа: "))
print(f"Ответ: {power_rec(number,power)}")