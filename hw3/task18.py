n = int(input("Количество чисел: "))
nums = [int(input()) for _ in range(n)]
x = int(input('Число для поиска: '))
min_diff = abs(nums[0] - x)
result = nums[0]
for i in range(1,n):
    if abs(nums[i]-x) < min_diff:
        min_diff = abs(nums[i] - x)
        result = nums[i]
print(result)
