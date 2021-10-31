import os
import fasttext


class ResourceHelper:

    def __init__(self, model_file_name: str = "lid.176.ftz"):
        model_path = self.__get_resource_path("language_detection_model/")

        self.__fast_text_language_identifier = self.__load_language_detector_model(model_path, model_file_name)

    def __load_language_detector_model(self, path_to_model_folder: str, file_name: str):
        model = fasttext.load_model(path_to_model_folder + file_name)

        return model

    def __get_resource_path(self, file_name: str) -> str:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    def get_fast_text_lang_identifier(self):
        return self.__fast_text_language_identifier
