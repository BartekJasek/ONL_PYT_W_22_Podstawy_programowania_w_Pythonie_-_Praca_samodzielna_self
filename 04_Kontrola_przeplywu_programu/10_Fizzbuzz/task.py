for element in range(1, 101):
    if (element % 3 == 0) and (element % 5 == 0):
        print("FizzBuzz")
    elif (element % 5 == 0):
        print("Buzz")
    elif (element % 3 == 0):
        print("Fizz")
    else:
        print(element)
