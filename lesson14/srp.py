class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class FileManager:

    @classmethod
    def save_to_file(cls, journal, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(str(journal))


if __name__ == '__main__':
    j = Journal()
    j.add_entry("День 1. Я съел жука.")
    j.add_entry("День 2. Мне плохо.")
    FileManager.save_to_file(j, "journal2.txt")
    print(j)
