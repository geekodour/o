+++
title = "Homelab"
author = ["Hrishikesh Barman"]
draft = false
+++

<div class="book-hint warning small-text">

> **NOTE** Everything about this page and my homelab and selfhosted tools are very much WIP ✨ 🚧 Currently contains both learning resources and specs. of homelab but will separate them in future.
</div>

<div class="outline-1 smol-table">

## What's the shape? {#what-s-the-shape}

The homelab is one of my passion projects. It's not even birthed yet and there's so much to do and experiment with. If things go alright, I'll probably have my dream homelab in 1-2 years. I [want it](https://beepb00p.xyz/myinfra.html) [well](https://tajd.co.uk/2021/12/29/literate-emacs-terraform#fn:2) [documented](https://howardism.org/Technical/Emacs/literate-devops.html), well maintained, reproducible, high quality and of-course do all the things I want it to do. Why? Vendor independence, privacy, costs, peace of mind, fun. pro: you can fix the problem, con: you have to fix the problem.

<div class="outline-2 smol-table">

### Properties {#properties}

-   Should have solid observability. This is also my playground for things.
-   Upto-date and mostly automated
-   Good and live documentation and should be easily debug-able
-   It's not like I want to selfhost everything, if there are external hosted services which satisfy my needs I would skip selfhosting. I want this to be seamless, controlled and do not want to spend hours on [debugging any](https://www.reddit.com/r/homeassistant/comments/gz1mka/moving_all_iot_devices_to_vlan_what_steps_should/ftdw3zh/) issue. Same goes for hardware.
-   I am not building enterprise network here, I can have fun so stupid stuff is sort of allowed

</div>

</div>

<div class="outline-1 smol-table">

## Components {#components}

<div class="book-hint warning small-text">

> **NOTE:** These are not actual boundaries, I am just laying out an abstract layout here for me to build on. Things might be not be technically correct(I might be placing things in the wrong places of the stack as-well) as I have not thought all of this though but merely dumping ideas here. **this is NOT the topology**
</div>

<div class="outline-2 smol-table">

### Goku {#goku}

