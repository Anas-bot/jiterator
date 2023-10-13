"""This is where the class for the context manager is."""
import subprocess
import threading
from collections.abc import Iterator
from types import TracebackType
from typing import Callable


class JitContextManager:
    """The class for the context manager."""

    def __init__(self, iterator: Iterator, function: Callable, file_path: str):
        """Initializer the context manager taking in an iterator as an argument."""
        self.iterator = iterator
        self.function = function
        self.file_path = file_path

    def __enter__(self):
        """Called as soon as the context manager is used."""
        # TODO: use subprocess.run() to use the jit compiler in pypy
        # TODO: use the correct pypy command :/
        pypy_thread = threading.Thread(target=self.run_pypy, daemon=True)
        pypy_thread.start()

    def __exit__(self, exception_type: Exception, execution_value: int, execution_traceback: TracebackType):
        """Called when the context manager's usage is done."""
        print(f"exited with type: {exception_type}, value: {execution_value}, and tb: {execution_traceback}")

    @staticmethod
    def run_pypy():
        """Runs the pypy command on the code_to_execute file with the JIT on."""
        subprocess.run("pypy --jit on code_to_execute.py")
