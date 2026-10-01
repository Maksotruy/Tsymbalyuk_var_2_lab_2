while True:
    try:
        data = input("Введіть цілі числа через пробіл: ").split()

        if not data:
            print("Помилка: список порожній.")
            continue

        numbers = [int(x) for x in data]

        rows = int(input("Введіть кількість рядків: "))
        cols = int(input("Введіть кількість стовпців: "))

        if rows <= 0 or cols <= 0:
            print("Помилка: кількість рядків і стовпців має бути додатною.")
            continue

        if rows * cols != len(numbers):
            print("Помилка: кількість чисел не відповідає розміру списку.")
            continue

        matrix = []
        for i in range(rows):
            matrix.append(numbers[i * cols:(i + 1) * cols])

        break

    except ValueError:
        print("Помилка: потрібно вводити тільки цілі числа.")


print("Двовимірний список:")
for row in matrix:
    print(row)

symmetric = True

for i in range(rows // 2):
    if matrix[i] != matrix[rows - 1 - i]:
        symmetric = False
        break

if symmetric:
    print("Має горизонтальну вісь симетрії")
else:
    print("Не має горизонтальної осі симетрії")