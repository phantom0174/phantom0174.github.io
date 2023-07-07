# status code translator

class STL:
    status_codes: dict

    def __init__(self, status_codes: dict) -> None:
        self.status_codes = status_codes

    def get(self, key):
        """
        key: int | str, int will be casted to str
        """
        key = str(key)
        return self.status_codes.get(key)
