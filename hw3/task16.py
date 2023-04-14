n = int(input('Количество чисел в списке: '))
# nums = list(map(int,input().split())) если числа в одной строке через пробел
nums = []
for i in range(n):
    nums.append(int(input()))
x = int(input())
print(f"Количество {x} в списке: {nums.count(x)}")
