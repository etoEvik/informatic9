# Задача №1 
# Квадрат числа
# На вхід програмі подається натуральне число  n. Напишіть програму, яка для кожного з чисел від 0 до n (включно) виводить фразу: «Квадрат числа [число] дорівнює [число]» (без лапок).

# Формат вхідних даних
# На вхід програмі подається натуральне число n.

# Формат вихідних даних
# Програма має вивести текст відповідно до умови завдання. 

number = int(input("Введіть натуральне число: "))

for i in range(number+1):
    square = i ** 2
    print("Квадрат числа", i, "дорівнює", square)
