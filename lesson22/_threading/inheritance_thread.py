from threading import Thread
import logging


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        logging.debug(f'Thread args = {self.args} and kwargs = {self.kwargs}')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='(%(threadName)-10s) %(message)s',
    )
    for index in range(5):
        new_thread = MyThread(args=(index,), kwargs={index: index + 2, f"{index}": str(index) * 2})
        new_thread.start()
