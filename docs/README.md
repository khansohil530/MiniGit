
# Creating repo. `init`

- made of two things:
    - `work tree`: directory where files of version control lives
    - `git directory`: directory where git stores it data
- `creating new repo`:
    - verify that `worktree` directory is present and contains subdirectory `.git`
    - check the `.git/config` (INI file) has `core.repositoryformatversion` 0

- `gitdir` contains following:
    - `/objects/`: object store
    - `refs/`: reference store
        - `/heads`:
        - `/tags`: 
    - `/HEAD`: references to current HEAD
    - `/config`: repository's configuration file in INI format
    - `/description`: holds free-form description of repo's contents for humans, rarely used

- `.git/config` file is a simple INI like file with single section `core` and three fields:
    - `repositoryformatversion=0`: version of gitdir format, 0 means initial format, 1 the same with extensions.
    - `filemode=False`: disable tracking of file modes changes in worktree
    - `bare=False`: indicates that this repo has `worktree`.  