from flexudy_language_detector.language_detector_service.language_service import LanguageService
import logging

logger = logging.getLogger(__name__)


class LanguageDetector:

    def __init__(self, language_service: LanguageService):
        self.__language_service = language_service

    def get_language(self, text: str) -> str:

        try:

            predicted_language = self.__language_service.get_language(text)

        except Exception as e:

            logger.error("An error occurred while detecting the language.")

            raise e

        return predicted_language
