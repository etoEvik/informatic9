
listOfWords = []

while True:
    word = input("Введіть слово: ")
    if word == "КІНЕЦЬ":
        break
    listOfWords.append(word)

for word in listOfWords:
    print(word)