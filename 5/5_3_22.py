# Подвиг 1
# С помощью функции range() сформируйте следующую последовательность чисел:
# 0, 1, 2, ..., 10
# Результат выведите в виде последовательности чисел, записанных через пробел в
# одну строчку.
# for i in range(11):
#     print(i, end=" ")


# Подвиг 2
# С помощью функции range() сформируйте следующую последовательность чисел:
# 10, 9, 8, ..., 0
# Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.
# for i in range(10, -1, -1):
#     print(i, end=" ")


# Подвиг 3
# С помощью функции range() сформируйте следующую последовательность чисел:
# -10, -8, -6, -4, -2
# Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку
# for i in range(-10, -1, 2):
#     print(i, end=" ")


# Подвиг 4
# С помощью функции range() сформируйте следующую последовательность чисел:
# 1, 4, 7, 10, 13, 16, 19
# Результат выведите в виде последовательности чисел, записанных через пробел в одну строчку.
# for i in range(1, 20, 3):
#     print(i, end=" ")


# Подвиг 5
# Вводятся целые числа в одну строчку через пробел. Необходимо преобразовать эти
# данные в список целых чисел. Затем, перебрать этот список в цикле for и
# просуммировать все нечетные значения. Результат вывести на экран.
# num = list(map(int, input().split()))
# summa = 0
# for i in num:
#     if i % 2 != 0:
#         summa += i
# print(summa)
