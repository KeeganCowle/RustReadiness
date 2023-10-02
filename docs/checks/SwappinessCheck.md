# Swappiness too high

swappiness controls the relative weight given to swapping out of runtime memory, as opposed to dropping memory pages from the system page cache. 

in other words. This number controlls when the system will start swapping to disk. Since disk is an order of magnitute slower than RAM, we dont want this number too low. We also dont want it too high. For our purposes the sweet spot is 10. i.e only start swapping to disk when 90% of RAM is taken.

To fix:
edit the `/etc/sysctl.conf` file as sudo and add `vm.swappiness = 10`
