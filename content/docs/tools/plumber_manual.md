+++
title = "Plumber Manual ⚔"
author = ["Hrishikesh Barman"]
draft = false
+++

<div class="book-hint warning small-text">

> -   I already have [alias](https://github.com/geekodour/dottedflies/tree/main/.config/fish/functions) and [custom cheatsheets](https://github.com/geekodour/dottedflies/tree/main/.config/cheat/personal) for commands. These notes are more about why I'd want to use certain tool and **not** how.
> -   This is for personal reference and is contexual to my knowledge
</div>

<div class="outline-1 smol-table no-tags">

## Links {#links}

-   [CPU-World: Microprocessor news, benchmarks, information and pictures](https://www.cpu-world.com)
-   [GPU Database | TechPowerUp](https://www.techpowerup.com/gpu-specs/)
-   [Sysctl Explorer](https://sysctl-explorer.net/)

</div>

<div class="outline-1 smol-table no-tags">

## No access troubleshooting {#no-access-troubleshooting}

-   `Ctrl+Alt+F{1-12}` : Get virtual terminal (tty)
-   [Magic SysRq key - Wikipedia](https://en.wikipedia.org/wiki/Magic_SysRq_key)
    -   Enable Alt+SysRq+F keyboard shortcut
-   [Reset lost root password - ArchWiki](https://wiki.archlinux.org/title/Reset_lost_root_password)

</div>

<div class="outline-1 smol-table no-tags">

## Useful tips and formatting {#useful-tips-and-formatting}

```shell
$ some command | column -t # formats the output
$ pv
$ nohup and disown
# pkill/killall/kill
```

-   worth bench-marking your file system to find out what the peak performance is
    -   [GitHub - hpc/ior: IOR and mdtest](https://github.com/hpc/ior) and there are other tools.

</div>

<div class="outline-1 smol-table no-tags">

## General system information {#general-system-information}

```shell
neofetch
lsmod
atop
w
id
last
uptime
history | awk '{print $1}' | sort | uniq -c | sort -rn | head
dmesg
progress # shows any things that might be progressing
mount | column -t
lsof
```

-   [Linux Performance](https://www.brendangregg.com/linuxperf.html)  : The OG

{{< figure src="/ox-hugo/plumber_manual-364908995.png" >}}

</div>

<div class="outline-1 smol-table no-tags">

## Processes {#processes}

```shell
fuser # fuser can tell you which process open a specific file.
lsof # print the list of files open by a process.
strace
gcore # core dumps
pgrep
```

<div class="outline-2 smol-table no-tags">

### strace {#strace}

-   will make your program slower

</div>

<div class="outline-2 smol-table no-tags">

### bpftrace {#bpftrace}

-   There are a lot of tools under this
-   See <https://github.com/iovisor/bpftrace/tree/master/tools>
-   `opensnoop.bt` : This is similar to `strace` but using eBPF.

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Process Statistics {#process-statistics}

```shell
dstat -cdngyt # how much network and disk your computer used that second
htop
ps auxf
```

<div class="outline-2 smol-table no-tags">

### Load average {#load-average}

load average: 0.00, 0.01, 0.03
The first three columns represent the average system load of the last 1, 5, and 15 minute periods.

More than you want to know about htop: <https://peteris.rocks/blog/htop/>

</div>

</div>

<div class="outline-1 smol-table no-tags">

## CPU {#cpu}

```shell
lstopo # https://unix.stackexchange.com/questions/113544/interpret-the-output-of-lstopo
lscpu
cpufetch
numastat
uname -a
hwloc-ls
numactl --hardware
```

</div>

<div class="outline-1 smol-table no-tags">

## Security {#security}

```shell
passwd
```

</div>

<div class="outline-1 smol-table no-tags">

## Interfaces &amp; Devices {#interfaces-and-devices}

```shell
lspci
xev
udev
libinput debug-events
```

</div>

<div class="outline-1 smol-table no-tags">

## Disk and Filesystems {#disk-and-filesystems}

```shell
df -hi # inodes availability
duf
lsblk
stat # inspect inode
file
filefrag
sudo tune2fs -l /dev/sda3  # for extX systems
/dev/disk/
lsblk
blkid
mount
findmnt
fdisk # gets you sector size
iotop
dumpe2fs
tune2fs
smartctl
blockdev
/proc/filesystems
iostat # from sysstat utils
cat /sys/block/sda/queue/scheduler # active scheduler in brackets
```

<div class="outline-2 smol-table no-tags">

### Formatting usb drive {#formatting-usb-drive}

fdisk, dd, parted

```shell
$ dd if=/dev/zero of=/dev/sdX status=progress
$ fdisk /dev/sdb
$ mkfs.vfat /dev/sdb1
```

<https://www.pendrivelinux.com/restoring-your-usb-key-partition/>

-   Putting a filesystem on a partition == "Making a filesystem"
-   Filesystems are what gets mounted
-   `mkfs -t <type> <partition>` eg. `mkfs -t ext4 /dev/sdb1`
-   Ordinary files can also be formatted and mounted (???)

</div>

<div class="outline-2 smol-table no-tags">

### dd {#dd}

-   dd if=/dev/random of=/var/tmp/file1.db count=100 bs=1M
-   sudo dd if=/dev/zero of=speedtest bs=1G count=50 conv=fdatasync : This should tell us how fast disk IO is happening etc.
-   `dd` was originally to be called `cc` for "character copy", but because cc was already taken by the C compiler, the next letter in the alphabet was taken.
-   **Quick Tip:** Creating a file of arbirary bytes `dd` : data dump `$ dd if=/dev/zero of`./mytempimage.img bs=1MB count=500= The above command generates a file mytempimage.img whose size is 500M
-   Really understand dd
-   <https://www.reddit.com/r/commandline/comments/hckwrq/explain_dd_command_to_me/>
-   <https://www.reddit.com/r/linuxquestions/comments/rm8fqt/help_with_understanding_how_to_use_the_dd_command/>
-   <https://unix.stackexchange.com/questions/189030/why-specify-block-size-when-copying-devices-of-a-finite-size/189091#189091>
-   <https://www.pixelbeat.org/docs/coreutils-gotchas.html>
-   <https://www.reddit.com/r/linuxquestions/comments/r7zmll/dd_for_beginners/>
-   <https://www.reddit.com/r/linux/comments/dkce3/how_and_when_to_use_the_dd_command/>
-   <https://www.reddit.com/r/linuxquestions/comments/qo90ca/how_does_dd_work/>
-   <https://www.reddit.com/r/ManjaroLinux/comments/o62s17/understanding_dd_command/>
-   <https://www.reddit.com/r/linuxmasterrace/comments/82alc1/eli5_dd_command_options/>
-   <https://www.reddit.com/r/learnprogramming/comments/2x8s2q/question_about_the_dd_unixlinuxqnx_command/>
-   <https://www.reddit.com/r/raspberry_pi/comments/xkx990/how_to_use_count_parameter_in_dd_command_properly/>
-   <https://www.reddit.com/r/linux/comments/62clm6/why_use_dd_for_writing_disk_images_to_devices/>

</div>

<div class="outline-2 smol-table no-tags">

### mounting {#mounting}

-   For disk devices, the type of FS is automatically detected by the `mount` command, so specifying a type is not necessary

<div class="outline-3 smol-table no-tags">

#### Special FS (Non disk file systems) {#special-fs--non-disk-file-systems}

-   procfs, sysfs, debugfs, NFS etc : These are also mounted by the `mount` command
-   But here we have to specify types:
    -   `mount -t <type> <device_file> <directory>`
    -   `mount -t proc proc /proc`
    -   `mount -t sysfs sysfs /sys`

</div>

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Memory {#memory}

```shell
getconf pagesize
vmstat
free
some command to kill whatever is taking up all memory and make the system operational (sort by memory consumption and kill9)
/proc/meminfo
slabtop
/proc/buddyinfo
pmap
cat /proc/<pid>/smaps
/proc/[pid]/statm
/proc/[pid]/status
```

-   Some nice tools here

</div>

<div class="outline-1 smol-table no-tags">

## Network {#network}

```shell
sudo lsof -nP -iTCP -sTCP:LISTEN
netcat # deprecated, can be used to make http request, send files over the network
socat # socat can do serial line stuff, netcat cannot.
traceroute
nmap
dig and dns
```

<div class="outline-2 smol-table no-tags">

### `ip` command {#ip-command}

-   `ip address` command output
    -   `<BROADCAST,MULTICAST,UP,LOWER_UP>` : Interface state.
        -   Broadcast &amp; Multicast capable
        -   Interface is enabled `(UP)`
        -   Physical layer is connected `(LOWER_UP)`
    -   `mtu`: Maximum transmission unit (MTU) for the interface. ([Default is 1500 bytes](https://blog.benjojo.co.uk/post/why-is-ethernet-mtu-1500))
    -   `qdisc` : The queueing approach being used by the interface.
        -   `noqueue` : Send immediately
        -   `noop` : Drop all
    -   `state` :  Another indication of the operational state of an interface.
        -   `UP` and `DOWN`
        -   `UNKNOWN` : Interface is up and operational, but nothing is connected.
    -   `group` : Interfaces can be grouped together on Linux to allow common attributes or commands. Usually `default`. Other usecase, eg. VM host system with 2 interfaces for management and 8 for data traffic. Group them into `mgmt` and `data` groups.
    -   `qlen` : Eg. 1000 – The interface has a 1000 packet queue.  The 1001st packet would be dropped.
    -   `inet:scope` : `global` means globally reachable. Others can be `link` and `host`
    -   `inet:dynamic` : DHCP was used. Leased info in `valid_lft`
-   `ip link` : shows interfaces, can make changes to interfaces
-   `ip neigh` : ARP table.
-   `ip route` : Routing table. `src` attribute is to specify source ip in multihomed setups.
    -   `ip route get` : Tells you which path will take (TODO)

</div>

<div class="outline-2 smol-table no-tags">

### `ss` command {#ss-command}

```shell
- netstat -tunapl # which processes are running on which ports
- lsof -i -P # ^ does similar things
- ss -platune
```

-   `-l` : Listen flag is not about the state but more on wherether the socket is a server(listening) or no.
-   `Netid`: nl, p_raw, u_str(Unix stream), u_seq(Unix sequence), u_dgr(Unix Datagram), icmp6, udp, tcp, v_str. See `man ss`
-   `State`: This is only useful for things using TCP(`tcp`, `u_str`, `u_seq` etc.). See `man ss` for details on the states. For anything else(udp etc.) this should be `UNCONN`.
-   `Recv-Q/Send-Q, Local Address:Port, Peer Address:Port`: See `netstat` manpage for details
-   `Process`: Sometimes this will not show up without `sudo`

</div>

<div class="outline-2 smol-table no-tags">

### socat {#socat}

-   [socat. I learned about socat a few years ago… | by Cindy Sridharan | Medium](https://copyconstruct.medium.com/socat-29453e9fc8a6)

</div>

<div class="outline-2 smol-table no-tags">

### spy tools {#spy-tools}

<div class="outline-3 smol-table no-tags">

#### ngrep {#ngrep}


</div>

<div class="outline-3 smol-table no-tags">

#### tcpdump {#tcpdump}

-   [Introduction · GitBook](https://nanxiao.github.io/tcpdump-little-book/)
-   [tcpdump is amazing (2016) | Hacker News](https://news.ycombinator.com/item?id=34623604)
-   [A tcpdump Tutorial with Examples — 50 Ways to Isolate Traffic - Daniel Miessler](https://danielmiessler.com/study/tcpdump/)
-   [Tcpdump Examples - 22 Tactical Commands | HackerTarget.com](https://hackertarget.com/tcpdump-examples/)

</div>

<div class="outline-3 smol-table no-tags">

#### wireshark {#wireshark}


</div>

</div>

<div class="outline-2 smol-table no-tags">

### dns {#dns}

```shell
sudo pkill -USR1 systemd-resolve
sudo journalctl -u systemd-resolved > ~/resolved.txt
sudo systemd-resolve --flush-caches
```

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Namespaces {#namespaces}

```bash
$ lsns
```

</div>
