try:
    x = int(input("Please enter a number: "))
    y = int(input("Please enter another number: "))
    result = x // y
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)
finally:
    # Будет выполнятся всегда
    print('This is always executed')
