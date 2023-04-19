# Подвиг 1
# a = float(input())
# b = float(input())
# d = a if a > b else b
# print(d)

# Подвиг 2
# a = int(input())
# msg = 'кратно 3' if a % 3 == 0 else 'не кратно 3'
# print(msg)

# Подвиг 3
# word = input().lower()
# msg = 'палиндром' if word == word[::-1] else 'не палиндром'
# print(msg)

# Подвиг 4
# a = int(input())
# msg = 'True' if a == 1 else 'False'
# print(msg)

# Подвиг 5
# msg = int(input())
# result = 0 if msg >= 59 else msg+1
# print(result)

# Подвиг 6
# notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
# # Сохраняю переменные в список
# number_note_1, number_note_2, number_note_3  = list(map(int, input().split()))
# # Делаю список в котором буду хранить результат
# new_list = []
# # Если номер ноты не 1 или не 4: Выводи ноту без знака #, иначе выводим ноту с знаком #
# new_list.append(f'#{notes[number_note_1-1]}' if number_note_1 == 1 or number_note_1 == 4 else f'{notes[number_note_1 - 1]}')
# new_list.append(f'#{notes[number_note_2-1]}' if number_note_2 == 1 or number_note_2 == 4 else f'{notes[number_note_2 - 1]}')
# new_list.append(f'#{notes[number_note_3-1]}' if number_note_3 == 1 or number_note_3 == 4 else f'{notes[number_note_3 - 1]}')
# # Выводим результат
# print(*new_list)
