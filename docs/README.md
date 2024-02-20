
# Creating repository: `init`

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

# Reading and writing objects: `hash-object` and `cat-file`

## What are objects?

At core git is a `content-addressed filesystem`, which means the name of files stored by `Git` are mathematically derived from their contents. This way, <b><u>if a single byte change will change the internal filename.</u></b>
This will lead to creation of new git file for changes in original file. These internal files are called `Git Objects` or simply `Objects`.

`Objects` are used to store a lot of things like,
- actual files
- commits
- tags

With a few exception, almost everything in Git is stored as `object`.

The path where git stores a given object is computed using `sha1` hash of its content. More precisely
- Git renders the hash as lowercase hexadecimal string
- Splits the string into two parts:
    - First two characters as directory name
    - Rest of the string as file name.

    This is done because filesystem slows down on having tow many files in single directoy. With this implementation, we'll have 256 possible intermediate directories.

> `sha1` hash is used because it pratically guaranatees unique hash for each file but that's old. Git uses different [hardend variant](https://github.com/git/git/blob/26e47e261e969491ad4e3b6c298450c061749c9e/Documentation/technical/hash-function-transition.txt#L34-L36) of sha1 to hash. Also [`sha1`](https://shattered.io/) has been broken already.   


# TODO understand exact storage format [here](https://wyag.thb.lt/#org279a578)

An object storage format :
- starts with a header that specifies the type, i.e. `blob`, `commit`, `tag` or `tree`.
- (0x20) ascii space
- size of object in bytes as ASCII
- null (0x00)
- content of object

## Generic Objects

Objects can be of multiple types, but shares same storage/retrieval mechanism and some general header format. This can be abstracted out in a common generic class

Git has 4 object types, `blob`, `commit`, `tag` and `tree`

1. `blob`:
    - user data, basically content of every file we need in git
    - have not actual format since they're just unspecified data, so serializing and deserialing are trivial

2. 

## `cat-file`

FORMAT: `git cat-file TYPE OBJECT`

- Prints an existing git object to standard output
- mainly used internally by git to manage objects


## `hash-object`

FORMAT: `git hash-object [-w] [-t TYPE] FILE`

- converts existing file into a git object
- if `-w` flag is passed, it'll write the object in repository else it'll just print the hash


## `packfiles`

Git has second object storage mechanism called `packfiles` which are must more efficient than directly storing object mentioned above (known as `loose objects`). 

TODO: read more about packfile, unimplemented as of now

