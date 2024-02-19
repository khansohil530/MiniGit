import argparse

def get_option_parser():
    argparser = argparse.ArgumentParser(description='Simple Content Tracker based on Git')
    argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
    
    argsp = argsubparsers.add_parser("init", help="Initialize a new, empty repository.")
    argsp.add_argument("path",
                       metavar="directory",
                       nargs="?",
                       default=".",
                       help="Where to create the repository.")
    
    argsubparsers.required = True
    return argparser