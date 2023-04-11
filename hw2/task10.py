amount = int(input())

reshki = 0
for i in range(amount):
    if int(input()) == 0:
        reshki += 1
print(min(reshki,amount-reshki))