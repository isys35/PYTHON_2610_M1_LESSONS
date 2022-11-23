def multiply(num1):
    var = 10

    def inner(num2):
        return num1 * num2

    return inner


if __name__ == '__main__':
    multiply_by_10 = multiply(10)
    print(multiply_by_10(54))
