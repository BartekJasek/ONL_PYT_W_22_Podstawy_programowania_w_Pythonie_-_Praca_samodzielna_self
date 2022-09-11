print("Podaj pierwszą liczbe:")
a = input()
first = float(a)
print("Podaj drugą liczbe:")
b = input()
second = float(b)
if first > second:
    print(f"a jest większe!")
elif first < second:
    print(f"b jest większe!")
else:
    pass
