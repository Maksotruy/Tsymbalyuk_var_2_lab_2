while True:
    try:
        secret = int(input("Петро загадує число від 1 до 100: "))

        if secret < 1 or secret > 100:
            print("Помилка: число має бути від 1 до 100.")
            continue

        break

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


while True:
    try:
        attempts = int(input("Введіть кількість спроб: "))

        if attempts <= 0:
            print("Помилка: кількість спроб має бути додатною.")
            continue

        break

    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


possible = set(range(1, 101))

for i in range(attempts):

    while True:
        try:
            data = input("Олена вводить числа через кому з пробілом або HELP: ").strip()

            if data.upper() == "HELP":
                print("Можливі числа:", *sorted(possible))
                continue

            if not data:
                print("Помилка: введення порожнє.")
                continue

            numbers = set(map(int, data.split(",")))

            if any(x < 1 or x > 100 for x in numbers):
                print("Помилка: числа мають бути від 1 до 100.")
                continue

            break

        except ValueError:
            print("Помилка: вводити можна тільки цілі числа через кому.")

    if secret in numbers:
        print("Yes")
        possible &= numbers
    else:
        print("No")
        possible -= numbers


print("HELP")
print("Можливі числа:", *sorted(possible))