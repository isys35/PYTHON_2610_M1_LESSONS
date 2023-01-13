from threading import Thread


def thread_work(name):
    print(name)


if __name__ == '__main__':
    for i in range(5):
        thread = Thread(target=thread_work, args=(f"Thread #{i}",))
        thread.start()

