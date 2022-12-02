
class Chain:

    def __init__(self, position):
        self.position = position-1
        if not self.position:
            self.next = None
        else:
            self.next = Chain(self.position)



if __name__ == '__main__':
    chain = Chain(4)
    print()