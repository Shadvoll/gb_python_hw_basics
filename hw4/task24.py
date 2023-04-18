import random
n = int(input('Количество кустов: '))
bushes = [random.randint(0,9) for _ in range(n)]
print(*bushes)
bushes.insert(bushes[-1],0)
bushes.append(bushes[1])
berries = [bushes[i-1] + bushes[i] + bushes[i+1] for i in range(n)]
print(max(berries))