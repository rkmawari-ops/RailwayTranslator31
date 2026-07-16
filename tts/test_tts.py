from tts.parler_engine import ParlerEngine


def main():

    engine = ParlerEngine()

    text = input("Enter Text : ")

    result = engine.synthesize(
        text=text,
        filename="test.wav",
    )

    print(result)


if __name__ == "__main__":
    main()