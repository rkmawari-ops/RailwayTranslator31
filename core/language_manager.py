LANGUAGE_NAMES = {

    "en": "English",

    "hi": "Hindi",

    "ta": "Tamil",

    "te": "Telugu",

    "ml": "Malayalam",

    "kn": "Kannada",

    "mr": "Marathi",

    "gu": "Gujarati",

    "bn": "Bengali",

    "pa": "Punjabi",

    "or": "Odia",

    "as": "Assamese",

    "ur": "Urdu",

}


def get_language_name(code):

    return LANGUAGE_NAMES.get(code, code)