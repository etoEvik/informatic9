
def dogYearsCalculator():
    dogYears = int(input('Введіть вік вашої собаки: '))
    humanYears = 0

    for i in range (1, dogYears+1):
        if i <= 2:
            humanYears = humanYears + 10.5
        else:
            humanYears = humanYears + 4
    print (str(humanYears) + " років")
    

indicator = 1

while indicator == 1:
    answer = input('Хочете перевести вік своєї собаки в людський?: ').lower()
    if answer == 'так':
        dogYearsCalculator()
        indicator = 1
    elif answer == 'ні':
        indicator = 0