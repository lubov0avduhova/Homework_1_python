import math

#     Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

#     Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def input_num():
    num = int(input("Введите число "))
    return num


def find_distance(first_x, second_x, first_y, second_y):
    return math.sqrt(((second_x - first_x) ** 2) + ((second_y - first_y) ** 2))


first_x = input_num()
first_y = input_num()

second_x = input_num()
second_y = input_num()

result = find_distance(first_x, second_x, first_y, second_y)

print(f"Результат: {round(result,3)}")
