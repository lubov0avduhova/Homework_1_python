# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def disjunction (num1, num2):
# пример X ⋁ Y
    if num1 == 0 and num2 == 0:
        return False
    elif num1 == 0 and num2 == 1:
        return True

def conjunction (num1, num2):
#пример Y ⋀ Z
    if num1 == 0:
        return False
    elif num1 == 1 and num2 == 0:
        return False
    else: return True

def denial (num):
#пример ¬X
    if num == 0:
        return True
    else:
        return False

def input_num ():
    num = bool(input('Введите число от нуля до одного '))
    return num


num_x = input_num()
num_y = input_num()
num_z= input_num()

print ("\nПроверяем первое утверждение: ¬(X ⋁ Y ⋁ Z)")

truth_first = disjunction(num_x, num_y)
truth_first = disjunction(truth_first, num_y)
truth_first = denial(truth_first)
print (f"В первом выражении получилось {truth_first}")

print ("\nПроверяем второе утверждение: ¬X ⋀ ¬Y ⋀ ¬Z")

num_x = denial(num_x)
num_y = denial(num_y)

truth_second = conjunction(num_x, num_y)
num_z = denial(num_z)
truth_second = conjunction(truth_second,num_z)
print (f"В первом выражении получилось {truth_second}")

print (f'Ответ: {truth_first} и {truth_second}')