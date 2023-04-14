costs = {}
for elem in "AEIOULNSTRАВЕИНОРСТ":
    costs[elem] = 1
for elem in "DGДКЛМПУ":
    costs[elem] = 2
for elem in "BCMPБГЁЬЯ":
    costs[elem] = 3
for elem in "FHVWYЫЙ":
    costs[elem] = 4
for elem in "KЖЗХЦЧ":
    costs[elem] = 5
for elem in "JXШЭЮ":
    costs[elem] = 8
for elem in "QZФШЪ":
    costs[elem] = 10

word = input("Введите слово: ").upper()
score = 0
for elem in word:
    score += costs[elem]
print(f"Количество очков: {score}")