import random
n = int(input('Количество элементов в первом множестве: '))
m = int(input('Количество элементов во втором множестве: '))
lower_bound = -10 # может задать пользователь
upper_bound = 10
numbers1 = [random.randint(lower_bound,upper_bound) for _ in range(n)]
numbers2 = [random.randint(lower_bound,upper_bound) for _ in range(m)]
print("Множество 1:",*numbers1)
print("Множество 2:",*numbers2)
intersection = sorted(list(set(numbers1) & set(numbers2)))
print("Числа в обоих множествах:")
print(*intersection)