import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Фильтрация и агрегация данных из CSV файла")
    parser.add_argument("--file", required=True, help="CSV файл для обработки")
    parser.add_argument("--where", help="""
        Фильтрация по колонке.
        Значение в виде <column>?<value>.
        В качестве знака сравнения ? могут быть знаки (>, =, <)
        """
    )
    parser.add_argument("--aggregate", help="""
        Агрегация по колонке.
        Значение в виде <column>=<value>
        """
    )
    return parser
