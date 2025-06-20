import argparse

def get_parser() -> argparse.ArgumentParser:
    """ Функция для настройки парсинга аргументов командной строки. """
    parser = argparse.ArgumentParser(description="Фильтрация и агрегация данных из CSV файла")
    parser.add_argument("--file", required=True, help="CSV файл для обработки")
    parser.add_argument("--where", help="""
        Фильтрация по колонке.
        Могут использоваться операторы >, =, <.
        Таким образом, значение может быть в одном из представленных видов: 
        column=value ,
        column>value ,
        column<value .
        """
    )
    parser.add_argument("--aggregate", help="""
        Агрегация по колонке.
        Значение в виде <column>=<value>
        """
    )
    return parser
