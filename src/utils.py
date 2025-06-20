from collections.abc import Iterable, Sequence, Sized


def has_csv_extension(filename: str) -> bool:
    """ Функция для проверки, что название файла имеет расширение ".csv". """
    return len(filename) < 4 or filename[-4:] == ".csv"



def get_headers(reader: Iterable[Sequence[str]]) -> list[str]:
    """ Функция для получения списка заголовков. """
    headers_row = next(iter(reader))
    return list(headers_row)


def does_column_exist(column_name: str, *, headers: Iterable[str]) -> bool:
    """ Функция для проверки, что данная колонка существует в заголовках."""
    return column_name in headers


def is_digital_column(column: Iterable | Sized) -> bool:
    """ Функция для проверки, что колонка содержит только числовые значения. """
    if len(column) == 0:
        raise ValueError("Column is empty")

    for value in column:
        try:
            _ = float(value)
        except ValueError:
            return False
    return True
