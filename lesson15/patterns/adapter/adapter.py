from init_objects import AudioPlayer, VideoPlayer, GameConsole


class SourceAudioPlayer(AudioPlayer):

    def source_play(self):
        self.play_audio()


class SourceVideoPlayer(VideoPlayer):

    def source_play(self):
        self.play_video()


class SourceGameConsole(GameConsole):

    def source_play(self):
        if input("Вы действительно хотите запустить игру?") == 'Да':
            self.play_game()


class TV:

    def __init__(self, source):
        self.source = source

    def play(self):
        self.source.source_play()


if __name__ == '__main__':
    TV((
           SourceGameConsole(),
           SourceVideoPlayer(),
           SourceAudioPlayer(),
           SourceAudioPlayer()
       )[int(input("Введите индекс устройства"))]).play()
