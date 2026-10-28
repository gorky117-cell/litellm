import importlib
from types import ModuleType

from . import *
from . import _router_host as _router_host  # installs the proxy's RouterHost on import


def __getattr__(name: str) -> ModuleType:
    if name == "_types":
        return importlib.import_module("litellm.proxy._types")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
