import simpleaudio as sa


class AudioPlayer:

    def play(self, audio_path):

        print(f"\nPlaying : {audio_path}")

        wave = sa.WaveObject.from_wave_file(audio_path)

        play = wave.play()

        play.wait_done()