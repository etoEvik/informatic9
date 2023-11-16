# Задача:
# Сортування трьох 🌶️
# Напишіть програму, яка впорядковує три числа від більшої до меншої. 

# Формат вхідних даних 
# На вхід до програми подається три цілих числа, кожне на окремому рядку. 
# Формат вихідних даних 
# Програма повинна вивести три числа, кожне на окремому рядку, впорядкованих від більшого до меншого

maxNumbers = int(input('Скільки чисел ви хочете відсортувати?: '))
numbers = []

def bubbleSort(elements):
    N = len(elements)      

    for i in range(0, N-1):    
        for j in range(0, N-1-i):  
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

def addElementsInList(myList, limit):
    while len(myList) < limit:
        myList.append(int(input()))


print('Введіть числа: ')
addElementsInList(numbers, maxNumbers)
bubbleSort(numbers)
print("Відсортовані числа: ")

for i in numbers:
    print(i)

   
# a = int(input())
# b = int(input())
# c = int(input())

# max_num = max(a, b, c)
# min_num = min(a, b, c)
# mid_num = (a + b + c) - max_num - min_num

# print(max_num)
# print(mid_num)
# print(min_num) 