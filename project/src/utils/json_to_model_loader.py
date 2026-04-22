from typing import Type
from pydantic import BaseModel

from src.utils.json_utils import JsonUtils


class JsonToModelLoader:
    @staticmethod
    def get(json_file_path: str, model_class: Type[BaseModel]):
        raw = JsonUtils.read_json(json_file_path)
        if isinstance(raw, dict):
            raw = [raw]
        elif not isinstance(raw, list):
            raise ValueError(f"Unsupported JSON format in {json_file_path}")
        return [JsonUtils.parse_model(item, model_class) for item in raw]
    