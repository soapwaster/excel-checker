from enum import Enum


class CheckError(str, Enum):
    WARNING = "WARNING"
    BLOCKING = "BLOCKING"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
