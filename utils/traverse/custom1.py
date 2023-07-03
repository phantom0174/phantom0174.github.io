from io import TextIOWrapper
from traverser import Response


def custom1(file_path: str, file: TextIOWrapper, responser: Response):
    responser.add("s/101", {
        "path": file_path
    })
