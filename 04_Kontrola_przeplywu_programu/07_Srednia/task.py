numbers = []
print("Podaj n:")
n = input()
n = int(n)
for element in range(n):
    print("Podaj liczbę:")
    figure = input()
    figure = int(figure)
    numbers.append(figure)
print(f"Podane liczby {n}, {element}")
print(f"Suma {sum(numbers)}")
print(f"Średnia {sum(numbers) / len(numbers)}")
if sum(numbers) > n:
    print("Suma jest większa!")
elif sum(numbers) < n:
    print("Średnia jest większa!")
else:
    pass
