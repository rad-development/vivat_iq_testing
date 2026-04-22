from pathlib import Path

class PathUtils:
    DEFAULT_PARENT_LEVEL = 2
    PROJECT_MARKERS = [".git", "pyproject.toml"]

    @staticmethod
    def get_project_root() -> Path:
        current = Path(__file__).resolve()
        for parent in current.parents:
            for marker in PathUtils.PROJECT_MARKERS:
                if (parent / marker).exists():
                    return parent
        return Path(__file__).resolve().parents[PathUtils.DEFAULT_PARENT_LEVEL]

    @staticmethod
    def get_path_from_root(relative_path: str) -> Path:
        return (PathUtils.get_project_root() / relative_path).resolve()