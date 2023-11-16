# Задача №2:
# Абсолютна сума
# Дані п'ять чисел
# a1, a2, a3, a4, a5. Напишіть програму, яка обчислює суму їх модулів
# |a1|+|a2|+|a3|+|a4|+|a5|. 

# Формат вхідних даних 
# На вхід до програми подається п'ять дійсних чисел
# a1,
# a2,
# a3,
# a4,
# a5, кожне на окремому рядку. 
# Формат вихідних даних 
# Програма повинна вивести одне число – суму модулів введених чисел.

maxNumbers = int(input('Скільки чисел ви бажаєте скласти?: '))
print('Введіть числа: ')

def addNumbers(limitNumbers):
    index = 0
    total = 0
    while index < limitNumbers:
        a = int(input())
        total = total  + abs(a)
        index = index+ 1
    return total


totalSum = addNumbers(maxNumbers)
print('Сума модулів введених чисел: ' + str(totalSum))


# a1 = float(input("Enter a1: "))
# a2 = float(input("Enter a2: "))
# a3 = float(input("Enter a3: "))
# a4 = float(input("Enter a4: "))
# a5 = float(input("Enter a5: "))

# result = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
# print("The absolute sum is", result)

