from lesson10.example.decorators import repeat, counter_slow


@repeat(count=10)
@counter_slow()
def print_hello(name):
    print(f"Привет, {name}")


@counter_slow()
def print_gaf(name_dog):

    print(f"{name_dog}: Гав!")


# print_hello = repeat(count=10)(print_hello)

if __name__ == '__main__':
    print_hello("Олег")