"""Package metadata for tessilator."""

import importlib.metadata

try:
    __version__ = importlib.metadata.version('tessilator')
except importlib.metadata.PackageNotFoundError:
    # Source-tree import without installed package metadata.
    pass
