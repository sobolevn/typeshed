from typing import Any
from _typeshed import Incomplete

RegionData: Any

def regions(**kw_params): ...
def connect_to_region(region_name, **kw_params): ...
def get_region(region_name, **kw_params): ...

# Explicitly mark this package as incomplete.
def __getattr__(name: str) -> Incomplete: ...
