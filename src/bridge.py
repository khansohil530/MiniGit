from src.repo import repo_create

def cmd_init(args):
    repo_create(args.path)