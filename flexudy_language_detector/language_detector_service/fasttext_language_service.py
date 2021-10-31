from flexudy_language_detector.resource_management.resource_helper import ResourceHelper
from flexudy_language_detector.language_detector_service.language_service import LanguageService


class FastTextLangService(LanguageService):

    def __init__(self, resource_helper: ResourceHelper):
        self.__resource_helper = resource_helper

    def get_language(self, text: str) -> str:
        language_identifier = self.__resource_helper.get_fast_text_lang_identifier()

        text = text.replace("\\n", " ")

        text = text.replace("\n", " ")

        text = " ".join(text.splitlines())

        language = language_identifier.predict(text)

        language = language[0][0]

        return language.replace("__label__", "")
