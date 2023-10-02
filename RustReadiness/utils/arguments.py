import argparse
from RustReadiness.utils.exceptions import ParserNotSetupException


class RustReadinessArguments:
    def __init__(self) -> None:
        self._parser: argparse.ArgumentParser | None = None
        self._args: argparse.Namespace | None = None

    def setup(self) -> None:
        # create the parser
        self._parser = argparse.ArgumentParser(description='RustReadiness. A tool to evaluate if your server is ready for the prime time!\n\nTo run: python3 RustReadiness.py')
    
    def load_args(self) -> None:
        if not self._parser:
            raise ParserNotSetupException()

        # Parse the arguments
        self._args = self._parser.parse_args()
    
    def get_parser(self) -> argparse.ArgumentParser:
        if not self._parser:
            raise ParserNotSetupException()

        return self._parser
    
    def get_args(self) -> argparse.Namespace:
        if not self._args:
            raise ParserNotSetupException()
        
        return self._args