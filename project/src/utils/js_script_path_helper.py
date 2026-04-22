from pathlib import Path
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper
from py_selenium_auto_core.utilities.file_reader import FileReader


class JsScriptPathHelper:
    FOLDER_NAME = "js_scripts"

    @staticmethod
    def get_js_script_file_path(script_name: str) -> str:
        root = RootPathHelper.calling_root_path()
        js_script_path = FileReader.get_resource_file_path(
            str(Path(JsScriptPathHelper.FOLDER_NAME, script_name)),
            root
        )
        return js_script_path
    