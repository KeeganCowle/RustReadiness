from abc import abstractmethod, ABCMeta
import argparse

class IChecker(metaclass=ABCMeta):
    @abstractmethod
    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add arguments to the parser for this check. These arguments can then be used in run_test()
        """
        ...
    
    @abstractmethod
    def run_test(self, arguments: argparse.Namespace) -> bool | None:
        """
        The actual test to run. Returns a boolean. If True is returned then the check passes. If False then the check failed. None if inconclusive
        """
        ...

    @abstractmethod
    def get_one_line_fail(self) -> str:
        """
        Return a 1 liner that will go next to the check name if it fails on the report
        """
        ...
    
    