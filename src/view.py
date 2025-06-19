from tabulate import tabulate

from src.command_handlers.abstract_handler import ProcessedData

def show(values: ProcessedData) -> None:
    """ Функция для вывода данных на печать. """
    print(tabulate(values, headers="keys", tablefmt="outline"))
