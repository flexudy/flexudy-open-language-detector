from flexudy_language_detector.start import FlexudyLanguageDetectorFactory

language_detector = FlexudyLanguageDetectorFactory.get_flexudy_language_detector()

text = "He is a happy fellow."

language = language_detector.get_language(text)

print(language)
