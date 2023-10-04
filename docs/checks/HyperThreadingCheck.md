# HyperThreading enabled

Hyper-threading is used to improve parallelization. For each processor core that is physically present, the operating system addresses two virtual (logical) cores and shares the workload between them when possible.

For rust servers since it uses an old version of unity and much of it runs single threaded we dont want to share the cores. We want 1 core to do 1 thing REALLY quickly. 

Disabling HyperThreading is done on the BIOS level. 