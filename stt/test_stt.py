from speech_to_text import SpeechToText


def main():

    audio_file = input("Enter audio path: ")

    stt = SpeechToText()

    result = stt.transcribe(audio_file)

    if result["status"] == "error":

        print("\nERROR")
        print("----------------------------")
        print(result["message"])
        return

    print("\n======================================")
    print("       Speech Recognition Result")
    print("======================================")

    print(f"Status            : {result['status']}")
    print(f"Timestamp         : {result['timestamp']}")
    print(f"Audio File        : {result['audio_file']}")
    print(f"Detected Language : {result['language']}")
    print(f"Confidence        : {result['confidence']} %")

    print("\nRecognized Text")
    print("--------------------------------------")
    print(result["recognized_text"])

    print("\nProcessing Time")
    print("--------------------------------------")
    print(f"{result['processing_time']} seconds")


if __name__ == "__main__":
    main()
    