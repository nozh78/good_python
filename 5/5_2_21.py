# Подвиг 2
p = [0]*10
count = 0
num = 0
while count < 6:
    num = int(input())
    if p[num] == 0:
        p[num] = 1
    count += 1
print(*p)

# test, изменения для пуша на гитхаб
