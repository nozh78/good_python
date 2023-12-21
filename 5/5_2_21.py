# Подвиг 2
# p = [0] * 10
# count = 0
# num = 0
# while count < 7:
#     num = int(input())
#     if p[num] == 0:
#         p[num] = 1
#     count += 1
# print(*p)


# Подвиг 3
# На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение
# только положительных чисел, до тех пор, пока не будет введено значение 0.
# Реализовать пропуск вычислений с помощью оператора continue,
# а также использовать цикл while. Результат произведения вывести на экран.
# proizv = 1
# count = 0
# while count < 10:
#     chislo = int(input("Введите число "))
#     if chislo > 0:
#         proizv *= chislo
#     elif chislo == 0:
#         break
#     elif chislo < 0:
#         continue
#     count += 1
# print(proizv)


# Подвиг 4.
# Вводится список названий городов в одну строчку через пробел. Определить, что в
# этом списке все города имеют длину более 5 символов. Реализовать программу с
# использованием цикла while и оператора break. Вывести ДА, если условие выполняется
#  и НЕТ - в противном случае.
# cities = input()
# cities_list = cities.split()
# count = 0
# while count < len(cities_list):
#     if len(cities_list[count]) > 5:
#         count += 1
#     else:
#         print("НЕТ")
#         break
# else:
#     print("ДА")
