from translation.translation_service import (
    TranslationService
)


def main():

    service = TranslationService()

    result = service.translate(

        "Where is Platform Number Five?",

        "en",

        "hi"

    )

    print()

    print(result.model_dump())


if __name__ == "__main__":
    main()