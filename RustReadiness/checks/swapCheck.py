from RustReadiness.checks.IChecker import IChecker
import argparse
import subprocess
import logging

logger = logging.getLogger("SwapCheck")

class SwapCheck(IChecker):
    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add arguments to the parser for this check. These arguments can then be used in run_test()
        """
        return 
    
    def run_test(self, arguments: argparse.Namespace) -> bool | None:
        """
        The actual test to run. Returns a boolean. If True is returned then the check passes. If False then the check failed
        """
        command = "cat /proc/meminfo | grep -i SwapTotal"
        try:
            all_info = subprocess.check_output(command, shell=True).decode().strip()
            line = all_info.strip().split('SwapTotal:')[1].strip()
            if line.startswith('0'):
                return False
            return True
        except Exception as e:
            logger.error("Cannot get swap total")
            return None
    
    def get_one_line_fail(self) -> str:
        """
        Return a 1 liner that will go next to the check name if it fails on the report
        """
        return "You have no swap enabled. https://github.com/SA-Flowz/RustReadiness/blob/main/docs/checks/SwapCheck.md"
    

    