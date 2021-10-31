from distutils.core import setup
import setuptools

setup(
    name='flexudy-language-detector',
    version='0.0.1',
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={"flexudy_language_detector.resource_management.language_detection_model": ["location.resource",
                                                                                             "lid.176.bin"]},
    url='https://flexudy.com',
    license='',
    author='Flexudy Education',
    author_email='support@flexudy.com',
    description='Module that detects the languages using Facebook\'s Fasttext Library'
)
