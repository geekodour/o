+++
title = "Plumber Manual ⚔"
author = ["Hrishikesh Barman"]
draft = false
+++

see [cheats](https://cheats.geekodour.org/)
![](/ox-hugo/plumber_manual-364908995.png)

<div class="outline-1 smol-table no-tags">

## General {#general}

<div class="outline-2 smol-table no-tags">

### Emergency {#emergency}

-   `Ctrl+Alt+F{1-12}` : Get virtual terminal (tty)
-   [Magic SysRq key](https://en.wikipedia.org/wiki/Magic_SysRq_key) (Alt+SysRq+F)

</div>

<div class="outline-2 smol-table no-tags">

### Formatting &amp; extra information {#formatting-and-extra-information}

-   Formatting: `column`
-   Progress: `pv`, [progress](https://sirupsen.com/progress)

</div>

<div class="outline-2 smol-table no-tags">

### System information {#system-information}

-   User-space: `w`, `id`, `last`, `uptime`, `history`, `uname`
-   Kernel: `lsmod`, `dmesg`
-   CPU: [lstopo](https://unix.stackexchange.com/questions/113544/interpret-the-output-of-lstopo), `lscpu`, `numastat`, `hwloc-ls`, `numactl`
-   Security: [audit framework](https://wiki.archlinux.org/title/Audit_framework), [rflament/loggedfs](https://github.com/rflament/loggedfs)
-   Devices: `lspci`, `libinput`, `lsblk`
-   Containers: `lsns`

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Processes {#processes}

-   Files: `fuser`, `lsof`
-   Visual: `atop`, [htop](https://peteris.rocks/blog/htop/)
-   Statistics: `dstat`
-   Debugging: `strace`, `gcore`, [bpftrace tools](https://github.com/iovisor/bpftrace/tree/master/tools)
-   Lookup/Signal: `pgrep`, `ps`, `pstree`, `pkill`, `killall`, `kill`
-   Operations: `nohup`, `disown`
    -   `nohup` : Ignores `SIGHUP` and then `exec` the mentioned command
    -   `disown` : shell utility that we can use to tell the shell not to send SIGHUP to that process.

</div>

<div class="outline-1 smol-table no-tags">

## Files, devices and filesystems {#files-devices-and-filesystems}

-   Statistics: `df`, `duf` (pretty `df`), `iotop`, `iostat`
-   File
    -   inode: `stat`, `file`
    -   content: `strings` (useful w non-text files), [stringsext](https://github.com/getreu/stringsext), `filefrag`, `dd`
-   FS: `tune2fs`, `dumpe2fs`, `/proc/filesystems`
-   Block device: `blkid`, `findmnt`, `blockdev` (good for getting various sizes), `/sys/block/sda/queue/scheduler`
-   Disk: `fdisk`, `smartctl`

</div>

<div class="outline-1 smol-table no-tags">

## Memory {#memory}

```text
/proc/meminfo
/proc/buddyinfo
/proc/[pid]/smaps
/proc/[pid]/statm
/proc/[pid]/status
```

-   Statistics: `free`, `vmstat`, `slabtop`
-   Inspection: `pmap`

</div>

<div class="outline-1 smol-table no-tags">

## Network &amp; Security {#network-and-security}

-   Debugging: `traceroute`, `tracepath`
-   Inspection: `ss/netstat` (what all is running), `ip`, `nethogs` (realtime), `tcpdump/wireshark/ngrep`, `iperf3`
-   DNS: `drill`
-   Transfer: `socat/netcat`, `rsync`
-   Reconnaissance: `nmap`
-   Links
    -   [leandromoreira/linux-network-performance-parameters](https://github.com/leandromoreira/linux-network-performance-parameters)

</div>
