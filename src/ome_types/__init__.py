from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("ome-types-widget")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
