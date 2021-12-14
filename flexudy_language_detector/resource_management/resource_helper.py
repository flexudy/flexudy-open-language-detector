import os
import fasttext
import urllib.request
from typing import Optional


class ResourceHelper:
    MODEL_FILE_NAME = "lid.176.bin"

    DEFAULT_MODEL_URL = "https://dl.fbaipublicfiles.com/fasttext/supervised-models/"

    def __init__(self, model_url: Optional[str] = None, model_file: Optional[str] = None):
        if model_url is None:
            model_url = self.DEFAULT_MODEL_URL

        if model_file is None:
            model_file = self.MODEL_FILE_NAME

        local_model_path = self.__get_resource_path("language_detection_model/")

        self.__fast_text_language_identifier = self.__load_language_detector_model(local_model_path, model_url,
                                                                                   model_file)

    def __load_language_detector_model(self, path_to_model_folder: str, model_url: str, model_file: str):
        self.__download_resources(path_to_model_folder, model_url, model_file)

        model = fasttext.load_model(path_to_model_folder + model_file)

        return model

    def __download_resources(self, path_to_model_folder: str, model_url: str, model_file: str) -> None:
        if model_file not in os.listdir(path_to_model_folder):
            urllib.request.urlretrieve(model_url + model_file, path_to_model_folder + model_file)

    def __get_resource_path(self, file_name: str) -> str:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

    def get_fast_text_lang_identifier(self):
        return self.__fast_text_language_identifier
