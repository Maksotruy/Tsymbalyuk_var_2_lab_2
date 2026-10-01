secret = int(input("Петро загадує число: "))
attempts = int(input("Кількість спроб: "))

possible = set(range(1, 101))

for _ in range(attempts):
    numbers = set(map(int, input("Олена вводить числа через пробіл: ").split()))

    if secret in numbers:
        print("Yes")
        possible &= numbers
    else:
        print("No")
        possible -= numbers

print("HELP")
print(*sorted(possible))