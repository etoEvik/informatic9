
listOfNumbers = []

while True:
    number = int(input("Введіть число, що ділиться на 7: "))
    if number % 7 != 0:
        break 
    listOfNumbers.append(number)

for number in listOfNumbers:
    print(number) 