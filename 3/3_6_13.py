# Подвиг 3
# lst = list(map(int, input().split()))
# print(lst)

# Подвиг 4
# cities = input().split()
# print('Москва' in cities)

# Подвиг 6
# cities = input().split()
# print(cities[-1])

# Подвиг 7
# marks = list(map(int, input().split()))
# marks_sr = sum(marks) / len(marks)
# print(round(marks_sr, 1))

# Подвиг 8
# title = input()
# autor = input()
# pages = int(input())
# sales = float(input())
# book = [title, autor, pages, sales]
# print(book)
# del (book[2])
# book[1] = 'Пушкин'
# book[2] *= 2
# print(book)

# Подвиг 9
# Сохраняем данные в перемененную
# people = list(map(int, input().split()))
# Выводим максимальное, минимальное значения и сумму числе в списке
# print(f"{max(people)} {min(people)} {sum(people)}")

# Подвиг 10
# Сохраняем данные в перемененную
# lst = list(map(int, input().split()))
# # С помощью функции sorted() сортируем список по возрастанию и с помощью параметра reverse=True переворачиваем его.
# lst = sorted(lst, reverse=True)
# # Выводим списко без скобок и запятых.
# print(*lst)

# Подвиг 12
# lst = list(input().split())
# Создание объекта списка городов, на который ссылается имя cities:
# cities = ["Москва", "Тверь", "Вологда"]
# Создание нового объекта с именем lst, содержащего объект списка cities с добавленным старым списком lst в конец:
# lst = cities + lst
# Вывод нового объекта списка *lst:
# print(*lst)

# Подвиг 13
# lst = list(input().split())
# cities = ["Москва", "Тверь", "Вологда"]
# lst = lst + cities
# print(*lst)
