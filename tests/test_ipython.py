import functools
from typing import Callable

import pytest
from IPython.core.interactiveshell import InteractiveShell

from lineapy import save


def test_empty_cell(run_cell):
    """
    Test that the trace_line method works.
    """
    assert run_cell("") is None


def test_result(run_cell):
    assert run_cell("10") == 10

    assert run_cell("a = 10") is None
    assert run_cell("a") == 10


def test_stop(run_cell):
    assert run_cell("import lineapy\nlineapy.ipython.stop()") is None
    assert run_cell("10") == 10


def test_slice(run_cell):
    assert run_cell("import lineapy") is None
    assert run_cell("a = [1, 2, 3]") is None
    assert run_cell("y = 10") is None
    assert run_cell(f"x=a[0]\na = lineapy.{save.__name__}(x, 'x')") is None

    assert run_cell("a.code") == "a = [1, 2, 3]\nx=a[0]\n"


def test_slice_artifact_inline(run_cell):
    assert run_cell("import lineapy") is None
    assert run_cell("a = [1, 2, 3]\nres = lineapy.save(a, 'a')") is None
    assert (
        run_cell("res.code")
        == """a = [1, 2, 3]
"""
    )


def test_get_value_artifact_inline(run_cell):
    assert run_cell("import lineapy") is None
    assert run_cell("a = [1, 2, 3]\nres = lineapy.save(a, 'a')") is None
    assert run_cell("res.value") == [1, 2, 3]


def test_ends_semicolon_no_print(run_cell):
    assert run_cell("10;") is None


@pytest.fixture
def ip():
    """
    Return a unique InteractiveShell instance per test.

    We call it `ip`, because that what IPython calls it in its tests.

    It provides a `run_cell` method, which returns an `ExecutionResult`.
    """
    return InteractiveShell()


@pytest.fixture
def ip_traced(ip):
    """
    An ipython fixture that first enables
    """
    assert (
        _run_cell(ip, "import lineapy.ipython\nlineapy.ipython.start()")
        is None
    )
    return ip


def _run_cell(ip: InteractiveShell, cell: str) -> object:
    """
    Runs a cell and asserts it succeeds, returning the result.
    """

    # Set store_history to True to get execution_counts added to cells
    res = ip.run_cell(cell, store_history=True)
    assert not res.error_before_exec
    assert not res.error_in_exec
    return res.result


@pytest.fixture
def run_cell(ip_traced: InteractiveShell) -> Callable[[str], object]:
    return functools.partial(_run_cell, ip_traced)
