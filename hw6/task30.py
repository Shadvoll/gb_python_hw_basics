def create_list_progression(a1,d,n):
    return [a1+i*d for i in range(n)] 
    
a1 = int(input("Введите первый элемент арифм. посл-ти: "))
n = int(input("Введите кол-во элементов арифм. посл-ти: "))
d = int(input("Введите шаг арифм. посл-ти: "))

print("Последовательность: ")
print(*create_list_progression(a1,d,n))