Sort of a [bastion host](https://goteleport.com/blog/ssh-bastion-host/). Idea is to have access to all my services from one place. Eg. I should be able to ssh from my phone to this machine and manage things even if I am away from my laptop. It should have the tools installed I need in a dev/sysadmin machine.

-   **Location**: VPS
-   **Threat Model**: Go with the assumption that it can be compromised and reduce attack surface accordingly.
-   **Possible stuff here**: [centralized logging](https://www.reddit.com/r/selfhosted/comments/1031chv/simple_way_to_centralize_my_server_logs/), centralized observability center, orchestrator center, [Teleport](https://goteleport.com/) w 2FA
-   **Concerns**: The usecase and motive of this component sort of contradicts. I am expecting this to be target but at the same time making this the most powerful and yet SOP in a way? Need to think.

</div>

<div class="outline-2 smol-table">

### Dobbies {#dobbies}

Local RPi(s)/Small computers/NUCs, can name them dobby-1, dobby-2 etc. Host small tools or whatever that I want to use locally or maybe expose some to the public internet as-well.

-   **Location**: Local
-   **Possible stuff here**: [AboutRSS/ALL-about-RSS](https://github.com/AboutRSS/ALL-about-RSS), ArchiveWarrior stuff, baserow(does not have kanban!) guacamole, kasm, bespoke scripts, a lot more.

</div>

<div class="outline-2 smol-table">

### SRK {#srk}

The media server, connected to a NAS most likely. . I wanted to be local first, requiring internet to reach my media does not make sense but I probably would want to have public access to this in-case.

-   **Location**: Local
-   **Possible stuff here**: [Perfect Media Server](https://perfectmediaserver.com/index.html), \*​arr services like Prowlarr, Lidarr, Sonarr Radarr, [Tdarr](https://tdarr.io/) etc

</div>

<div class="outline-2 smol-table">

### Warehouse {#warehouse}

Some kind of storage server. I have to explore this, zfs etc. This will store archives, media files etc. **This is not the backup**, it'll be done separately.

-   [Building NAS with ZFS, AFP/Samba for Time Machine | by Cory Chu | GWLab](https://blog.gwlab.page/building-nas-with-zfs-afp-for-time-machine-d8d67add1980)
-   [When would I want to use raidz3 vs raidz2?](https://www.reddit.com/r/DataHoarder/comments/b4759f/when_would_i_want_to_use_raidz3_vs_raidz2/)

</div>

<div class="outline-2 smol-table">

### Cloud ZEPEEYOU {#cloud-zepeeyou}

To carry out AI experiments. Not worrying about this much rn as this will be specific to usecase but definitely want this to be billed on usage lol.

</div>

<div class="outline-2 smol-table">

### Rasta {#rasta}

-   Location: VPS, needs to be ephemeral

A test server / dummy that i can trash and recreate anytime, installs my necessary tools automatically on creation etc.

</div>

</div>

<div class="outline-1 smol-table">

## Orchestration {#orchestration}

| Name       | Remark                                                                                                                                                                                                                                                                                                                            |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nomad      | Based [on](https://www.reddit.com/r/homelab/comments/h7gvn0/nomad_development_sandbox/) [what](https://github.com/aldoborrero/hashi-homelab) I [read](https://mrkaran.dev/posts/home-server-nomad/) it [seems](https://www.carrot.blog/posts/2023/01/self-hosting-mastodon-aws-nomad/) like this would be suitable for my homelab |
| Kubernetes | There are things [like k3s](https://github.com/thaum-xyz/ankhmorpork)                                                                                                                                                                                                                                                             |
| Promox     | Runs LXC and VMs, Min 3 nodes needed                                                                                                                                                                                                                                                                                              |

What keeps everything together? I have not decided yet but guess it'll be a mix of terraform and [ansible](https://0xc45.com/blog/ansible-defined-homelab/).

</div>

<div class="outline-1 smol-table">

## Networking {#networking}

Goals

-   I should be able to access(ssh) certain private devices/services securely from the public internet.
-   I should be able to access certain public services securely from the public internet. (eg. fileserver, mediaserver etc)
-   Local devices should be able to talk to each other, preferably put local devices into a different VLAN and internet facing stuff into a DMZ.
-   Should have a proper way to access geoblocked content
-   Security, have not thought about my threat model properly.

Anti-Goals

-   Not trying to be anonymous here

<div class="outline-2 smol-table">

### VPN {#vpn}

<div class="outline-3 smol-table">

#### What I need {#what-i-need}

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

</div>

<div class="outline-2 smol-table">

### Forward Proxy {#forward-proxy}

<div class="book-hint warning small-text">

> There can be `n` reasons why you'd want a forward proxy, but I am listing these thinking about censorship. You can mix these network proxies with your VPN or TOR network as you see fit. You could also host them in different servers. I do not understand these properly and there are edge cases around UDP support etc. I have to experiment to see what exactly I can get out of these.
</div>

-   [Outline](https://getoutline.org/how-it-works/)
    -   Designed specifically to circumvent certain firewalls and bypass censorship. **Never designed to be anonymous or private**.
    -   This is built on top of [Shadowsocks](https://en.wikipedia.org/wiki/Shadowsocks) but claims to be more resistant to blocking and detection.
    -   Shadowsocks in turn is built on top of [SOCKS5](https://datatracker.ietf.org/doc/html/rfc1928) which sort of adds an encryption layer. You can just [use SSH](https://ma.ttias.be/socks-proxy-linux-ssh-bypass-content-filters/) [to do](https://github.com/sshuttle/sshuttle) [the same](http://www.dest-unreach.org/socat/doc/socat-tun.html) though.
-   v2ray and cloak: These are other popular solutions in the bypass censorship space. Good [overview here](https://github.com/net4people/bbs/issues/36).
-   So called "SmartDNS" solutions. I am not exactly sure how these work. These bundle DNS and a proxy together in the same service. Examples: Unlocator, NordVPN etc. also see [Seji64/SniDust](https://github.com/Seji64/SniDust). I don't really want to use this at all but just putting this here as an option.

</div>

<div class="outline-2 smol-table">

### Reverse Proxy {#reverse-proxy}

I can use these things to do load-balancing/ssl termination/reverse proxy/protocol demultiplexing/[HA](https://www.reddit.com/r/selfhosted/comments/ytg5kf/high_availability_for_beginners/)/failover/caching/rate-limiting etc. Here's [a more](https://github.com/GrrrDog/weird_proxies) [complete list](https://www.authelia.com/overview/prologue/supported-proxies/)

| Name                | Remark                                                                                                                      |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Traefik             | Automatic TLS, SD, TCP/UDP support, config heavy, web ui, use consul if needed                                              |
| Caddy               | Automatic TLS, Only HTTP support by default                                                                                 |
| Envoy               | Little extra for moi                                                                                                        |
| NGINX               | Good but needs extra configurations, can you [step-ca](https://smallstep.com/docs/step-ca)                                  |
| NGINX Proxy Manager | Ez and nice but maintenance is not [very](https://github.com/NginxProxyManager/nginx-proxy-manager/discussions/1202) active |
| Apache              | I used it in the past did not like it v.much don't remember why exactly                                                     |
| HAproxy             | Did not look into, putting for completeness sake                                                                            |

<div class="outline-3 smol-table">

#### DNS and reverse proxy {#dns-and-reverse-proxy}

-   Once you have a reverse-proxy setup, you can have your local DNS server point to your reverse proxy for whatever domain. eg. `*.home`
-   Some people recommend doing split-horizon DNS along with reverse-proxy if running multiple services, I don't see a point rn but maybe I'll later.

</div>

</div>

<div class="outline-2 smol-table">

### Router {#router}

-   There are three major players OPNSense, [PFSense](https://teklager.se/en/pfsense-vs-opnsense/), OpenWRT. These can be mixed and matched, eg. You can have OPNSense as the gateway and OpenWRT in the APs.
-   Between OPNSense and PFSense, better go with OPNSense
-   There are three major parts Router(Gateway), Firewall, Access Points(AP). All of this can be done by one device or separate device based on preference. Eg. You can run commercial routers in AP mode and have some old laptop be the router, or simply use a commercial router which will do all 3 etc.
-   Things you can do(most of them overkill for a homelab): policy routing, firewalling, DNS filtering, I(D/P)S, Dual WAN, monitoring, AntiBufferBloat, traffic shaping, RADIUS etc.
-   Few things about OpenWRT
    -   Started as a firmware replacement for a Linksys WRT54G, ended up being a powerful Linux-based router OS
    -   Designed to run on small embedded devices, like commercial routers and single board computers. can also run x86
    -   Designed to be a powerful wireless access point/router.
    -   Firewall is good but the \*Sense are better at this.
    -   Upgrading to a newer versions is little painful
-   Point web services logs to fail2ban and let it handle rate-limiting etc.
-   For extra points you can check Crowdsec

</div>

<div class="outline-2 smol-table">

### DNS {#dns}

This one is a bad boy. i probably just want to resolver with security.

</div>

<div class="outline-2 smol-table">

### Local Network {#local-network}

<div class="outline-3 smol-table">

#### VLANs {#vlans}

-   **Reason:** It's nice to separate things with vlans and firewall rules + IoT devices are known to be [insecure](https://www.reddit.com/r/hacking/comments/rt7k6y/how_does_an_entire_network_get_compromised_after/). (Sort of an overkill in someways but like jff)
-   VLANs are a layer 2 technology (they break up a broadcast domain into separate logical networks). You can get a managed switch otherwise OpenWRT [can help](https://www.reddit.com/r/openwrt/comments/vaqhph/vlans_without_a_builtin_switch/) you do it aswell.
-   IoT devices like smart TV, voice assistants, security cameras etc. which cannot run a VPN client should be in a different VLAN.
-   Strategy
    -   VLAN 1 is used for home devices LAN
    -   VLAN 2 is used for trusted IoT, which I allow access to the Internet
    -   VLAN 3 is used for isolated (untrusted) IoT devices
    -   VLAN 4 for DMZ for publicly hosted services etc
    -   What comes and goes out of these VLANS to be configured via firewalls
    -   VPN runs on VLAN1

</div>

<div class="outline-3 smol-table">

#### DMZ {#dmz}

-   Reason: Because I plan to host public facing services it makes sense to have a DMZ.
-   What is a DMZ is very confusing, different people mean different things. I am going with whatever wikipedia tells for [consistency](https://en.wikipedia.org/wiki/DMZ_(computing)#DMZ_host). **Image for ref. not exact topology.**

{{< figure src="/ox-hugo/dmz.png" >}}

-   The objective is to provide firewall capabilities between hosts in the DMZ and hosts on the internal network.

</div>

</div>

<div class="outline-2 smol-table">

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

<div class="outline-2 smol-table">

### Mesh Networks {#mesh-networks}

<div class="book-hint warning small-text">

> Now this is something I do not want to do right away but 100% want to experiment with it. Super exciting stuff.
</div>

-   [Using Yggdrasil As an Automatic Mesh Fabric to Connect All Your containers](https://changelog.complete.org/archives/10461-using-yggdrasil-as-an-automatic-mesh-fabric-to-connect-all-your-docker-containers-vms-and-servers)
-   [What Happens Inside a 100-hop IPv6 Wireless Mesh Network?](https://www.thingsquare.com/blog/articles/100-hops-ipv6-mesh/)
-   [WikiStart - Open-Mesh - B.A.T.M.A.N](https://www.open-mesh.org/projects/open-mesh/wiki)
-   [NetHood - Bridging the digital with the physical](https://archive.is/KnsnU)
-   [Meshtastic](https://meshtastic.org/)
-   [cjdelisle/cjdns](https://github.com/cjdelisle/cjdns)
-   [NYC Mesh](https://www.nycmesh.net/)

</div>

</div>

<div class="outline-1 smol-table">

## Backup Plan {#backup-plan}

After some reading and going through [various backup](https://github.com/restic/others) solutions, I decided that the primary tool to make my backups will be [restic](https://restic.net/). I initially considered [borg with rysnc.net](https://www.rsync.net/products/borg.html), but using restic lets me use cheaper storage alternatives and at the time of this writing I am trying to cut costs.

<div class="outline-2 smol-table">

### Data inventory {#data-inventory}

-   Laptop's home directory
-   Configuration files
-   Bitwarden
-   SSH, Age keys
-   Github repos
-   Google photos

</div>

<div class="outline-2 smol-table">

### What(change later) {#what--change-later}

-   I store backups of my critical data on 2 externals (1 at home and 1 at work) and have cloud backups.
-   NAS
-   I just use restic (incremental encrypted backup) to Backblaze b2. (offsite backup)
-   People usually do not backup media(esp movies etc.) but if you want to do, rather not do that in offsite backup into another NAS or something

</div>

<div class="outline-2 smol-table">

### Notes {#notes}

-   I am not doing any filesystem backups(yet)

</div>

</div>

<div class="outline-1 smol-table">

## Best practices {#best-practices}

<div class="outline-2 smol-table">

### Hardening system {#hardening-system}

-   Reverse proxy only accepting domain-name queries instead of the IP.
-   `PermitRootLogin no` in your `sshd_config` file.
-   [How to Set Up and Secure a Compute Instance | Linode](https://www.linode.com/docs/products/compute/compute-instances/guides/set-up-and-secure/)
-   [Linux Hardening Guide](https://madaidans-insecurities.github.io/guides/linux-hardening.html)
-   [Linux Security Hardening and Other Tweaks](https://vez.mrsk.me/linux-hardening.html)
-   [imthenachoman/How-To-Secure-A-Linux-Server](https://github.com/imthenachoman/How-To-Secure-A-Linux-Server)

</div>

<div class="outline-2 smol-table">

### Environment {#environment}

-   [Best practices for segmentation of the corporate network of any company](https://github.com/sergiomarotco/Network-segmentation-cheat-sheet)
-   [doitintl/secure-gcp-reference](https://github.com/doitintl/secure-gcp-reference)

</div>

<div class="outline-2 smol-table">

### Observability {#observability}

-   [samber/awesome-prometheus-alerts](https://github.com/samber/awesome-prometheus-alerts): Collection of Prometheus alerting rules
-   [monitoringsucks/metrics-catalog](https://github.com/monitoringsucks/metrics-catalog): Catalog of valuable metrics you might want to collect
-   [Enapiuz/awesome-monitoring](https://github.com/Enapiuz/awesome-monitoring): List of tools for monitoring and analyze everything.

</div>

<div class="outline-2 smol-table">

### Security {#security}

-   [Who’s Attacking My Server?](https://bastian.rieck.me/blog/posts/2022/server/)

</div>

</div>

<div class="outline-1 smol-table">

## Resources {#resources}

-   [Home | LinuxServer.io](https://www.linuxserver.io/) : Community Images
-   [ligurio/awesome-ci: List of Continuous Integration services](https://github.com/ligurio/awesome-ci)
-   [Why should I switch from Restic to Borg?](https://www.reddit.com/r/BorgBackup/comments/v3bwfg/why_should_i_switch_from_restic_to_borg/) : Nice comparison between restic and borg
-   [geerlingguy/my-backup-plan](https://github.com/geerlingguy/my-backup-plan) : inspiration for my backup plan

<div class="outline-2 smol-table">

### Compute providers {#compute-providers}

| Name                                                                      | Remark                                                                                                                              |
|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [Vultr](https://www.vultr.com/)                                           |                                                                                                                                     |
| [Exoscale](https://www.exoscale.com/)                                     |                                                                                                                                     |
| [Hetzner](https://www.hetzner.com/)                                       | Good value for VPS, support, transparent, peering issues                                                                            |
| [Time4VPS](https://www.time4vps.com/)                                     |                                                                                                                                     |
| [Uberspace](https://uberspace.de/en/product/#prices)                      | Unique "shared server" concept. In theory you can use as much ressources as you want but in that case other customers are impacted. |
| [Scaleway](https://www.scaleway.com/en/)                                  | Complaints about support                                                                                                            |
| [Oracle](https://www.oracle.com/cloud/free/#always-free)                  | It's a free tire but lot of complaints about dark patterns. Use it w caution.                                                       |
| [Tornado VPS](https://tornadovps.com/)                                    | poop                                                                                                                                |
| [Linode](https://www.linode.com/)                                         | Little pricy but trusy                                                                                                              |
| [DigitalOcean](https://www.digitalocean.com/)                             | Little pricy but trusy(2)                                                                                                           |
| [RackNerd](https://my.racknerd.com/index.php?rp=/store/black-friday-2022) | Black friday yearly deal is juicy                                                                                                   |
| [netcup](https://www.netcup.eu/)                                          |                                                                                                                                     |
| [SSD Nodes](https://www.ssdnodes.com/)                                    | Cheap stuff but good                                                                                                                |
| [OVH](https://www.ovhcloud.com/en-ie/)                                    | French company, once data center caught fire but otherwise reviews are mixed. Interesting bare metal offerings                      |

<div class="outline-3 smol-table">

#### Other server resources {#other-server-resources}

-   [Server Hunter](https://www.serverhunter.com)
-   [BuyVM](https://buyvm.net/)
-   [LowEndBox](https://lowendbox.com/)
-   [Cloud server CPU performance comparison](https://jan.rychter.com/enblog/cloud-server-cpu-performance-comparison-2019-12-12)
-   [How much can you really get out of a 4$ VPS?](https://alicegg.tech//2023/02/06/4dollar-vps.html)

</div>

</div>

<div class="outline-2 smol-table">

### Storage providers {#storage-providers}

| Name                  | Remark |
|-----------------------|--------|
| Hetzner storage boxes |        |
| Blackblaze B2         |        |

<div class="outline-3 smol-table">

#### Storage resources {#storage-resources}

-   [Storage Calculator](https://www.reddit.com/r/DataHoarder/comments/ocaglt/interactive_graphing_calculator_for_cloud_storage/)
-   [CostStorage.com](http://coststorage.com/)
-   [Object Storage Price Comparison - qBackup](https://www.qualeed.com/en/qbackup/cloud-storage-comparison/)

</div>

</div>

</div>

<div class="outline-1 smol-table">

## Hardware {#hardware}

<div class="outline-2 smol-table">

### Products {#products}

-   [ZimaBoard - World's First Hackable Single Board Server](https://www.zimaboard.com/)
-   [Synology Inc.](https://www.synology.com/en-global)
-   [FRITZ!Box | AVM International](https://en.avm.de/products/fritzbox/)
-   [Dream Machine Pro – Ubiquiti Inc.](https://store.ui.com/products/udm-pro)
-   [HP USB-C G5 Essential Dock](https://www.hp.com/us-en/shop/pdp/hp-usb-c-g5-essential-dock)
-   [MINISFORUM DeskMini UM350 Mini PC ](https://www.amazon.com/UM250-Windows-Computer-Output-Graphics/dp/B08QZC6H8Q)
-   [The Modern, Open-Source KVM over IP | TinyPilot](https://tinypilotkvm.com/)
-   [Garmin inReach Explorer+, Handheld Satellite Communicator](https://www.amazon.com/Garmin-Explorer-Satellite-Communicator-Navigation/dp/B01MY03CZP)
-   [USB Numeric Keypad Portable Slim Mini Number Pad](https://www.amazon.in/SPIN-CART-Numeric-Portable-Computer/dp/B07FTBKJ6T)
-   [Cat S62 Pro Smartphone | Cat phones USA](https://www.catphones.com/en-us/cat-s62-pro-smartphone/)
-   [DeviceFarmer/stf: Control and manage Android devices from your browser.](https://github.com/DeviceFarmer/stf)
-   [Custom made portable PC](https://www.reddit.com/r/homelab/comments/xm76nm/moved_my_allinone_pentest_lab_from_a_2u_case_to_a/)

</div>

<div class="outline-2 smol-table">

### Guides {#guides}

-   [Aluminum T-slot Building Systems – Build your Idea | Hacker News](https://news.ycombinator.com/item?id=34567318)
-   [GitHub - help-14/mechanical-keyboard: DIY mechanical keyboard and where to find them](https://github.com/help-14/mechanical-keyboard)
-   [GitHub - haimgel/display-switch: Turn a $30 USB switch into a kvm sw](https://github.com/haimgel/display-switch)
-   [GitHub - seemoo-lab/openhaystack: Build your own 'AirTags'](https://github.com/seemoo-lab/openhaystack)
-   [Help us improve the flight coverage in your area](https://planefinder.net/coverage)
-   [ESP32 Buyer’s Guide: Different Chips, Firmware, Sensors](https://eitherway.io/posts/esp32-buyers-guide/)
-   [A Beginner's Guide to Houseplants](https://www.notion.so/A-Beginner-s-Guide-to-Houseplants-f90190a8c15b4bb8b65c60f16e3f9502)
-   [Notes on RSI for Developers](https://www.swyx.io/rsi-tips)

</div>

</div>

<div class="outline-1 smol-table">

## Other Homelabs {#other-homelabs}

-   [How I re-over-engineered my home network for privacy and security | Ben Balter](https://ben.balter.com/2021/09/01/how-i-re-over-engineered-my-home-network/)
-   [My Homelab Build - Xe Iaso](https://xeiaso.net/blog/my-homelab-2021-06-08)
-   [Home Lab Beginners guide - Hardware](https://haydenjames.io/home-lab-beginners-guide-hardware/)
-   [Building a better home network | Kevin Burke](https://kevin.burke.dev/kevin/building-a-better-home-network/)
-   [My network home setup - v4.0 | etcetera](https://giuliomagnifico.blog/networking/2023/01/05/home-network_v4.html)
-   [Setting up a Raspberry Pi with 2 Network Interfaces as a very simple router](https://www.jeffgeerling.com/blog/2021/setting-raspberry-pi-2-network-interfaces-very-simple-router)
-   [khuedoan/homelab](https://github.com/khuedoan/homelab)
-   /r/homelab /r/selfhosted

</div>

<div class="outline-1 smol-table">

## Selfhosting Lingo {#selfhosting-lingo}

There are few pointy things to be aware of when making decisions about vendors, how to do things, what to buy etc. Few terms or set of terms that I think I might want to keep a note of.

<div class="outline-2 smol-table">

### Egress/Ingress {#egress-ingress}

> [Suppose](https://www.reddit.com/r/googlecloud/comments/uh9j8a/google_cloud_compute_engine_ingress_vs_egress/) you're running a VPN in a server and they charge you only for `egress`

-   Ingress
    -   Traffic coming into your VM. For example, if over your VPN to request a website in your browser, this request from your browser to the website would be ingress to the VM.
-   Egress
    -   Traffic leaving your VM. Using the above example, traffic that leaves your VM to the website to get the request is egress. When the VM get's the response from the website (ingress, free), it then has to send that response over the VM to your computer (egress, not free).
    -   Cloud companies charge egress fees when customers want to move their data out of the provider’s platform. i.e more egress fee = sort of [vendor lock in attempt](https://www.cloudflare.com/bandwidth-alliance/)

Visually, a request/response to a website over your VPN looks like this:

```nil
Your PC ----ingress---> VM ----egress---> Website
Website ----ingress---> VM ----egress---> Your PC
```

In this case, you are charged for all egress.

</div>

<div class="outline-2 smol-table">

### local/onsite/offsite backups {#local-onsite-offsite-backups}

-   Local: copy in your machine
-   Onsite: External drive fits [perfectly](https://www.hyper-v.io/keep-backups-lets-talk-backup-storage-media/)
-   Offsite: Either cloud storage or an external drive that you can keep in a different location.

</div>

<div class="outline-2 smol-table">

### sync/backup {#sync-backup}

Understanding this helped me better plan my backup strategy.

-   Sync
    -   When you’re using a sync service, you can easily delete or change a file, save it, and then lose the one you actually wanted to keep.
    -   Allow you to access your files across different devices.
    -   Share files with other users
-   Backup
    -   Usually work automatically in the background of your computer
    -   Backing up a **copy** of your new or changed data to another location
    -   A good backup will have versioning and restore set correctly

</div>

<div class="outline-2 smol-table">

### Flat tired/Tired pricing {#flat-tired-tired-pricing}

-   Flat tired Pricing: Charges the user based on the storage volume, and cost is typically expressed per gigabyte stored. There is only one tier.
-   Tired Pricing: A provider may have a small business pricing tier and an enterprise tier.

</div>

<div class="outline-2 smol-table">

### Minimum Retention Periods {#minimum-retention-periods}

It sounds innocent but some providers may charge you for deleting data before the retention period! beware.

</div>

</div>

<div class="outline-1 smol-table">

## Aesthetics {#aesthetics}

-   [corkami/pics](https://github.com/corkami/pics) : Posters, drawings.
-   [The Unix Magic Poster | Hacker News](https://news.ycombinator.com/item?id=27029196)
-   [Investing in lighting did great things for my mental and physical health](https://www.bramadams.dev/projects/invest-in-lights)

</div>
