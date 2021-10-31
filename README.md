# flexudy-open-language-detector
This language detector is a wrapper of Facebook's Fasttext Language Identifier.
Minor edge cases are handled.

```python
from flexudy_language_detector.start import FlexudyLanguageDetectorFactory

language_detector = FlexudyLanguageDetectorFactory.get_flexudy_language_detector()

text = "He is a happy fellow."

language = language_detector.get_language(text)

print(language)
```
