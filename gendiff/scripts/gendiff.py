from ..modules.generate_diff import generate_diff
from ..modules.parse_args_cli import parse_args


def main():
    args = parse_args()
    return generate_diff(args.first_file, args.second_file, args.format)


if __name__ == "__main__":
    main()