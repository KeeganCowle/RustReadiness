from RustReadiness.checks.cpu_gov import CPUGovCheck
from RustReadiness.checks.swapCheck import SwapCheck
from RustReadiness.checks.swappinessCheck import SwappinessCheck
from RustReadiness.checks.systemdCPUAffinity import SystemdCPUAffinityCheck


check_list = [
    CPUGovCheck,
    SwapCheck,
    SwappinessCheck,
    SystemdCPUAffinityCheck
]