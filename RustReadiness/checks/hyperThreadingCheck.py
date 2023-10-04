from RustReadiness.checks.IChecker import IChecker
import argparse
import subprocess
import logging

logger = logging.getLogger("SystemdCPUAffinityCheck")

class HyperThreadingCheck(IChecker):
    def add_arguments(self, parser: argparse.ArgumentParser):
        """
        Add arguments to the parser for this check. These arguments can then be used in run_test()
        """
        return 
    
    def run_test(self, arguments: argparse.Namespace) -> bool | None:
        """
        The actual test to run. Returns a boolean. If True is returned then the check passes. If False then the check failed
        """
        command = 'cat /proc/cpuinfo | grep "siblings\\|cpu cores"'
        try:
            all_info = subprocess.check_output(command, shell=True).decode().strip()
            lines = all_info.split('\n')
            cores = 0
            siblings = 0
            for line in lines:
                if line.startswith('siblings'):
                    siblings = int(line.split(':')[1].strip())
                if line.startswith('cpu'):
                    cores = int(line.split(':')[1].strip())
                
                if cores != 0 and siblings != 0:
                    break

            if cores != siblings:
                return False
            return True
        except Exception as e:
            logger.error("Cannot check hyperthreading")
            return None
    
    def get_one_line_fail(self) -> str:
        """
        Return a 1 liner that will go next to the check name if it fails on the report
        """
        return "HyperThreading is enabled. https://github.com/SA-Flowz/RustReadiness/blob/main/docs/checks/SystemdCPUAffinityCheck.md"
    

    