from typing import Callable
from dep._dep import _overrides, _cache

def override(**kwargs: Callable) -> None:
    """
    Override dependency functions with new implementations.

    Args:
        **kwargs: Keyword arguments mapping original function names to their overrides
    """

    # - Update override mappings

    _overrides.update(kwargs)

    # - Clear cache when overrides are set

    _cache.clear()


def test():

    # - Test override functionality

    from dep._dep import dep

    @dep()
    def get_foo(bar: str):
        yield bar

    @dep()
    def new_get_foo(bar: str):
        yield bar * 2

    # - Test original function

    with get_foo(bar="bar") as foo:
        assert foo == "bar"

    # - Apply override

    override(get_foo=new_get_foo)

    # - Test overridden function

    with get_foo(bar="bar") as foo:
        assert foo == "barbar"
