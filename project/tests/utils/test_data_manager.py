from typing import Type
from pydantic import BaseModel
from py_selenium_auto_core.logging.logger import Logger

from src.utils.json_to_model_loader import JsonToModelLoader

class TestDataManager:
    __datasets = {}

    @classmethod
    def get_dataset(cls, model_class: Type[BaseModel]):
        if model_class in cls.__datasets:
            Logger.info(f"Test data loaded from cache: model='{model_class.__name__}'")
            return cls.__datasets[model_class]
        
        if not hasattr(model_class, "data_file"):
            raise AttributeError(f"{model_class.__name__} must define data_file() method")

        json_file_path = model_class.data_file()
        Logger.info(f"Loading test data from file: path='{json_file_path}', model='{model_class.__name__}'")

        data = JsonToModelLoader.get(json_file_path, model_class)
        cls.__datasets[model_class] = data
        return data

    @classmethod
    def get_single(cls, model_class: Type[BaseModel]) -> BaseModel:
        dataset = cls.get_dataset(model_class)
        if not dataset:
            raise ValueError(f"No test data found for model '{model_class.__name__}'")
        return dataset[0]
