import os
import zlib
import hashlib

from src.utils import repo_file


def object_find(repo, name, fmt=None, follow=True):
    """
    Name resolution of objects using full hash, short hash, tags, etc.
    """
    # TODO implement rest of ways to resolve
    return name

def object_hash(fd, fmt, repo=None):
    """
    Hash object, writing to repo if provided
    """
    
    data = fd.read()
    
    # Choose constructor according to fmt argument
    match fmt:
        # case b'commit' : git_obj=GitCommit(data)
        # case b'tree'   : git_obj=GitTree(data)
        # case b'tag'    : git_obj=GitTag(data)
        case b'blob'   : git_obj=GitBlob(data)
        case _: raise Exception(f"Unknown type {fmt}!")

    return object_write(git_obj, repo)

def object_write(git_obj, repo=None):
    data = git_obj.serialize()
    # Add header
    result =  git_obj.fmt + b' ' + str(len(data)).encode('ascii') + b'\x00' + data
    
    # compute hash
    sha = hashlib.sha1(result).hexdigest()
    if repo:
        path = repo_file(repo, "objects", sha[0:2], sha[2:], mkdir=True)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(zlib.compress(result))
    
    return sha    


def object_read(repo, sha):
    """
    Read object sha from Git repository repo.  Return a
    GitObject whose exact type depends on the object.
    """
    path = repo_file(repo, "objects", sha[0:2], sha[2:])
    if not os.path.isfile(path):
        return None
    
    with open(path, 'rb') as f:
        raw = zlib.decompress(f.read())
        
        # Read object type
        header_offset = raw.find(b' ')
        fmt = raw[0:header_offset]
        
        # Read and validate object size
        object_offset = raw.find(b'\x00', header_offset)
        size = int(raw[header_offset:object_offset].decode('ascii'))
        if size != len(raw) - object_offset - 1:
            raise Exception(f"Malformed object {sha}: bad length")
        
        # Pick constructor
        match fmt:
            # case b'commit' : git_obj=GitCommit
            # case b'tree'   : git_obj=GitTree
            # case b'tag'    : git_obj=GitTag
            case b'blob'   : git_obj=GitBlob
            case _:
                raise Exception(f"Unknown type {fmt.decode("ascii")} for object {sha}")
    
        return git_obj(raw[object_offset+1:])


class GitObject:
    def __init__(self, data=None):
        if data is None:
            self.init()
        else:
            self.deserialize(data)
    
    def serialize(self, repo):
        raise NotImplementedError()
    
    def deserialize(self, data):
        raise NotImplementedError()
    
    def init(self):
        pass

class GitBlob(GitObject):
    fmt = b'blob'
    
    def serialize(self):
        return self.blobdata
    
    def deserialize(self, data):
        self.blobdata = data