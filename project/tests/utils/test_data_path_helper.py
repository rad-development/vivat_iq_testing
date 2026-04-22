from src.utils.path_utils import PathUtils

class TestDataPathHelper:
    @staticmethod
    def get_test_data_file_path(TC_folder_name: str, filename: str) -> str:
        path = PathUtils.get_path_from_root(f"tests/test_cases/{TC_folder_name}/{filename}")
        if not path.exists():
            raise FileNotFoundError(f"JSON file not found: {path}")
        return str(path)
    