import csv
from typing import Literal

from src.utils import has_csv_extension, does_column_exist, get_headers
from src.models import CmdArgs
from src.command_handlers.abstract_handler import AbstractCommandHandler, ProcessedData
from src.command_handlers.filter import Filter
from src.command_handlers.aggregator import Aggregator

CommandHandlers = tuple[AbstractCommandHandler | None, ...]


def _get_data_from_file(filename: str, *, sep: Literal[",", ";"] = ",") -> ProcessedData:
    """ Функция для получения данных из CSV файла. """

    if has_csv_extension(filename):
        try:
            file =  open(filename, "r")
        except OSError:
            raise FileNotFoundError(f"Couldn't open the file with {filename=}")
    else:
        raise ValueError(f"Invalid file extension for {filename=}")

    with file as f:
        csvreader = csv.reader(f, delimiter=sep, skipinitialspace=True)
        headers = get_headers(csvreader)

        column_to_indices = {col: idx for idx, col in enumerate(headers)}
        column_to_values = {col: [] for col in headers}
        for value in csvreader:
            for col, idx in column_to_indices.items():
                column_to_values[col].append(value[idx])
    return column_to_values


def process_file(args: CmdArgs) -> ProcessedData:
    """ Основной скрипт обработки. """

    # Указываем обработчиков команд в нужном порядке
    handlers: CommandHandlers = (
        Filter(args.where) if args.where is not None else None,
        Aggregator(args.aggregate) if args.aggregate is not None else None,
    )

    processed_data = _get_data_from_file(args.file)
    for handler in handlers:
        if handler is None:
            continue

        column, sign, param = handler.parse_command()
        if not does_column_exist(column, headers=processed_data.keys()):
            raise ValueError(f"Invalid column for {handler.name} command: {column=}")

        processed_data = handler.process(processed_data, column=column, sign=sign, param=param)
    return processed_data
