from collections.abc import Iterable


def has_csv_extension(filename: str) -> bool:
    return len(filename) < 4 or filename[-4:] == ".csv"


def does_column_exist(reader: Iterable, column_name: str) -> bool:
    headers = next(iter(reader))
    return column_name in headers
