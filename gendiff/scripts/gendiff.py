import sys

from ..modules.generate_diff import generate_diff
from ..modules.parse_args_cli import parse_args


def main():
    args = parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)
    sys.exit(0)


if __name__ == "__main__":
    main()