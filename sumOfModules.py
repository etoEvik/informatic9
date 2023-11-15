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

