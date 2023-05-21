def create_list_progression(a1,d,n):
    return [a1+i*d for i in range(n)]  

def create_list(a1,d,n):
    lst = []
    for i in range(n):
        lst.append(a1+i*d)
    return lst

    
a1 = int(input("Введите первый элемент арифм. посл-ти: "))
n = int(input("Введите кол-во элементов арифм. посл-ти: "))
d = int(input("Введите шаг арифм. посл-ти: "))

print("Последовательность: ")
print(*create_list_progression(a1,d,n))
print(*create_list(a1,d,n))
print(*range(a1,a1+n*d,d))
