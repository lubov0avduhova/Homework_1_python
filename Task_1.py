# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

#     Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


number = int(input("Введите число для поиска дня недели: "))

if  number > 7 or number <= 0:
    print("Нужно число из диапазона от 1 до 7 ")
elif 1 <= number <= 5:
    print("Будни")
elif 6 <= number <= 7:
    print("Выходной")
