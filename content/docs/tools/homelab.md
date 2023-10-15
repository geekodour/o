+++
title = "Homelab"
author = ["Hrishikesh Barman"]
draft = false
+++

<div class="book-hint warning small-text">

> **NOTE**
>
> -   Everything about this page and my homelab and selfhosted tools are very much WIP ✨ 🚧
> -   [geekodour/workshop](https://github.com/geekodour/workshop/) : Keeping track of homelab and other workshop things.
</div>

<!--quoteend-->

<div class="book-hint info small-text">

> **TIP:**
>
> -   I did some internet comparison/study when preparing this selfhosting setup. I always take notes when studying anything, all my notes related to selfhosting [can be found here in my wiki](https://mogoz.geekodour.org/posts/20230212140130-selfhosting/).
> -   Check "tags" and "Links to this note" in the wiki page.
</div>

<div class="outline-1 smol-table no-tags">

## What's the shape? {#what-s-the-shape}

The homelab is one of my passion projects. It's not even birthed yet and there's so much to do and experiment with. If things go alright, I'll probably have my dream homelab in 1-2 years. I [want it](https://beepb00p.xyz/myinfra.html) [well](https://tajd.co.uk/2021/12/29/literate-emacs-terraform#fn:2) [documented](https://howardism.org/Technical/Emacs/literate-devops.html), well [maintained](https://wiki.kasad.com/books/kasadcom), reproducible, high quality and of-course do all the things I want it to do. Why? Vendor independence, privacy, costs, peace of mind, fun. pro: you can fix the problem, con: you have to fix the problem.

<div class="outline-2 smol-table no-tags">

### Properties {#properties}

-   Should have solid observability. This is also my playground for things.
-   Upto-date and mostly automated
-   Good and live documentation and should be easily debug-able
-   It's not like I want to selfhost everything, if there are external hosted services which satisfy my needs I would skip selfhosting. I want this to be seamless, controlled and do not want to spend hours on [debugging any](https://www.reddit.com/r/homeassistant/comments/gz1mka/moving_all_iot_devices_to_vlan_what_steps_should/ftdw3zh/) issue. Same goes for hardware.
-   I am not building enterprise network here, I can have fun so stupid stuff is sort of allowed

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Components <span class="tag"><span class="components">components</span></span> {#components}

<div class="book-hint warning small-text">

> **NOTE:**
>
> -   I have not built the homelab, this is first draft plan.
> -   These are not actual boundaries, I am just laying out an abstract layout here for me to build on.
> -   Things might be not be technically correct(I might be placing things in the wrong places of the stack as-well)
> -   I have not thought all of this properly but merely dumping ideas here. **this is NOT the topology**
</div>

| Name                              | Remark                                                               |
|-----------------------------------|----------------------------------------------------------------------|
| [Goku](#goku)                     | Bastion server, External VPS                                         |
| [Dobbies](#dobbies)               | Any service, many service, whatever random thing. These will run it. |
| [SRK](#srk)                       | Anything media management goes here, runs locallty                   |
| [Warehouse](#warehouse)           | multi purpose storage server(s)                                      |
| [Cloud ZEPEEYOU](#cloud-zepeeyou) | AI experiments helper                                                |
| [Rasta](#rasta)                   | Throwaway servers                                                    |
| [Piccolo](#piccolo)               | Trusted, Persistent Good ol webserver                                |
| [daCNC](#dacnc)                   | My phone                                                             |

<div class="outline-2 smol-table no-tags">

### Goku {#goku}

Sort of a [bastion host](https://goteleport.com/blog/ssh-bastion-host/). Idea is to have access to all my services from one place. Eg. I should be able to ssh from my phone to this machine and manage things even if I am away from my laptop. It should have the tools installed I need in a dev/sysadmin machine.

-   **Location**: VPS
-   **Threat Model**: Assume that it can be compromised and reduce attack surface accordingly.
-   **Possible stuff here**: [centralized logging](https://www.reddit.com/r/selfhosted/comments/1031chv/simple_way_to_centralize_my_server_logs/), centralized observability center, orchestrator center, [Teleport](https://goteleport.com/) w 2FA
-   **Concerns**: The usecase and motive of this component sort of contradicts. I am expecting this to be target but at the same time making this the most powerful and yet SOP in a way? Need to think.

</div>

<div class="outline-2 smol-table no-tags">

### Dobbies {#dobbies}

Local RPi(s)/Small computers/NUCs, can name them dobby-1, dobby-2 etc. Host small tools or whatever that I want to use locally or maybe expose some to the public internet as-well.

-   **Location**: Local
-   **Possible stuff here**: These will basically do anything. ArchiveWarrior stuff, bespoke scripts, see my [secondary toolchest](/docs/tools/secondary_toolchest/) for complete list of tools that are already selfhostable/can be made selfhostable to fit my needs.

</div>

<div class="outline-2 smol-table no-tags">

### SRK {#srk}

The [media server](https://www.smarthomebeginner.com/docker-media-server-2022/), [connected](https://github.com/sebgl/htpc-download-box) to a NAS most likely. . I wanted to be local first, requiring internet to reach my media does not make sense but I probably would want to have public access to this in-case.

-   **Location**: Local
-   Useful stuff
    -   [Perfect Media Server](https://perfectmediaserver.com/index.html)
    -   \*​arr services like Prowlarr, Lidarr, Sonarr Radarr, [Tdarr](https://tdarr.io/) etc
    -   [gerbera/gerbera](https://github.com/gerbera/gerbera)

</div>

<div class="outline-2 smol-table no-tags">

### Warehouse {#warehouse}

Some kind of storage server/multiple servers. I have to explore this, zfs, btrfs etc. This will store archives, media files etc. **This is not the backup**, it'll be done separately.

-   Useful stuff: [filebrowser/filebrowser](https://github.com/filebrowser/filebrowser), [mickael-kerjean/filestash](https://github.com/mickael-kerjean/filestash),
-   Readings
    -   [Building NAS with ZFS, AFP/Samba for Time Machine | by Cory Chu | GWLab](https://blog.gwlab.page/building-nas-with-zfs-afp-for-time-machine-d8d67add1980)
    -   [When would I want to use raidz3 vs raidz2?](https://www.reddit.com/r/DataHoarder/comments/b4759f/when_would_i_want_to_use_raidz3_vs_raidz2/)
    -   [simon987/awesome-datahoarding](https://github.com/simon987/awesome-datahoarding)

</div>

<div class="outline-2 smol-table no-tags">

### Cloud ZEPEEYOU {#cloud-zepeeyou}

To carry out AI experiments. Not worrying about this much rn as this will be specific to usecase but definitely want this to be billed on usage lol.

</div>

<div class="outline-2 smol-table no-tags">

### Rasta {#rasta}

-   Location: VPS, needs to be ephemeral

A test server / dummy that i can trash and recreate anytime, installs my necessary tools automatically on creation etc.

</div>

<div class="outline-2 smol-table no-tags">

### Piccolo {#piccolo}

Trusted, Persistent Good ol webserver. This will have a solid reverse proxy in place so that I spin up random APIs/Websites for public quickly.

</div>

<div class="outline-2 smol-table no-tags">

### daCNC {#dacnc}

This is my phone. This is more like a remote control for things and I've set some phone specific tasker profiles which are super useful. Eg. Taking picture and Uploading it to my Google Drive via SMS trigger etc.

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Orchestration {#orchestration}

We have few options.

| Name       | Remark                                                                                                                                                                                                                                                                                                                            |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nomad      | Based [on](https://www.reddit.com/r/homelab/comments/h7gvn0/nomad_development_sandbox/) [what](https://github.com/aldoborrero/hashi-homelab) I [read](https://mrkaran.dev/posts/home-server-nomad/) it [seems](https://www.carrot.blog/posts/2023/01/self-hosting-mastodon-aws-nomad/) like this would be suitable for my homelab |
| Kubernetes | There are things [like k3s](https://github.com/thaum-xyz/ankhmorpork)                                                                                                                                                                                                                                                             |
| Promox     | Runs LXC and VMs, Min 3 nodes needed                                                                                                                                                                                                                                                                                              |

What keeps everything together? I have not decided yet but guess it'll be a mix of terraform and [ansible](https://0xc45.com/blog/ansible-defined-homelab/).

I think I'll go with Nomad like I mentioned.

</div>

<div class="outline-1 smol-table no-tags">

## Networking {#networking}

Goals

-   I should be able to access(ssh) certain private devices/services securely from the public internet.
-   I should be able to access certain public services securely from the public internet. (eg. fileserver, mediaserver etc)
-   Local devices should be able to talk to each other, preferably put local devices into a different VLAN and internet facing stuff into a DMZ.
-   Should have a proper way to access geoblocked content
-   Security, have not thought about my threat model properly.

Anti-Goals

-   Not trying to be anonymous here
-   Even though I want to build a mesh network, in this iteration it's not the goal. At most I might be use tailscale or something similar.

<div class="outline-2 smol-table no-tags">

### VPN {#vpn}

-   **Mesh VPN setup**
    -   Goal: Allow my devices to talk to each other
    -   Something like Tailscale is looking juicy here
-   **Road warrior setup (VPN VPS)**
    -   Goal: Something that allows me to access my devices at home when I am out.
-   **Encrypted Traffic + Hide source IP(geo) setup**
    -   Goal: Not anonymity but more of privacy and bypassing censorship. Eg. When using insecure public wifi or anything else that fits.
    -   I can selfhost this but with that I cannot keep switching countries etc. So might be good idea to go with something like [Mullvad VPN](https://mullvad.net/en/)
-   **Tunnels**
    -   Goal: Expose public only services quickly, give temporary access to something that I am running locally etc.

</div>

<div class="outline-2 smol-table no-tags">

### Proxy {#proxy}

<div class="outline-3 smol-table no-tags">

#### Forward Proxy {#forward-proxy}

I do not really feel the need of a forward proxy as such at the moment. But I can see one usecase: Censorship bypass. Setting up shadowsocks, vray and cloak along w tor proxy(whatever combination makes sense for the usecase) might be a good idea. Because you don't need them until you need them :)

</div>

<div class="outline-3 smol-table no-tags">

#### Reverse Proxy {#reverse-proxy}

I can use these things to do load-balancing/ssl termination/reverse proxy/protocol demultiplexing/[HA](https://www.reddit.com/r/selfhosted/comments/ytg5kf/high_availability_for_beginners/)/failover/caching/rate-limiting etc. Here's [a more](https://github.com/GrrrDog/weird_proxies) [complete list](https://www.authelia.com/overview/prologue/supported-proxies/). After some comparison, I think i'll be going with either Traefik or Caddy.

</div>

</div>

<div class="outline-2 smol-table no-tags">

### Router {#router}

-   We have the options of OpenWRT and OPNSense here. We can mix and match, will think of exact topology later.
-   Point web services logs to fail2ban and let it handle rate-limiting etc.
-   For extra points can check Crowdsec

</div>

<div class="outline-2 smol-table no-tags">

### DNS {#dns}

This is one bad boi. I probably just want to run local resolver. Maybe an authoritative server replicated to secondaries later. But for now, I plan PiHole/Blocky+Unbound.

-   Once we have a reverse-proxy setup, you can have your local DNS server point to your reverse proxy for whatever domain. eg. `*.home`. Also see [what domain name to use for your home network? home.arpa](https://www.ctrl.blog/entry/homenet-domain-name.html)
-   Some people recommend doing split-horizon DNS along with reverse-proxy if running multiple services, I don't see a point rn but maybe I'll later.

</div>

<div class="outline-2 smol-table no-tags">

### Local Network {#local-network}

<div class="outline-3 smol-table no-tags">

#### VLANs and Subnets {#vlans-and-subnets}

-   **Reason:** It's nice to separate things with vlans and firewall rules + IoT devices are known to be [insecure](https://www.reddit.com/r/hacking/comments/rt7k6y/how_does_an_entire_network_get_compromised_after/). (Sort of an overkill but who cares)
-   Subnets
    -   VLAN 1 for home devices LAN
    -   VLAN 2 for trusted IoT which cannot run VPN client, access to the Internet allowed
    -   VLAN 3 for isolated (untrusted) IoT devices
    -   VLAN 4 for DMZ for publicly hosted services etc
-   VPN runs on VLAN1
-   What comes and goes out of these VLANS to be configured via firewalls
-   [ ] Check if we'll need a managed switch or OpenWRT [will cut it](https://www.reddit.com/r/openwrt/comments/vaqhph/vlans_without_a_builtin_switch/)

</div>

<div class="outline-3 smol-table no-tags">

#### DMZ {#dmz}

-   Reason: Because I plan to host public facing services it makes sense to have a DMZ.
-   Objective is to provide firewall capabilities between hosts in the DMZ and hosts on the internal network.

</div>

</div>

<div class="outline-2 smol-table no-tags">

### Monitoring the network {#monitoring-the-network}

I haven't explored this properly, so just link dumping.

-   [zaneclaes/network-traffic-metrics](https://github.com/zaneclaes/network-traffic-metrics)
-   [maxandersen/internet-monitoring](https://github.com/maxandersen/internet-monitoring)
-   [internet-pi](https://github.com/geerlingguy/internet-pi)
-   [Monitoring my home network](https://mrkaran.dev/posts/isp-monitoring/)
-   [Taking Back What Is Already Yours: Router Wars Episode I](https://psaux.io/2020/03/01/Taking-Back-What-Is-Already-Yours-Router-Wars-Episode-I/)
-   [Self-hosted home network traffic monitoring with ntopng](https://davquar.it/post/self-hosting/ntopng-fritzbox-monitoring/)
-   [Observing my cellphone switch towers](https://fabiensanglard.net/lte/index.html)

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Backup Plan {#backup-plan}

<div class="book-hint danger small-text">

> **NOTE** ⚠
>
> -   I have not started backing up anything at the moment, there are just scattered copies etc.
> -   This will be an incremental process, but will start soon. (18th Feb'23)
> -   In some cases I **need to do some prior work**, eg. my video files are scrattered all over the internet and different drives. I have to put them together into one place before I even think of backing them up.
</div>

After some reading and going through [various backup](https://github.com/restic/others) solutions, I decided that the primary tool to make my backups will be [restic](https://restic.net/). I initially [considered](https://www.reddit.com/r/BorgBackup/comments/v3bwfg/why_should_i_switch_from_restic_to_borg/) [borg with rysnc.net](https://www.rsync.net/products/borg.html), but using restic lets me use [cheaper storage](https://www.backblaze.com/b2/cloud-storage.html) alternatives and at the time of this writing I am trying to cut costs. I haven't really looked into [tarsnap](https://www.tarsnap.com/design.html) but I wanted to.

-   The main strategy I am going to follow is the [3-2-1 strategy](https://github.com/geerlingguy/my-backup-plan). (3 copies, 2 different media, 1 offsite) + **restore tested**.
-   I am not backing up emails, DMs etc as I consider them ephemeral and I try to set disappear timer in most of them.

<div class="outline-2 smol-table no-tags">

### Data inventory {#data-inventory}

| Name                                 | What about it?                                                                                                                                                                                                                               | Priority | Backed Up? |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------|
| Passwords &amp; 2FA passphrases      | Strengthen master pass. Create regular encrypted export from bitwarden. Backup local `pass` store.                                                                                                                                           | 5/5      | 👎         |
| 2FA                                  | Google Authenticator, no backups nothing, do something.                                                                                                                                                                                      | 5/5      | 👎         |
| PC                                   | Nothing worth backing up here                                                                                                                                                                                                                | 0/5      | 👎         |
| Laptop                               | Installed package list and configurations(dot files). Browser profile+ext. configurations                                                                                                                                                    | 5/5      | 👎         |
| Phone                                | Tasker configuration. App list + configuration                                                                                                                                                                                               | 2/5      | 👎         |
| Access &amp; Encryption Keys         | Put SSH and Age private keys somewhere safe, make way for automatic backup of rotated keys                                                                                                                                                   | 5/5      | 👎         |
| Homelab configuration                | I don't have the homelab ready now so would not know                                                                                                                                                                                         | 0/5      | 👎         |
| Public and Private repositories      | Github+Bitbucket mirrors. Offsite(forked+own+custom repo) backup.                                                                                                                                                                            | 1/5      | 👎         |
| eBooks                               | I have a book collection on google drive. Setup automated organization. Then backup.                                                                                                                                                         | 4/5      | 👎         |
| Internet Documents                   | Research papers and other random PDFs. Put them in appropriate place first. Backup.                                                                                                                                                          | 1/5      | 👎         |
| Internet memes&amp;photos&amp;videos | Make a [media browser/search engine](https://findthatmeme.com/blog/2023/01/08/image-stacks-and-iphone-racks-building-an-internet-scale-meme-search-engine-Qzrz7V6T.html) first for this. Backup everything as application backup afterwards. | 0.2/5    | 👎         |
| Personal Photos                      | Photos from Google drive/photos                                                                                                                                                                                                              | 2/5      | 👎         |
| Personal Screenshots                 | Screenshots from Google drive                                                                                                                                                                                                                | 1/5      | 👎         |
| Personal Documents                   | Google drive, Physical copies. Put them in appropriate place first. Backup.                                                                                                                                                                  | 3/5      | 👎         |
| Personal Social Media Dumps          | First organize. Then backup.                                                                                                                                                                                                                 | 1/5      | 👎         |

</div>

<div class="outline-2 smol-table no-tags">

### Backup details {#backup-details}

<div class="book-hint warning small-text">

> This section will be incrementally populated with details about how I am doing the backups etc. I'll probably do it in literate programming fashion.
</div>

-   Threat model of data loss and disaster recovery is no longer hardware failure: it’s account lock out. So make sure to use replicate stuff to different media/providers.

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Resources &amp; Links {#resources-and-links}

-   [Home | LinuxServer.io](https://www.linuxserver.io/) : Community Images
-   [ligurio/awesome-ci: List of Continuous Integration services](https://github.com/ligurio/awesome-ci)

<div class="outline-2 smol-table no-tags">

### Compute providers {#compute-providers}

| Name                                                                      | Remark                                                                                                                              |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [Vultr](https://www.vultr.com/)                                           | Heard good things                                                                                                                   |
| [Exoscale](https://www.exoscale.com/)                                     | One person said good thing about this                                                                                               |
| [Hetzner](https://www.hetzner.com/)                                       | Good value for VPS, support, transparent, peering issues (Now as ARM64! cheap :))                                                   |
| [Time4VPS](https://www.time4vps.com/)                                     | Idk, probably good and cheap                                                                                                        |
| [Uberspace](https://uberspace.de/en/product/#prices)                      | Unique "shared server" concept. In theory you can use as much ressources as you want but in that case other customers are impacted. |
| [Scaleway](https://www.scaleway.com/en/)                                  | Complaints about support                                                                                                            |
| [Oracle](https://www.oracle.com/cloud/free/#always-free)                  | It's a free tire but lot of complaints about dark patterns. Use it w caution.                                                       |
| [Tornado VPS](https://tornadovps.com/)                                    | Idk, probably good and cheap                                                                                                        |
| [Linode](https://www.linode.com/)                                         | Little pricy but trusy                                                                                                              |
| [DigitalOcean](https://www.digitalocean.com/)                             | Little pricy but trusy(2)                                                                                                           |
| [RackNerd](https://my.racknerd.com/index.php?rp=/store/black-friday-2022) | Black friday yearly deal is juicy                                                                                                   |
| [netcup](https://www.netcup.eu/)                                          | Old fellow, probably good                                                                                                           |
| [SSD Nodes](https://www.ssdnodes.com/)                                    | Cheap stuff but good                                                                                                                |
| [OVH](https://www.ovhcloud.com/en-ie/)                                    | French company, once data center caught fire but otherwise reviews are mixed. Interesting bare metal offerings                      |

<div class="outline-3 smol-table no-tags">

#### Other server resources {#other-server-resources}

-   [How much can you really get out of a 4$ VPS?](https://alicegg.tech//2023/02/06/4dollar-vps.html)
-   [Cloud server CPU performance comparison](https://jan.rychter.com/enblog/cloud-server-cpu-performance-comparison-2019-12-12)
-   [Free clouds | Paul's page](https://paul.totterman.name/posts/free-clouds/)
-   [Cloud Costs Every Programmer Should Know | Lobsters](https://lobste.rs/s/m4uejv/cloud_costs_every_programmer_should_know)
-   Markets: [Server Hunter](https://www.serverhunter.com) | [BuyVM](https://buyvm.net/) | [LowEndBox](https://lowendbox.com/)
-   AWS: [EC2Throughput](https://www.ec2throughput.info/) | [Amazon EC2 Instance Comparison](https://instances.vantage.sh/) | [ec2.shop](https://ec2.shop/) | [AWS networking concepts](https://miparnisariblog.wordpress.com/2023/03/29/aws-networking-concepts/)

</div>

</div>

<div class="outline-2 smol-table no-tags">

### Storage providers {#storage-providers}

| Name                  | Remark                                  |
|-----------------------|-----------------------------------------|
| Hetzner storage boxes | have not checked but good things heard  |
| Blackblaze B2         | moi wants 2 use this for offsite backup |

<div class="outline-3 smol-table no-tags">

#### Storage resources {#storage-resources}

-   [Storage Calculator](https://www.reddit.com/r/DataHoarder/comments/ocaglt/interactive_graphing_calculator_for_cloud_storage/)
-   [CostStorage.com](http://coststorage.com/)
-   [Object Storage Price Comparison - qBackup](https://www.qualeed.com/en/qbackup/cloud-storage-comparison/)
-   [Disk Prices (US)](https://diskprices.com/)

</div>

</div>

<div class="outline-2 smol-table no-tags">

### Best practices {#best-practices}

<div class="outline-3 smol-table no-tags">

#### Hardening system {#hardening-system}

-   Reverse proxy only accepting domain-name queries instead of the IP.

</div>

<div class="outline-3 smol-table no-tags">

#### Environment {#environment}

-   [Best practices for segmentation of the corporate network of any company](https://github.com/sergiomarotco/Network-segmentation-cheat-sheet)
-   [doitintl/secure-gcp-reference](https://github.com/doitintl/secure-gcp-reference)

</div>

<div class="outline-3 smol-table no-tags">

#### Observability {#observability}

-   [samber/awesome-prometheus-alerts](https://github.com/samber/awesome-prometheus-alerts): Collection of Prometheus alerting rules
-   [monitoringsucks/metrics-catalog](https://github.com/monitoringsucks/metrics-catalog): Catalog of valuable metrics you might want to collect
-   [Enapiuz/awesome-monitoring](https://github.com/Enapiuz/awesome-monitoring): List of tools for monitoring and analyze everything.
-   [AnalogJ/scrutiny](https://github.com/AnalogJ/scrutiny)

</div>

<div class="outline-3 smol-table no-tags">

#### Security {#security}

-   [Who’s Attacking My Server?](https://bastian.rieck.me/blog/posts/2022/server/)

</div>

</div>

<div class="outline-2 smol-table no-tags">

### Other Homelabs {#other-homelabs}

-   [How I re-over-engineered my home network for privacy and security | Ben Balter](https://ben.balter.com/2021/09/01/how-i-re-over-engineered-my-home-network/)
-   [Local First Home Spaces - HackMD](https://hackmd.io/@XR/local-first-homes)
-   [Personal Data Warehouses: Reclaiming Your Data](https://simonwillison.net/2020/Nov/14/personal-data-warehouses/)
-   [The Honeypot Diaries: Thousands of Daily Attacks on My Home Network | Hacker News](https://news.ycombinator.com/item?id=37799438)
-   [FOSDEM 2023 - Self-Hosting (Almost) All The Way Down](https://archive.fosdem.org/2023/schedule/event/rv_selfhosting_all_the_way_down/)
-   [Moving Marginalia to a new server | Hacker News](https://news.ycombinator.com/item?id=37800753)
-   [My Overkill Home Network - Complete Details 2023](https://blog.networkprofile.org/my-home-network-complete-details-2023/)
-   [gokrazy is really cool - Xe Iaso](https://xeiaso.net/blog/gokrazy)
-   [Synthing Anywhere With Tailscale | init(8)](https://archive.is/20220821082158/https://init8.lol/synthing-anywhere-with-tailscale/)
-   [Notes on using a single-person Mastodon server | Lobsters](https://lobste.rs/s/ggdnee/notes_on_using_single_person_mastodon)
-   [I found the Holy Grail of backups - Stavros' Stuff](https://www.stavros.io/posts/holy-grail-backups/)
-   [How I store my files and why you should not rely on fancy tools for backup](https://www.unixsheikh.com/articles/how-i-store-my-files-and-why-you-should-not-rely-on-fancy-tools-for-backup.html)
-   [This blog is now running on solar power](https://louwrentius.com/this-blog-is-now-running-on-solar-power.html) and [LOW←TECH MAGAZINE](https://solar.lowtechmagazine.com/)
-   [This blog is hosted on my Android phone | Hacker News](https://news.ycombinator.com/item?id=35944315)
-   [Off-the-Grid Raspbian Repositories](https://blog.thelifeofkenneth.com/2018/01/off-grid-raspbian-repositories.html)
-   [My Homelab Build - Xe Iaso](https://xeiaso.net/blog/my-homelab-2021-06-08)
-   [Self hosting in 2023 - Grifel](https://grifel.dev/decentralization/)
-   [Make your own VPN with Fly.io, tailscale and GitHub | Hacker News](https://news.ycombinator.com/item?id=36064305)
-   [Linux Networking Shallow Dive: WireGuard, Routing, TCP](https://news.ycombinator.com/item?id=36040803)
-   [Ask HN: How would you build a budget CPU compute cluster in 2023? | Hacker News](https://news.ycombinator.com/item?id=35260049)
-   [Home Lab Beginners guide - Hardware](https://haydenjames.io/home-lab-beginners-guide-hardware/)
-   [Building a better home network | Kevin Burke](https://kevin.burke.dev/kevin/building-a-better-home-network/)
-   [My network home setup - v4.0 | etcetera](https://giuliomagnifico.blog/networking/2023/01/05/home-network_v4.html)
-   [Setting up a Raspberry Pi with 2 Network Interfaces as a very simple router](https://www.jeffgeerling.com/blog/2021/setting-raspberry-pi-2-network-interfaces-very-simple-router)
-   [khuedoan/homelab](https://github.com/khuedoan/homelab)
-   <https://twitter.com/workspacesxyz>
-   /r/homelab /r/selfhosted
-   [Node-RED](https://nodered.org/)

</div>

<div class="outline-2 smol-table no-tags">

### Aesthetics {#aesthetics}

-   [corkami/pics](https://github.com/corkami/pics) : Posters, drawings.
-   [The Unix Magic Poster | Hacker News](https://news.ycombinator.com/item?id=27029196)
-   [Investing in lighting did great things for my mental and physical health](https://www.bramadams.dev/projects/invest-in-lights)

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Hardware {#hardware}

<div class="outline-2 smol-table no-tags">

### Products {#products}

-   [ZimaBoard - World's First Hackable Single Board Server](https://www.zimaboard.com/)
-   [Synology Inc.](https://www.synology.com/en-global)
-   [FRITZ!Box | AVM International](https://en.avm.de/products/fritzbox/)
-   [CardSystem | learn effective with flash cards](https://www.cardsystem.net/)
-   [Dream Machine Pro – Ubiquiti Inc.](https://store.ui.com/products/udm-pro)
-   [HP USB-C G5 Essential Dock](https://www.hp.com/us-en/shop/pdp/hp-usb-c-g5-essential-dock)
-   [Nitrokey | Secure your digital life](https://www.nitrokey.com/)
-   [MINISFORUM DeskMini UM350 Mini PC ](https://www.amazon.com/UM250-Windows-Computer-Output-Graphics/dp/B08QZC6H8Q)
-   [The Modern, Open-Source KVM over IP | TinyPilot](https://tinypilotkvm.com/)
-   [Garmin inReach Explorer+, Handheld Satellite Communicator](https://www.amazon.com/Garmin-Explorer-Satellite-Communicator-Navigation/dp/B01MY03CZP)
-   [USB Numeric Keypad Portable Slim Mini Number Pad](https://www.amazon.in/SPIN-CART-Numeric-Portable-Computer/dp/B07FTBKJ6T)
-   [Cat S62 Pro Smartphone | Cat phones USA](https://www.catphones.com/en-us/cat-s62-pro-smartphone/)
-   [DeviceFarmer/stf: Control and manage Android devices from your browser.](https://github.com/DeviceFarmer/stf)
-   [Tamagotchi - Wikipedia](https://en.wikipedia.org/wiki/Tamagotchi)
-   [Custom made portable PC](https://www.reddit.com/r/homelab/comments/xm76nm/moved_my_allinone_pentest_lab_from_a_2u_case_to_a/)

</div>

<div class="outline-2 smol-table no-tags">

### Guides {#guides}

-   [Aluminum T-slot Building Systems – Build your Idea | Hacker News](https://news.ycombinator.com/item?id=34567318)
-   [GitHub - help-14/mechanical-keyboard: DIY mechanical keyboard and where to find them](https://github.com/help-14/mechanical-keyboard)
-   [E-ink is so Retropunk](https://rmkit.dev/eink-is-so-retropunk/)
-   [Old Vintage Computing Research: The Fossil Wrist PDA becomes a tiny Gopher client (with Overbite Palm 0.3)](https://oldvcr.blogspot.com/2023/09/the-fossil-wrist-pda-becomes-tiny.html)
-   [Privacy friendly ESP32 smart doorbell with Home Assistant local integration | Hacker News](https://news.ycombinator.com/item?id=37131957)
-   [GitHub - haimgel/display-switch: Turn a $30 USB switch into a kvm sw](https://github.com/haimgel/display-switch)
-   [GitHub - seemoo-lab/openhaystack: Build your own 'AirTags'](https://github.com/seemoo-lab/openhaystack)
-   [Help us improve the flight coverage in your area](https://planefinder.net/coverage)
-   [Comparing Hobby PCB Vendors | Hacker News](https://news.ycombinator.com/item?id=35285769)
-   [ESP32 Buyer’s Guide: Different Chips, Firmware, Sensors](https://eitherway.io/posts/esp32-buyers-guide/)
-   [Unpopular Opinion: Don’t Use a Raspberry Pi for That | Hacker News](https://news.ycombinator.com/item?id=35260322)
-   [JanOS: Turn your phone into an IoT board (2015) | Hacker News](https://news.ycombinator.com/item?id=35748052)
-   [Junk drawer phone as a music streaming server | Hacker News](https://news.ycombinator.com/item?id=35747379)
-   [Your First LTE | Hacker News](https://news.ycombinator.com/item?id=35709114)
-   [Making a Linux home server sleep on idle and wake on demand](https://news.ycombinator.com/item?id=35627107)
-   [A Beginner's Guide to Houseplants](https://www.notion.so/A-Beginner-s-Guide-to-Houseplants-f90190a8c15b4bb8b65c60f16e3f9502)
-   [Notes on RSI for Developers](https://www.swyx.io/rsi-tips)

</div>

</div>

<div class="outline-1 smol-table no-tags">

## Issues {#issues}

<div class="outline-2 smol-table no-tags">

### USB ova IP {#usb-ova-ip}

-   There's good support for linux but next to none for an easy installation for windows.
-   <https://usbip.sourceforge.net/>
-   <https://github.com/usbip/implementations>
-   <https://github.com/usbip/protocol>
-   <https://github.com/klabarge/fob>

</div>

<div class="outline-2 smol-table no-tags">

### Wayland x Windows KVM {#wayland-x-windows-kvm}

-   input-leap works but unfortunately/fortunately i am using wlroots and win11.
-   <https://github.com/htrefil/rkvm>
-   <https://github.com/r-c-f/waynergy> (client, does not seem to work w barrier server on win)

</div>

</div>
