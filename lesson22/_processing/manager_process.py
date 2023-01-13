from multiprocessing import Process, Manager, Event


def slave(namespace, event):
    namespace.my_list.append(1)
    namespace.my_list.append(2)
    namespace.my_list.append(3)
    namespace.my_list.append("new value")
    namespace.my_value = 3.14
    event.set()


def master(namespace, event):
    print(f'my_list до установки флага события: '
          f'{namespace.my_list}')
    print(f'my_value до установки флага события: '
          f'{namespace.my_value}')
    event.wait()
    print(f'my_list после установки флага события: '
          f'{namespace.my_list}')
    print(f'my_value после установки флага события:'
          f'{namespace.my_value}')


if __name__ == '__main__':
    manager = Manager()
    namespace = manager.Namespace()
    # общее пространство имен
    namespace.my_list = manager.list()  # создаем список
    # объявляем переменную
    namespace.my_value = manager.Value('d', 0.0)
    event = Event()
    slave_process = Process(
        target=slave,
        args=(namespace, event),
    )
    master_process = Process(
        target=master,
        args=(namespace, event),
    )
    master_process.start()
    slave_process.start()
    master_process.join()
    slave_process.join()
