# Задача
# Напишіть програму, яка використовує рівно три цикли для друку наступної послідовності символів:
# AAA 
# AAA 
# AAA 
# AAA 
# AAA 
# AAA
# BBBB 
# BBBB 
# BBBB 
# BBBB 
# BBBB 
# E 
# TTTTT
# TTTTT 
# TTTTT 
# TTTTT 
# TTTTT 
# TTTTT 
# TTTTT 
# TTTTT 
# TTTTT 
# G
# Формат вихідних даних 
# Програма має вивести вказану послідовність символів.

for i in range(6):
    for j in range(3):
        print("A", end="")
    print()

for i in range(5):
    for j in range(4):
        print("B", end="")
    print()

print("E")

for i in range(9):
    for j in range(5):
        print("T", end="")
    print()

print("G")
