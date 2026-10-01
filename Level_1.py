numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

result = sum(x ** 3 for x in numbers[:5])

print(result)