import json
from typing import Type, Any
from pathlib import Path
from pydantic import TypeAdapter, BaseModel
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from src.constants.encoding_types import EncodingTypes


class JsonUtils:
    @staticmethod
    def read_json(path: str | Path):
        if isinstance(path, Path):
            path_obj = path
        else:
            path_obj = Path(path)
            if not path_obj.is_absolute():
                tests_root = Path(RootPathHelper.calling_root_path())
                path_obj = tests_root / path_obj
        path_obj = path_obj.resolve()
        if not path_obj.exists():
            raise FileNotFoundError(f"JSON file not found: {path_obj}")
        with open(path_obj, "r", encoding=EncodingTypes.UTF8.value) as f:
            return json.load(f)

    @staticmethod
    def parse_model(data: Any, model_class: Type[BaseModel]) -> BaseModel:
        adapter = TypeAdapter(model_class)
        return adapter.validate_python(data)
    