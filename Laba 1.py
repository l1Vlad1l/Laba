import math

# ax^2 + bx + c=0
# D = b^2 - 4ac
# X1 = (-b = sqrt(D))/2a
# X2 = (-b - sqrt(D))/2a

a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
с = int(input("Введите число с:"))

D = b * b - 4 * a * с
print("Дискриминант квадратного уравнения:", D)

if D < 0:
    print("Корней нет, дискриминант < 0")

elif D == 0:
    X1 = (-b) / (2 * a)
    print("дискриминант = 0, один квадратный корень:", x1)

else:
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print("Первый корень уравнения:", x1)
    print("Второй корень уравнения:", x2)