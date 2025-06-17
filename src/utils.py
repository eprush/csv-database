from collections.abc import Iterable

def file_does_exist_and_has_csv(filename: str) -> bool:
    if len(filename) >= 4 and filename[-4:] != ".csv":
        #Что-то не так с названием файла
        return False

    try:
        _ = open(filename)
    except OSError:
        #Такого файла не существует
        return False
    return True

def does_exist_column(reader: Iterable, column: str) -> bool:
    headers = next(iter(reader))
    return column in headers

