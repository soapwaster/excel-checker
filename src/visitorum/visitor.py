from __future__ import annotations
from abc import ABC, abstractmethod

class Visitor(ABC):

    @abstractmethod
    def visit_workbook(self, element: CWorkbook) -> None:
        pass

    @abstractmethod
    def visit_worksheet(self, element: CWorksheet) -> None:
        pass
    
    @abstractmethod
    def visit_row(self, element: CRow) -> None:
        pass

    @abstractmethod
    def visit_col(self, element: CCol) -> None:
        pass

    @abstractmethod
    def visit_cell(self, element: CCell) -> None:
        pass