from recorder import AudioRecorder


def main():
    recorder = AudioRecorder()

    input("Press ENTER to start recording...")

    recorder.start()

    input("Press ENTER to stop recording...")

    recorder.stop()


if __name__ == "__main__":
    main()