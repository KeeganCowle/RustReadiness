# CPU governor is not set to performance

The majority of modern processors are capable of operating in a number of different clock frequency and voltage configurations. 
The Linux kernel supports CPU performance scaling by means of the CPUFreq (CPU Frequency scaling) subsystem that consists of three layers of code: the core, scaling governors and scaling drivers.

We dont care about the core and the scaling drivers since that is largely out of our control as sever admins. The scaling governor however is in our contorl. 

Scaling governors implement algorithms to estimate the required CPU capacity. As a rule, each governor implements one, possibly parametrized, scaling algorithm.

There are a few different governors in linux:
- Performance
- Powersave
- Userspace
- Ondemand
- Conservative
- Schedutil

The one we want is `Performance` since it sets the CPU statically to the
highest frequency within the borders of scaling_min_freq and
scaling_max_freq.

To set this the easiers way is to install `cpufrequtils` and set the governor:
```bash
sudo apt-get install cpufrequtils
echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils
sudo systemctl disable ondemand
```