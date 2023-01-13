import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print('In {}'.format(self.name))


if __name__ == '__main__':
    for i in range(5):
        p = Worker()
        p.start()

