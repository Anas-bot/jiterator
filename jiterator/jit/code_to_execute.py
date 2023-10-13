"""A python file containing the code for the iterators and it's function to be executed using pypy."""
from collections.abc import Iterator
from typing import Callable


def run_loop(function_object: Callable, iterator_object: Iterator):
    """A function that iterates over the iterator while calling the passed function."""
    for _ in iterator_object:
        function_object()
