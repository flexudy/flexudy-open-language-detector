from flexudy_language_detector.language_detector import LanguageDetector
from flexudy_language_detector.language_detector_service.fasttext_language_service import FastTextLangService
from flexudy_language_detector.resource_management.resource_helper import ResourceHelper
from typing import Optional


class FlexudyLanguageDetectorFactory:

    @staticmethod
    def get_flexudy_language_detector(model_url: Optional[str] = None,
                                      model_file: Optional[str] = None) -> LanguageDetector:
        resource_helper = ResourceHelper(model_url, model_file)

        language_detector_service = FastTextLangService(resource_helper)

        language_detector = LanguageDetector(language_detector_service)

        return language_detector
