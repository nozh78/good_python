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

# Подвиг 5
# Вводится список имен студентов в одну строчку через пробел. Определить, что
# хотя бы одно имя в этом списке начинается и заканчивается на ту же самую букву
# (без учета регистра). Реализовать программу с использованием цикла while и
# оператора break. Вывести ДА, если условие выполняется и НЕТ - в противном случае.
# students = input()
# students_list = students.split()
# count = 0
# while count < len(students_list):
#     if students_list[count][0].lower() != students_list[count][-1].lower():
#         count += 1
#     else:
#         print("ДА")
#         break
# else:
#     print("НЕТ")


# Подвиг 6
# Вводится натуральное число n (то есть, целое положительное). В цикле перебрать
# все целые числа в интервале [1; n] и сформировать список из чисел, кратных 3 и 5
# одновременно. Вывести полученную последовательность чисел в виде строки через
# пробел, если значение n меньше 100. Иначе вывести на экран сообщение
# "слишком большое значение n" (без кавычек). Использовать в программе оператор
# else после цикла while.
# n = int(input())
# if n < 100:
#     numbers = []
#     count = 1
#     while count <= n:
#         if count % 3 == 0 and count % 5 == 0:
#             numbers.append(count)
#         count += 1
#     print(*numbers)
# else:
#     print("слишком большое значение n")
