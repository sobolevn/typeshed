from _typeshed import Incomplete

SUPPORTED_FORMATS: Incomplete

class ExcelReader:
    archive: Incomplete
    valid_files: Incomplete
    read_only: Incomplete
    keep_vba: Incomplete
    data_only: Incomplete
    keep_links: Incomplete
    shared_strings: Incomplete
    def __init__(self, fn, read_only: bool = ..., keep_vba=..., data_only: bool = ..., keep_links: bool = ...) -> None: ...
    package: Incomplete
    def read_manifest(self) -> None: ...
    def read_strings(self) -> None: ...
    parser: Incomplete
    wb: Incomplete
    def read_workbook(self) -> None: ...
    def read_properties(self) -> None: ...
    def read_theme(self) -> None: ...
    def read_chartsheet(self, sheet, rel) -> None: ...
    def read_worksheets(self) -> None: ...
    def read(self) -> None: ...

def load_workbook(filename, read_only: bool = ..., keep_vba=..., data_only: bool = ..., keep_links: bool = ...): ...
