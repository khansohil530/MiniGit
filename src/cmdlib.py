import sys

from src.argslib import get_option_parser
from src import bridge


def main(argv=sys.argv[1:]):
    args = get_option_parser().parse_args(argv)
    match args.command:
        case "init"         : bridge.cmd_init(args)
        case "cat-file"     : bridge.cmd_cat_file(args)
        case "hash-object"  : bridge.cmd_hash_object(args)
        case _              : print("Bad command.")

