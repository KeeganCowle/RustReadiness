# No Swap

Linux divides its physical RAM (random access memory) into chucks of memory called pages. Swapping is the process whereby a page of memory is copied to the preconfigured space on the hard disk, called swap space, to free up that page of memory. The combined sizes of the physical memory and the swap space is the amount of virtual memory available.

For rust servers this is usefull since if you are running a very large server you might not have enough memory. Swap is a good thing to have.

To create a swap file you might want to google it a bit but here is the just of it:

Note: Swap should usually be twice the size of RAM you have. So if you have 8GB ram then your swap should be 16GB. Adjust the below command accordingly
```bash
dd if=/dev/zero of=/mnt/swapfile bs=1024 count=2048k
mkswap /mnt/swapfile
echo /mnt/swapfile none swap defaults 0 0 >> /etc/fstab
chown root:root /mnt/swapfile 
chmod 0600 /mnt/swapfile
```