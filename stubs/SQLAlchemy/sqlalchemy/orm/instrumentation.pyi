from typing import Any

from ..util import HasMemoized, hybridmethod
from . import base

DEL_ATTR: Any

class ClassManager(HasMemoized, dict[Any, Any]):
    MANAGER_ATTR: Any
    STATE_ATTR: Any
    expired_attribute_loader: Any
    init_method: Any
    factory: Any
    mapper: Any
    declarative_scan: Any
    registry: Any
    @property
    def deferred_scalar_loader(self): ...
    @deferred_scalar_loader.setter
    def deferred_scalar_loader(self, obj) -> None: ...
    class_: Any
    info: Any
    new_init: Any
    local_attrs: Any
    originals: Any
    def __init__(self, class_) -> None: ...
    def __hash__(self) -> int: ...  # type: ignore[override]
    def __eq__(self, other): ...
    @property
    def is_mapped(self): ...
    # Will be overwritten when mapped
    # def mapper(self) -> None: ...
    def manage(self) -> None: ...
    @hybridmethod
    def manager_getter(self): ...
    @hybridmethod
    def state_getter(self): ...
    @hybridmethod
    def dict_getter(self): ...
    def instrument_attribute(self, key, inst, propagated: bool = ...) -> None: ...
    def subclass_managers(self, recursive) -> None: ...
    def post_configure_attribute(self, key) -> None: ...
    def uninstrument_attribute(self, key, propagated: bool = ...) -> None: ...
    def unregister(self) -> None: ...
    def install_descriptor(self, key, inst) -> None: ...
    def uninstall_descriptor(self, key) -> None: ...
    def install_member(self, key, implementation) -> None: ...
    def uninstall_member(self, key) -> None: ...
    def instrument_collection_class(self, key, collection_class): ...
    def initialize_collection(self, key, state, factory): ...
    def is_instrumented(self, key, search: bool = ...): ...
    def get_impl(self, key): ...
    @property
    def attributes(self): ...
    def new_instance(self, state: Any | None = ...): ...
    def setup_instance(self, instance, state: Any | None = ...) -> None: ...
    def teardown_instance(self, instance) -> None: ...
    def has_state(self, instance): ...
    def has_parent(self, state, key, optimistic: bool = ...): ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any

class _SerializeManager:
    class_: Any
    def __init__(self, state, d) -> None: ...
    def __call__(self, state, inst, state_dict) -> None: ...

class InstrumentationFactory:
    def create_manager_for_cls(self, class_): ...
    def unregister(self, class_) -> None: ...

instance_state: Any

instance_dict: Any
manager_of_class = base.manager_of_class

def register_class(
    class_,
    finalize: bool = ...,
    mapper: Any | None = ...,
    registry: Any | None = ...,
    declarative_scan: Any | None = ...,
    expired_attribute_loader: Any | None = ...,
    init_method: Any | None = ...,
): ...
def unregister_class(class_) -> None: ...
def is_instrumented(instance, key): ...
