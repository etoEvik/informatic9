# Задача №1

# Дано два цілих числа m і n (m≤n). Напишіть програму, яка виводить усі цілі числа від m до n включно.

# Формат вхідних даних
# На вхід програмі подаються два цілих числа m і n, кожне на окремому рядку.

# Формат вихідних даних
# Програма має вивести числа відповідно до умови завдання.

m = int(input("Введіть перше ціле число: "))
n = int(input("Введіть друге ціле число (більше за перше): "))

for i in range(m, n+1):
    print(i, end=" ")