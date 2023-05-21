import random
def find_idxs_in_bounds(lst, lower_bound, upper_bound):
    return [idx for idx, elem in enumerate(lst) if lower_bound <= elem <= upper_bound]

# def f(lst,lower_bound, upper_bound):
#     lst = []
#     for idx, elem in enumerate(lst):
#         if lower_bound <= elem <= upper_bound:
#             lst.append(idx)
#     return lst


n = int(input("Введите кол-во символов для генерации списка: "))
lower_bound = int(input("Введите нижнюю границу значений для нахождения индексов: "))
upper_bound = int(input("Введите нижнюю границу значений для нахождения индексов: "))
lst_random = [random.randint(-100,100) for _ in range(n)]
print(f"Случайные список: {lst_random}")
print(f"Индексы значений в диапазоне: [{lower_bound};{upper_bound}]")
print(find_idxs_in_bounds(lst_random,lower_bound,upper_bound))