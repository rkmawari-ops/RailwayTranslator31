from ai.manager import AIManager


def main():

    manager = AIManager()

    print()

    print("Loaded Models")

    for model in manager.registry.list_models():
        print(" -", model)

    print()

    whisper = manager.get_model("whisper")

    print(type(whisper))


if __name__ == "__main__":
    main()