from src.config import get_parser
from src.models import CmdArgs
from src.main import process_file
from src.view import show


def main() -> None:
    parser = get_parser()

    args = parser.parse_args()
    args = CmdArgs(file=args.file, where=args.where, aggregate=args.aggregate)

    headers, values = process_file(args)

    show(headers, values)
    return


if __name__ == "__main__":
    main()