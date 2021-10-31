from flexudy_language_detector.language_detector import LanguageDetector
from flexudy_language_detector.language_detector_service.fasttext_language_service import FastTextLangService
from flexudy_language_detector.resource_management.resource_helper import ResourceHelper


class FlexudyLanguageDetectorFactory:

    @staticmethod
    def get_flexudy_language_detector() -> LanguageDetector:
        resource_helper = ResourceHelper()

        language_detector_service = FastTextLangService(resource_helper)

        language_detector = LanguageDetector(language_detector_service)

        return language_detector
