from collections.abc import Iterable, Sequence, Sized
from typing import Literal


def has_csv_extension(filename: str) -> bool:
    """ Функция для проверки, что название файла имеет расширение ".csv". """
    return len(filename) < 4 or filename[-4:] == ".csv"


def parse_row(row: Sequence[str], *, sep: Literal[";", ","] = ";", is_headers: bool = False) -> list[str]:
    """ Функция для парсинга строки из файла. """
    row_str = row[0].strip()
    result = row_str.split(sep)
    if is_headers:
        result[0] = result[0][3:]
    return result


def get_headers(reader: Iterable[Sequence[str]]) -> list[str]:
    """ Функция для получения списка заголовков. """
    headers_row = next(iter(reader))
    return parse_row(headers_row, is_headers=True)


def does_column_exist(column_name: str, *, headers: Iterable[str]) -> bool:
    """ Функция для проверки, что данная колонка существует в заголовках."""
    return column_name in headers


def is_digital_column(column: Iterable | Sized) -> bool:
    """ Функция для проверки, что колонка содержит только числовые значения. """
    if len(column) == 0:
        raise ValueError("Column is empty")

    for value in column:
        try:
            float(value)
        except ValueError:
            return False
    return True
