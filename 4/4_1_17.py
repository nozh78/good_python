# Подвиг 1
# num = list(map(float, input().split()))
# # Сравниваем 2 числа из списка под индексом 0 и 1
# if num[0] > num[1]:
#     print(num[0])
# else:
#     print(num[1])

# Подвиг 2
# text_1 = input('text: ').lower()
# if text_1 == text_1[::-1]:
#     print('ДА')
# else:
#     print('НЕТ')

# Подвиг 3
# num = list(map(int, input().split()))
# if num[0] % num[1] == 0:
#     print(num[0] // num[1])
# else:
#     print(f'{num[0]} на {num[1]} нацело не делится')

# Подвиг 4
# a, b, c = map(int, input().split())
# Проверяем выполнения условия задания
# проверяем равна ли сумма квадратов стороны a и b, квадрату стороны c
# if c**2 == a**2 + b**2:
#     print("ДА") # Если условие выполняет выводим ДА
# else:
# print("НЕТ")

# Подвиг 5
# a = int(input())
# if a % 10 == 7:
#     print('ДА')
# else:
#     print('НЕТ')

# Подвиг 6
# word = input()
# if 't' in word and 'h' in word and 'o' in word:
#     print("ДА")
# else:
#     print("НЕТ")

# Подвиг 7
# text_1 = input().split()
# if 'Москва' in text_1:
#     text_1.remove('Москва')
# print(*text_1)

# Подвиг 8
# a, b, c, d = map(int, input().split())

# Определяю войдет ли открытка в конверт
# Сравниваем стороны открытки чтобы соответствовали сторонам конверта
# -1 мм, сравниваем по обоим сторонам
# if ((a-1) > c and (b-1) > d) or ((a-1) > d and (b-1) > c):
#     print('ДА') # Вывожу результат в консоль
# else:
#     print('НЕТ') # Вывожу результат в консоль

# Подвиг 9
# num = list(map(int, input()))
# if sum(num[:3]) == sum(num[3:]):
#     print('ДА')
# else:
#     print('НЕТ')

# Подвиг 10
# time_of_svet = float(input())
# Проверяю Если таймер больше 0 и меньше 3 или остаток от деления введенного времени больше 0 и меньше 3 тогда светится зеленый
# if (time_of_svet > 0 and time_of_svet < 3) or (time_of_svet % 5 > 0 and time_of_svet % 5 < 3):
#     print('green')
# else:
#     print('red')
# Логика с первым все понятно если так как первые три минуты гори зеленый то это подпадает под условия задания.
# Дальше Если при делении на 5 остаток о деления будет больше 0 но меньше трех, мы получаем значит светится зеленый сигнал светофора
# 4 % 5 = 4
