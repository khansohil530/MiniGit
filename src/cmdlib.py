import sys

from src.argslib import get_option_parser
from src.bridge import cmd_init


def main(argv=sys.argv[1:]):
    args = get_option_parser().parse_args(argv)
    match args.command:
        case "init"         : cmd_init(args)
        case _              : print("Bad command.")

