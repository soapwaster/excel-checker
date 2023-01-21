from enum import Enum


class CheckerType(str, Enum):
    ROW = "ROW"
    SHEET = "SHEET"
    DOCUMENT = "DOCUMENT"
    METADATA = "METADATA"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
