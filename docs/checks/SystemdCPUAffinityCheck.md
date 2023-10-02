# SystemD CPUAffinity not set

CPU Affinity is assigning a specific CPU core or set of CPU cores to a process. 

SystemD is the process that is responsible for running everything on a server. When you ssh to your server it will be running under systemd.

In normal day to day operation linux doesnt assign CPU affinity to anything. So any process can run on any core that is available for work. For a rust server though we dont need that flexibility. We care about 1 specific process (RustDedicated) running really well. Everything else needs to move out of the way for that process. 

Setting the CPU affinity on the systemd service limits everything on the server to running on 1 core. Then setting the CPU affinity of your rust dedicated process to the rest of your CPU cores allows the rust dedicated process to always have CPU available when its needed. 

To fix this you will need to edit `/etc/systemd/system.conf` and uncomment `#CPUAffinity=` (remove the `#` at the start of the line) and set it to 0. at the end of your changes you should have a line that looks like:

```
CPUAffinity=0
```
