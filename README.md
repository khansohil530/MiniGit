Simple <b>Version Control System</b> build on `git` implementation.
The main purpose is learning the interal working of original VCS `git`.

Commands Available:

- [x] [`init`](https://git-scm.com/docs/git-init)
- [x] [`cat-file`](https://git-scm.com/docs/git-cat-file)
- [x] [`hash-object`](https://git-scm.com/docs/git-hash-object)
- [ ] [`add`](https://git-scm.com/docs/git-add)
- [ ] [`check-ignore`](https://git-scm.com/docs/git-check-ignore)
- [ ] [`checkout`](https://git-scm.com/docs/git-checkout)
- [ ] [`commit`](https://git-scm.com/docs/git-commit)
- [ ] [`log`](https://git-scm.com/docs/git-log)
- [ ] [`ls-files`](https://git-scm.com/docs/git-ls-files)
- [ ] [`ls-tree`](https://git-scm.com/docs/git-ls-tree)
- [ ] [`rev-parse`](https://git-scm.com/docs/git-rev-parse)
- [ ] [`rm`](https://git-scm.com/docs/git-rm)
- [ ] [`show-ref`](https://git-scm.com/docs/git-show-ref)
- [ ] [`status`](https://git-scm.com/docs/git-status)
- [ ] [`tag`](https://git-scm.com/docs/git-tag)


# Usage

## Setup
- Add src module to path
    ```bash
    export PYTHONPATH="$(pwd)"
    ```
- Make the `minigit` file executeable to use as CLI command
    ```bash
    chmod +x src/minigit
    ```
## Commands

Use `-h` or `--help` flag to list available commands
```bash
src/minigit --help
```

To get list of available sub commands and options on command
```bash
src/minigit {cmd} --help
```