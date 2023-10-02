from RustReadiness.checks.cpu_gov import CPUGovCheck
from RustReadiness.checks.swapCheck import SwapCheck
from RustReadiness.checks.swappinessCheck import SwappinessCheck


check_list = [
    CPUGovCheck,
    SwapCheck,
    SwappinessCheck
]