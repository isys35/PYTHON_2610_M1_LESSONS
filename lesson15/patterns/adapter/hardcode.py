from init_objects import AudioPlayer, VideoPlayer, GameConsole



class TV:

    def __init__(self, source):
        self.source = source

    def play(self):
        if isinstance(self.source, GameConsole):
            if input("Вы действительно хотите запустить игру?") == 'Да':
                self.source.play_game()
        elif isinstance(self.source, VideoPlayer):
            self.source.play_video()
        elif isinstance(self.source, AudioPlayer):
            self.source.play_audio()


if __name__ == '__main__':
    TV((
           GameConsole(),
           VideoPlayer(),
           AudioPlayer(),
           AudioPlayer()
       )[int(input("Введите индекс устройства"))]).play()
