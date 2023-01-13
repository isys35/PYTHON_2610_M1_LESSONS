def simple_coroutine():
    print("Я корутина")
    try:
        while True:
            value = yield
            print(value)
    except GeneratorExit:
        print("Exiting coroutine...")


item = simple_coroutine()
next(item)
item.send("Some")
