while True:
    try:
        numbers = list(map(int, input("Введіть не менше 5 цілих чисел через пробіл: ").split()))

        if len(numbers) < 5:
            print("Помилка: потрібно ввести не менше 5 чисел.")
            continue

        break

    except ValueError:
        print("Помилка: вводити можна тільки цілі числа.")

numbers.sort(reverse=True)

result = sum(x ** 3 for x in numbers[:5])

print("Сума кубів 5 найбільших елементів:", result)