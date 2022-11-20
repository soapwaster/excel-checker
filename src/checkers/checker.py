import importlib
import json


class Checker:
    """
    Represents a Checker, that can either be a internal or leaf checker.
    Leaf checkers take checks as input and perform checks into che Excel document.
    Internal checkers simply contain other Checkers thus creating a tree structure

    e.g.
    WorkbookChecker
    ├── SheetChecker(Template)
    │   ├── RowChecker_1
    │   ├── ...
    │   ├── RowChecker_n
    │   └── HeadlineChecker
    └── MetadataChecker

    """

    def __init__(self, sheet, type):
        self.checkers = []
        self.sheet = sheet
        self.type = type
        self.checks = []
        self.executed = False
        self.checkerErrors = {}
        self.checkerErrorNumber = {}
        self.checkCodeError = {}
        self.checkCodeErrorNumber = {}

    def addChecker(self, checker):
        self.checkers.append(checker)

    def check(self):
        """
        Resursively visits the checkers of the Tree and performs their checks
        """
        # for each checker call check, take the resulting errors and add them to this
        for checker in self.checkers:
            checker.check()
            self.checkerErrors.setdefault(checker.type, []).append(checker)
            for k, v in checker.checkerErrorNumber.items():
                self.checkerErrorNumber.setdefault(k, 0)
                self.checkerErrorNumber[k] += v
            for k, v in checker.checkCodeErrorNumber.items():
                self.checkCodeErrorNumber.setdefault(k, 0)
                self.checkCodeErrorNumber[k] += v

        # if checks are present (used within leaf Checkers), perform check for each of them
        for check in self.checks:
            check.perform()

            # if the check fails, add it to the list of errors
            if not check.correct:
                self.checkerErrors.setdefault(check.type, []).append(check)
                self.checkCodeError.setdefault(check.code, []).append(check)

        # if it is a leaf checker, add the number of errors to the dict
        if not self.checkers:
            self.checkerErrorNumber = {
                k: len(v) for k, v in self.checkerErrors.items() if v
            }
            self.checkCodeErrorNumber = {
                k: len(v) for k, v in self.checkCodeError.items() if v
            }

        self.executed = True

    def _checksFromList(self, checkList, row=None):
        """
        Creates  a list of Check instances staring from a list of string

        Args:
            checkList (List[str]): list of strings representing the checks to be performed by this checker.
                                   The string must be the name of one of the classes in the check package

            row (int, optional): The row to which this checker has to be applied. Defaults to None.

        Returns:
            List[Check]: list of Check instances, to be performed by the checker
        """
        checks = []
        for check in checkList:
            module = importlib.import_module(f"checks.{check}")
            class_ = getattr(module, check)
            instance = class_(self.sheet, row)
            checks.append(instance)
        return checks

    def exportCheckResult(self, filepath):
        if not self.executed:
            raise Exception("Run check first")

        # save the result in a JSON file
        f = open(f"{filepath}", "w")
        json_dump = json.dumps(
            self.checkerErrors, default=lambda o: o.encode(), indent=4
        )
        f.write(json_dump)
        f.close()

    def __str__(self):
        """
        string representation of the checker
        Returns:
            str: the checkerErrors dictionary by removing those <key, value> which have [] as value (i.e. no error)
        """
        x = {k: v for k, v in self.checkerErrors.items() if v}
        return f"{x}"

    def __repr__(self):
        return self.__str__()

    def encode(self):
        """
        dict representation of Checker

        Returns:
            dict: same of __str__, but used for json.dump
        """
        return {k: v for k, v in self.checkerErrors.items() if v}
