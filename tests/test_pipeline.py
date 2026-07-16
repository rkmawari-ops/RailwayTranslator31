from pipeline.controller import PipelineController


def main():

    controller = PipelineController()

    controller.process_audio(

        "assets/recordings/20260716_140635.wav"

    )


if __name__ == "__main__":

    main()