
dictionary = {
        1: 'Ви хочете перевести градуси з Цельсія у Фаренгeйт чи з Фаренгейта в Цельсія? (1\\2): ',
        2: 'Ви надрукували неправильно, спробуйте ввести знову: ',
        3: 'Введіть градуси °C: ',
        4: 'Введіть градуси °F: ',
        5: 'будете рахувати ще? (так/ні): '
    }

def weatherCalculator():
    listFarenheit = ["1", "з цельсія", "перевести з цельсія", "у фаренгейт", "перевести у фаренгейт", "перше"]
    listCelsius = ["2","в цельсія", "перевести в цельсія", "з фаренгейту", "перевести з фаренгейту", "друге"]

    answer = input(dictionary[1]).lower()

    if answer in listFarenheit:
        toFarenheit()
    elif answer in listCelsius:
        toCelsius()
    else:
        print(dictionary[2])
        answer = input(dictionary[1]).lower()

def toFarenheit():
    degrees = float(input(dictionary[3]))
    degreesFahrenheit = round((degrees*1.8)+32, 2)
    print(str(degreesFahrenheit) + '°F')

def toCelsius():
    degrees = float(input(dictionary[4]))
    degreesCelsius = round(5/9*(degrees-32), 2)
    print(str(degreesCelsius) + '°C')



indicator = 1

while indicator == 1:
    weatherCalculator()
    decision = input(dictionary[5]).lower()
    if decision == "так":
        indicator = 1
    else:
        indicator = 0








              



