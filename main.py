#!/bin/python3
import logging
from typing import List
import sys


from RustReadiness.utils.arguments import RustReadinessArguments
from RustReadiness.checks.IChecker import IChecker
from RustReadiness.utils.log_colours import LogColours

# get the checks
from RustReadiness.checks import check_list


root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

logger = logging.getLogger("RustReadiness")
logger.setLevel(logging.DEBUG)


def load_checks(args: RustReadinessArguments) -> List[IChecker]:
    loaded_checks: List[IChecker] = []
    for check in check_list:
        tmp_checker = check()
        tmp_checker.add_arguments(args.get_parser())
        loaded_checks.append(tmp_checker)
    
    return loaded_checks


def main() -> None:
    args = RustReadinessArguments()
    args.setup()
    loaded_checks = load_checks(args)
    args.load_args()
    
    passed: List[str] = []
    failed: List[str] = []
    inconclusive: List[str] = []
    # loop the checks and run em
    for check in loaded_checks:
        check_result = check.run_test(args.get_args())
        if check_result == False:
            # check failed
            failed.append(check.__class__.__name__ + ' | ' + check.get_one_line_fail())
        elif check_result == True:
            # check passed
            passed.append(check.__class__.__name__)
        else:
            # inconclusive 
            inconclusive.append(check.__class__.__name__ )

    for passed_check in passed:
        logger.info("[" + LogColours.GREEN + "PASS" + LogColours.NORMAL + '] ' + passed_check)
    for incon_check in inconclusive:
        logger.info("[" + LogColours.YELLOW + "UNKN" + LogColours.NORMAL + '] ' + incon_check)
    for failed_check in failed:
        logger.info("[" + LogColours.RED + "FAIL" + LogColours.NORMAL + '] ' + failed_check)
        
    logger.info(str(len(passed)) + "/" + str(len(loaded_checks)) + " checks passed.")

if __name__ == '__main__':
    main()