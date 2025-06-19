from collections.abc import Iterable, Sequence


def has_csv_extension(filename: str) -> bool:
    return len(filename) < 4 or filename[-4:] == ".csv"


def parse_row(row: Sequence[str], *, is_headers: bool = False) -> list[str]:
    result = row[0].strip().split(";")
    if is_headers:
        result[0] = result[0][3:]
    return result


def get_headers(reader: Iterable[Sequence[str]]) -> list[str]:
    headers_row = next(iter(reader))
    return parse_row(headers_row, is_headers=True)


def does_column_exist(column_name: str, *, headers: Iterable[str]) -> bool:
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
