# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))


if quarter >= 5 or quarter <= 0:
    print('Неверная четверть')
elif quarter == 1:
    print("х > 1, y > 1")
elif quarter == 2:
    print("х < -1, y > 1")
elif quarter == 3:
    print("х < -1, y < -1")
elif quarter == 4:
    print("х > 1, y < -1")
