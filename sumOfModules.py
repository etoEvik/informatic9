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



