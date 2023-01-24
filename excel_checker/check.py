class Check:
    def __init__(self, sheet):
        self.code = self._code()
        self.sheet = sheet
        self.correct = None
        self.type = self._type()
        self.error = ""

    def _code(self):
        pass

    def _type(self):
        pass

    # Code to execute during test
    def perform(self):
        pass

    def __str__(self):
        return f"{self.code}, {self.error}"

    def __repr__(self):
        return self.__str__()

    def encode(self):
        return f"< {self.code}, {self.error} >"
