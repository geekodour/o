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
-   Statistics: `dstat` (`iotop`, `nethogs` and `top` combined)
-   Debugging: `strace`, `gcore`, [bpftrace tools](https://github.com/iovisor/bpftrace/tree/master/tools)
-   Lookup/Signal: `pgrep`, `ps`, `pstree`, `pkill`, `killall`, `kill`
-   Operations: `nohup`, `disown`
    -   `nohup` : Ignores `SIGHUP` and then `exec` the mentioned command
    -   `disown` : shell utility that we can use to tell the shell not to send SIGHUP to that process.
-   Resources
    -   [All my favorite tracing tools](https://lobste.rs/s/8992zd/all_my_favorite_tracing_tools_ebpf_qemu)

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
-   Inspection: `pmap`, `vmtouch`

</div>

<div class="outline-1 smol-table no-tags">

## Network &amp; Security {#network-and-security}

-   Debugging: `traceroute`, `tracepath`, [`dropreason`](https://dxuuu.xyz/dropreason.html)
-   Inspection: `ss/netstat` (what all is running), `ip`, `nethogs` (realtime), `tcpdump/wireshark/ngrep`, `iperf3`
-   DNS: `drill`
-   Transfer: `socat/netcat`, `rsync`
-   Reconnaissance: `nmap`
-   Links
    -   [leandromoreira/linux-network-performance-parameters](https://github.com/leandromoreira/linux-network-performance-parameters)

</div>

<div class="outline-1 smol-table no-tags">

## Opinionated development practices {#opinionated-development-practices}

<div class="outline-2 smol-table no-tags">

### SQL/Databases {#sql-databases}

-   Table names
    -   Should be singular. i.e `user` instead of `users`. This also helps with foreign key names(`user_id`), junction table names (eg. `actor_film` for `actor` and `film` tables) etc.
    -   But main deal is keeping it consistent, whatever we end up picking. Singular/Plural
    -   Sometimes may conflict with the database engine keywords, so consider using `prefix`
-   Booleans columns
    -   better represented as [nullable Timestamps](https://changelog.com/posts/you-might-as-well-timestamp-it), Eg. `DELETED` column instead of bool should be timestamp of timestamp of deletion.
-   Query building
    -   Check [squirrel](https://github.com/Masterminds/squirrel) for dynamic query building when sqlc is not flexible enough
-   Migrations
    -   While dropping tables, drop the ones with fk first when writing migrations
    -   If developing in golang, if using a migration tool(eg. `goose`) and `sqlc`, `sqlc`'s `schema.sql` will have duplicate table create statement. It's fine and OK to have this duplication.
-   NULL
    -   If you have a column set to `NOT NULL`, you probably also want to set a `CHECK (column_name <> '')` to it aswell, not always but most times.
-   Primary Keys
    -   Natural keys / Surrogate keys if applicable
    -   For identifier column name, if it has to be id, i'd prefer `id` over `<table_name>_id`, just cleaner.
    -   If not using serial keys, use timestamp ordered random ids instead of plain UUID (eg. ULID/UUIDv7)
        -   For pg, use [pg_idkit](https://github.com/VADOSWARE/pg_idkit) / `pg_uuidv7`
-   Upserts
    -   TODO

</div>

<div class="outline-2 smol-table no-tags">

### Data Interchange {#data-interchange}

-   Don't think too much and just do the manual conversion of timestamp to protobuf's [format from postgres](https://stackoverflow.com/questions/77773539/deserialize-timestamp-from-postgres-into-google-protobuf-timestamp-with-sqlx) when needed.
-   If developing using golang and using `sqlc` and `protobuf`, we'd have two different generated structs of the same entity. They might look similar but they're for different purposes, we want to keep this separated. One is for database and another one is for interchange.

</div>

</div>
