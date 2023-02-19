+++
title = "Primary tool-chest"
author = ["Hrishikesh Barman"]
draft = false
+++

<div class="outline-1nil">

## Handy {#handy}

These are not study notes. Study notes will probably be there in [🐄](https://mogoz.geekodour.org/)

-   Dotfiles: **Private**. So the following will probably be inaccessible to you if you're not me.
-   Alias: [My fish functions](https://github.com/geekodour/dottedflies/tree/main/.config/fish/functions).🐟
-   Snippets: [Moi YASnippets](https://github.com/geekodour/dottedflies/tree/main/.config/doom/snippets).
-   Cheatsheets: [Moi cheatkodes](https://github.com/geekodour/dottedflies/tree/main/.config/cheat/personal).

</div>

<div class="outline-1nil">

## Workflows {#workflows}

<div class="outline-2nil">

### General Development Tooling {#general-development-tooling}

Now how I do development has varied over the years. But I am constantly updating it. This section is a scratchpad area for links/notes about current or probable future workflow.

I am planning to checkout online sandboxes for development(candidates: [CodeSandbox](https://codesandbox.io/s/), [StackBlitz](https://stackblitz.com/), [Replit](https://replit.com/), [Glitch](https://glitch.com/)) as well try [using AI tools](https://lobste.rs/s/dfmiko/using_github_copilot_for_unit_testing) for development

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                                 | Remark                                                                                                                                                                                                                   |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Prettier](https://prettier.io/)                     | This integrates nicely with emacs for my web dev needs as of the moment.                                                                                                                                                 |
| [DOOM Emacs](https://github.com/doomemacs/doomemacs) | 6969                                                                                                                                                                                                                     |
| [Git](https://en.wikipedia.org/wiki/Git)             | Life saver                                                                                                                                                                                                               |
| [ASDF](https://asdf-vm.com/)                         | I use it to install different plugins(nodejs/python) and their versions. Can scope the version to be global/local etc. pretty neat.                                                                                      |
| [Fish](https://fishshell.com/)                       | Of all the shells I’ve used, fish do be the best for personal computer use.                                                                                                                                              |
| [direnv](https://direnv.net/)                        | direnv is an environment-variables manager. It can update your shell env upon directory change and clean it up when you leave that directory. I use it along with  asdf and fish. Just make sure to set direnv globally. |
| [Neovim](https://neovim.io/)                         | 69                                                                                                                                                                                                                       |
| [Github](https://github.com/)                        | Hosting personal git repos and playing w other repos out there                                                                                                                                                           |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                                 | Remark                                                                                                                                 |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [LXD](https://linuxcontainers.org/lxd/introduction/) | LXD is a manager/hypervisor for containers and vms. I use it when I need greater need of sandboxing for any project I am working with. |
| [Bitbucket](https://bitbucket.org/)                  | I host client projects/freelance projects here.                                                                                        |
</div>
</details>

</div>

<div class="outline-2nil">

### Data Engineering {#data-engineering}

Generally I have to fiddle with the data before I even realize what approach to take.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                        | Remark                                                                                                                                       |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Airtable](https://airtable.com/)           | I use airtable for a number of usecases, self quantification, to quickly prototype a database for client project, to organize some info etc. |
| [SQLite](https://www.sqlite.org/index.html) | My goto                                                                                                                                      |
</div>
</details>

</div>

<div class="outline-2nil">

### Data Analysis/Viz {#data-analysis-viz}

Doing this stuff manually is fun but ton of tools to make things fast for me. It only makes sense to make use of these tools.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                        | Remark                                                           |
|---------------------------------------------|------------------------------------------------------------------|
| [Desmos](https://www.desmos.com/calculator) | Quick gramphs                                                    |
| [Datasette](https://datasette.io/)          | Neat tool. Written by one of my favorite makers on the internet. |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                      | Remark                                                           |
|-------------------------------------------|------------------------------------------------------------------|
| [ObservableHQ](https://observablehq.com/) | I find this pretty neat. Haven't tried but want to try very soon |
</div>
</details>

</div>

<div class="outline-2nil">

### Infrastructure Management {#infrastructure-management}

I haven't fiddled with infra stuff in a while but it's always a combination of so many things. Shell scripts, custom programs, infra tools, external tools and so on. I plan to streamline this process eventually.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                   | Remark              |
|----------------------------------------|---------------------|
| [Prometheus](https://prometheus.io/)   | Anything monitoring |
| [Terraform](https://www.terraform.io/) | Managing big bois   |
</div>
</details>

</div>

<div class="outline-2nil">

### General Python Development {#general-python-development}

I like python. Makes it super easy to prototype things esp data related projects. I try not to delve too much into the ecosystem of tools here and try to use tools that just do the job and get out of my way. Understanding how python's import system works is a big one.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                    | Remark                                                                                                                                                                                                                                                       |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pudb](https://github.com/inducer/pudb) | Combined with iPython, I am having a fun debugging experience in Python                                                                                                                                                                                      |
| [Poetry](https://python-poetry.org/)    | Python packaging and dependency management. This is installed independently globally. Using the asdf version. I use this for my python virtual environment management. ASDF does not create me a virtual environment, this does. (got me confused initially) |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                       | Remark                                                                                                                            |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [Pylint](https://pypi.org/project/pylint/) | Flycheck on emacs uses pylint, but having issues of it not working great with virtual environments. Will have to figure that out. |
| [Black](https://github.com/psf/black)      | There are some arguments against black, but I am going with it as of the moment as it comes baked in with doom emacs.             |
</div>
</details>

</div>

<div class="outline-2nil">

### General Web Development {#general-web-development}

I want to move more towards web engineering vs the common idea of web development, I think it's more fun for me. Steering the wheel in that direction.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                    | Remark                                                                                                                                      |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [Vercel](https://vercel.com/)           | Anything next.js goes here baby                                                                                                             |
| [TailwindCSS](https://tailwindcss.com/) | I just use the CSS library not the UI kit, along with headless UI gives me most of the things required to prototype most things. I love it. |
| [Netlify](https://www.netlify.com/)     | All my static sites go here                                                                                                                 |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                            | Remark                                                                                            |
|---------------------------------|---------------------------------------------------------------------------------------------------|
| [caniuse](https://caniuse.com/) | "Can I use" provides up-to-date browser support tables for support of front-end web technologies. |
</div>
</details>

</div>

<div class="outline-2nil">

### Pure Frontend Development {#pure-frontend-development}

I don't do frontend development often but when I do I always find myself fighting with CSS the most. I am totally in for complex(rather simple) javascript application or any webstack for that matter but I would love to stay away from CSS as much as possible. I think TailwindCSS really saved my ass here. I wants to do creative programming but I needs a mix of things. I will focus on it someday but not yet.

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                           | Remark                                                   |
|------------------------------------------------|----------------------------------------------------------|
| [CSS Almanac](https://css-tricks.com/almanac/) | Good friendly reference for CSS properties and selectors |
| [animista](https://animista.net/)              | Lets me experiment with CSS Animation easily             |
| [svgartista](https://svgartista.net/)          | Lets me experiment with SVG Animation easily             |
</div>
</details>

</div>

<div class="outline-2nil">

### Network Troubleshooting {#network-troubleshooting}

Nothing is more annoying that getting disconnected. Even if I can't fix it I need to know what's up.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                                | Remark                                                |
|-----------------------------------------------------|-------------------------------------------------------|
| [Wireshark](https://www.kali.org/tools/macchanger/) | Needs no description but saved my ass couple of times |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                                 | Remark                                       |
|------------------------------------------------------|----------------------------------------------|
| [wavemon](https://github.com/uoaerg/wavemon)         | We're testing AP connectivity at ETHIndia'22 |
| [macchanger](https://www.kali.org/tools/macchanger/) | Whenever I need to change my mac address     |
</div>
</details>

</div>

<div class="outline-2nil">

### Planning/Brainstorming/Curation {#planning-brainstorming-curation}

Planning things and getting ideas is important for me before I start anything. I do not have any specific workflow as such but I make sure to think what will be the best way to think about this problem before I start thinking about the problem itself.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                              | Remark                                                                                                    |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------|
| [zotero](https://www.zotero.org/) | Keeping track of research papers. Currently using with firefox connector and the zotero-beta AUR package. |
| [Linear](https://linear.app/)     | I love linear. Whenever work with some team I prefer linear                                               |
| [TLDraw](https://www.tldraw.com/) | Online whiteboard                                                                                         |
</div>
</details>

</div>

<div class="outline-2nil">

### Communication and Discussions {#communication-and-discussions}

Asking the [right questions](http://www.catb.org/esr/faqs/smart-questions.html) is important. Having casual discussions is also important. I have so much problem communicating with other people idk where do I even start.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                                   | Remark                                                                                                       |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [Telegram](https://telegram.org/)      | Bots and few friends                                                                                         |
| [SimpleLogin](https://simplelogin.io/) | Nice open source anonymous email service, I currently use the provided one but might selfhost in the future. |
| [The Lounge](https://thelounge.chat/)  | I host this IRC server on my home rpi b+. Butter smooth from all devices.                                    |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                            | Remark                                                                             |
|---------------------------------|------------------------------------------------------------------------------------|
| [Discord](https://discord.com/) | I only understood how discord works after I created a server and tried being a mod |
</div>
</details>

</div>

<div class="outline-2nil">

### Art/Design {#art-design}

I wants to do art/design but not at the moment. I also wanted to make weird game videos using assets etc. But I might have to pause that for a while as it does not directly feed into my primary goals but I definitely want to make time for it.

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                       | Remark                                         |
|--------------------------------------------|------------------------------------------------|
| [MagicaVoxel](https://ephtracy.github.io/) | For trying out voxel art(haven't tried it yet) |
</div>
</details>

</div>

<div class="outline-2nil">

### AI/ML experiments {#ai-ml-experiments}

I absolutely know nothing of AI/ML but want to get into it. I also have a syllabus made for math and AI studies. Meanwhile I want to experiment with
[Hugging Face](https://huggingface.co/), [jerryjliu/gpt_index](https://github.com/jerryjliu/gpt_index), [hwchase17/langchain](https://github.com/hwchase17/langchain), OpenAI stuff

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                                                               | Remark                             |
|------------------------------------------------------------------------------------|------------------------------------|
| [ stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | For running SD experiments locally |
</div>
</details>

</div>

<div class="outline-2nil">

### Conversion/transformation {#conversion-transformation}

Converting stuff from one format to another is all we do.

<details class="book-hint info small-text mb-2">
<summary>Primary Tools</summary>
<div class="details">

| Name                            | Remark                                                                                                                              |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| [Squoosh](https://squoosh.app/) | My goto online image resizer. I heard they had less members on the team so cannot maintain this project well. That's extremely sad. |
</div>
</details>

<details class="book-hint warning small-text">
<summary>Additional Resources/Tools</summary>
<div class="details">

| Name                                            | Remark                                                                                                                                                                                                         |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [transform](https://transform.tools/)           | A polyglot web converter. Pretty handy.                                                                                                                                                                        |
| [CyberChef](https://gchq.github.io/CyberChef/)  | A simple, intuitive web app for analysing and decoding data without having to deal with complex tools or programming languages.                                                                                |
| [onlinelisttools](https://onlinelisttools.com/) | Online List Tools World's simplest list utilities . Currently this only has list but new stuff should be added soon. Nice when I want to quickly do something with a list without reading out to any language. |
</div>
</details>

</div>

</div>

<div class="outline-1nil">

## Generated {#generated}

<div class="book-hint info">

> These following lists are generated [here](https://github.com/geekodour/systemfiles/) and not in sync with my system at all times.
</div>

<div class="outline-2nil">

### Firefox Extensions {#firefox-extensions}

| Name                                                                                                                                                         | Description                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tab Stash](https://addons.mozilla.org/en-US/firefox/addon/tab-stash/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=homepage-primary-hero)   | A no-fuss way to save and restore batches of tabs as bookmarks.                                                                                                                                                        |
| [Sidebery](https://addons.mozilla.org/en-US/firefox/addon/sidebery/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                  | Addon for managing tabs, containers (contextual identities) and bookmarks in sidebar. Supports both flat and tree tabs layouts, per-container include/exclude rules, proxy configs for each container and much more.   |
| [Emoji](https://addons.mozilla.org/en-US/firefox/addon/emoji-sav/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                    | It permits just with a single click to copy and insert an emoji. You can also customise the add-on.                                                                                                                    |
| [Auto Tab Discard](https://addons.mozilla.org/en-US/firefox/addon/auto-tab-discard/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)  | Increase browser speed and reduce memory load when you have numerous open tabs.                                                                                                                                        |
| [Impulse Blocker](https://addons.mozilla.org/en-US/firefox/addon/impulse-blocker/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)    | Block distracting websites when you are browsing the web.                                                                                                                                                              |
| [ClearURLs](https://addons.mozilla.org/en-US/firefox/addon/clearurls/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                | Remove tracking elements from URLs.                                                                                                                                                                                    |
| [SingleFile](https://addons.mozilla.org/en-US/firefox/addon/single-file/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)             | Save a complete page into a single HTML file                                                                                                                                                                           |
| [Flagfox](https://addons.mozilla.org/en-US/firefox/addon/flagfox/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                    | Displays a flag depicting the location of the current server                                                                                                                                                           |
| [Imagus](https://addons.mozilla.org/en-US/firefox/addon/imagus/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                      | Enlarge thumbnails, and show images/videos from links with a mouse hover.                                                                                                                                              |
| [Dark Reader](https://addons.mozilla.org/en-US/firefox/addon/darkreader/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)             | Dark mode for every website. Take care of your eyes, use dark theme for night and daily browsing.                                                                                                                      |
| [Web Archives](https://addons.mozilla.org/en-US/firefox/addon/view-page-archive/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)     | View archived and cached versions of web pages on 10+ search engines, such as the Wayback Machine, Archive․is, Google, Bing, Yandex, Baidu and Yahoo                                                                   |
| [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)                                                                               | Finally, an efficient blocker. Easy on CPU and memory.                                                                                                                                                                 |
| [Cookie Quick Manager](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/)                                                                 | An addon to manage (view, search, create, edit, delete, backup, restore) cookies.                                                                                                                                      |
| [What Hacker News Says](https://addons.mozilla.org/en-US/firefox/addon/what-hacker-news-says/)                                                               | Easily find Hacker News threads about the page you're currently browsing.                                                                                                                                              |
| [LocalCDN](https://addons.mozilla.org/en-US/firefox/addon/localcdn-fork-of-decentraleyes/)                                                                   | Protects you against tracking through CDNs (Content Delivery Networks) by redirecting to local resources.                                                                                                              |
| [WhatFont](https://addons.mozilla.org/en-US/firefox/addon/zjm-whatfont/)                                                                                     | A wrapper for Chengyhin Liu's WhatFont tool                                                                                                                                                                            |
| [uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)                      | Point &amp; click to forbid/allow any class of requests made by your browser. Use it to block scripts, iframes, ads, facebook, etc.                                                                                    |
| [Debug CSS](https://addons.mozilla.org/en-US/firefox/addon/pranay-joshi/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)               | Adds outline to all elements on the page to show the culprit element which is changing desired layout                                                                                                                  |
| [Library Extension](https://addons.mozilla.org/en-US/firefox/addon/libraryextension/)                                                                        | &lt;nil&gt;                                                                                                                                                                                                            |
| [SponsorBlock for YouTube - Skip Sponsorships](https://addons.mozilla.org/en-US/firefox/addon/sponsorblock/)                                                 | Skip sponsorships, subscription begging and more on YouTube videos. Report sponsors on videos you watch to save others' time.                                                                                          |
| [Tweak New Twitter](https://addons.mozilla.org/en-US/firefox/addon/tweak-new-twitter/)                                                                       | Remove algorithmic content from Twitter, hide news &amp; trends, control which shared tweets appear on your timeline, and improve the UI                                                                               |
| [React Developer Tools](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) | Adds React debugging tools to the Firefox Developer Tools.Created from revision 47f63dc54 on 12/6/2022.                                                                                                                |
| [Zotero Connector](https://www.zotero.org/download/connectors)                                                                                               | Save references to Zotero from your web browser                                                                                                                                                                        |
| [Hello, Goodbye](https://addons.mozilla.org/en-US/firefox/addon/hello-goodbye/)                                                                              | Hello, Goodbye blocks annoying chat widgets.                                                                                                                                                                           |
| [Reddit Enhancement Suite](https://addons.mozilla.org/en-US/firefox/addon/reddit-enhancement-suite/)                                                         | A suite of modules that enhance your Reddit browsing experience                                                                                                                                                        |
| [uBlacklist](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/)                                                                                     | Blocks sites you specify from appearing in Google search results                                                                                                                                                       |
| [Video Speed Controller](https://addons.mozilla.org/en-US/firefox/addon/videospeed/)                                                                         | Speed up, slow down, advance and rewind HTML5 audio/video with shortcuts                                                                                                                                               |
| [Refined GitHub](https://addons.mozilla.org/en-US/firefox/addon/refined-github-/)                                                                            | Simplifies the GitHub interface and adds useful features                                                                                                                                                               |
| [Tridactyl](https://addons.mozilla.org/en-US/firefox/addon/tridactyl-vim/)                                                                                   | &lt;nil&gt;                                                                                                                                                                                                            |
| [Bitwarden - Free Password Manager](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/)                                              | A secure and free password manager for all of your devices.                                                                                                                                                            |
| [I don't care about cookies](https://addons.mozilla.org/en-US/firefox/addon/i-dont-care-about-cookies/)                                                      | &lt;nil&gt;                                                                                                                                                                                                            |
| [Temporary Containers](https://addons.mozilla.org/en-GB/firefox/addon/temporary-containers/)                                                                 | Open tabs, websites, and links in automatically managed disposable containers. Containers isolate the data websites store (cookies, cache, and more) from each other, further enhancing your privacy while you browse. |

</div>

<div class="outline-2nil">

### Arch Official Packages {#arch-official-packages}

| Name                                                                                                | Description                                                                                                    |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [adobe-source-han-sans-jp-fonts](https://github.com/adobe-fonts/source-han-sans)                    | Adobe Source Han Sans Subset OTF - Japanese OpenType/CFF fonts                                                 |
| [age](https://github.com/FiloSottile/age)                                                           | A simple, modern and secure file encryption tool                                                               |
| [aircrack-ng](https://www.aircrack-ng.org)                                                          | Key cracker for the 802.11 WEP and WPA-PSK protocols                                                           |
| [alacritty](https://github.com/alacritty/alacritty)                                                 | A cross-platform, GPU-accelerated terminal emulator                                                            |
| [alsa-utils](https://www.alsa-project.org)                                                          | Advanced Linux Sound Architecture - Utilities                                                                  |
| [autoconf](https://www.gnu.org/software/autoconf)                                                   | A GNU tool for automatically configuring source code                                                           |
| [automake](https://www.gnu.org/software/automake)                                                   | A GNU tool for automatically creating Makefiles                                                                |
| [bandwhich](https://github.com/imsnif/bandwhich)                                                    | Terminal bandwidth utilization tool                                                                            |
| [base](https://www.archlinux.org)                                                                   | Minimal package set to define a basic Arch Linux installation                                                  |
| [bat](https://github.com/sharkdp/bat)                                                               | Cat clone with syntax highlighting and git integration                                                         |
| [bison](https://www.gnu.org/software/bison/bison.html)                                              | The GNU general-purpose parser generator                                                                       |
| [bluez-utils](http://www.bluez.org/)                                                                | Development and debugging utilities for the bluetooth protocol stack                                           |
| [bmon](https://github.com/tgraf/bmon/)                                                              | Portable bandwidth monitor and rate estimator                                                                  |
| [bookworm](https://babluboy.github.io/bookworm)                                                     | A simple user centric eBook reader which displays multiple eBooks formats uniformly                            |
| [bottom](https://github.com/ClementTsang/bottom)                                                    | A graphical process/system monitor                                                                             |
| [brightnessctl](https://github.com/Hummer12007/brightnessctl)                                       | Lightweight brightness control tool                                                                            |
| [catimg](https://github.com/posva/catimg)                                                           | Print images in a terminal with 256 colors support                                                             |
| [chafa](https://hpjansson.org/chafa/)                                                               | Image-to-text converter supporting a wide range of symbols and palettes, transparency, animations, etc.        |
| [cloudflared](https://github.com/cloudflare/cloudflared)                                            | Command-line client for Cloudflare Tunnel                                                                      |
| [cmake](https://www.cmake.org/)                                                                     | A cross-platform open-source make system                                                                       |
| [cmus](https://cmus.github.io/)                                                                     | Feature-rich ncurses-based music player                                                                        |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term)                                   | A good looking terminal emulator which mimics the old cathode display                                          |
| [curlie](https://curlie.io)                                                                         | The power of curl, the ease of use of httpie.                                                                  |
| [dbeaver](https://dbeaver.io/)                                                                      | Free universal SQL Client for developers and database administrators (community edition)                       |
| [diffoscope](https://diffoscope.org/)                                                               | Tool for in-depth comparison of files, archives, and directories                                               |
| [discord](https://discord.com)                                                                      | All-in-one voice and text chat for gamers                                                                      |
| [dive](https://github.com/wagoodman/dive)                                                           | A tool for exploring each layer in a docker image                                                              |
| [dog](https://github.com/ogham/dog)                                                                 | Command-line DNS client like dig                                                                               |
| [dstat](http://dag.wieers.com/home-made/dstat/)                                                     | A versatile resource statistics tool                                                                           |
| [dua-cli](https://github.com/Byron/dua-cli)                                                         | A tool to conveniently learn about the disk usage of directories, fast!                                        |
| [duf](https://github.com/muesli/duf)                                                                | Disk Usage/Free Utility                                                                                        |
| [electron19](https://electronjs.org/)                                                               | Build cross platform desktop apps with web technologies                                                        |
| [element-desktop](https://element.io)                                                               | Glossy Matrix collaboration client — desktop version.                                                          |
| [emacs-nativecomp](https://www.gnu.org/software/emacs/emacs.html)                                   | The extensible, customizable, self-documenting real-time display editor with native compilation enabled        |
| [eva](https://github.com/nerdypepper/eva)                                                           | simple calculator REPL, similar to bc(1)                                                                       |
| [evtest](https://cgit.freedesktop.org/evtest/)                                                      | Input device event monitor and query tool                                                                      |
| [exa](https://the.exa.website/)                                                                     | ls replacement                                                                                                 |
| [fd](https://github.com/sharkdp/fd)                                                                 | Simple, fast and user-friendly alternative to find                                                             |
| [feh](https://feh.finalrewind.org/)                                                                 | Fast and light imlib2-based image viewer                                                                       |
| [firefox](https://www.mozilla.org/firefox/)                                                         | Standalone web browser from mozilla.org                                                                        |
| [fish](https://fishshell.com/)                                                                      | Smart and user friendly shell intended mostly for interactive use                                              |
| [gfold](https://github.com/nickgerace/gfold)                                                        | A CLI tool to help keep track of Git repositories                                                              |
| [git-delta](https://github.com/dandavison/delta)                                                    | Syntax-highlighting pager for git and diff output                                                              |
| [glances](https://github.com/nicolargo/glances)                                                     | CLI curses-based monitoring tool                                                                               |
| [gping](https://github.com/orf/gping)                                                               | Ping, but with a graph                                                                                         |
| [grex](https://github.com/pemistahl/grex)                                                           | A command-line tool for generating regular expressions from user-provided input strings                        |
| [grim](https://git.sr.ht/~emersion/grim)                                                            | Screenshot utility for Wayland                                                                                 |
| [handlr](https://github.com/chmln/handlr)                                                           | Powerful alternative to xdg-utils written in Rust                                                              |
| [hexyl](https://github.com/sharkdp/hexyl)                                                           | Colored command-line hex viewer                                                                                |
| [htop](https://htop.dev/)                                                                           | Interactive process viewer                                                                                     |
| [hugo](https://gohugo.io/)                                                                          | Fast and Flexible Static Site Generator in Go                                                                  |
| [hunspell-en_us](http://wordlist.aspell.net/dicts/)                                                 | US English hunspell dictionaries                                                                               |
| [hyperfine](https://github.com/sharkdp/hyperfine)                                                   | A command-line benchmarking tool                                                                               |
| [imv](https://sr.ht/~exec64/imv/)                                                                   | Image viewer for Wayland and X11                                                                               |
| [intel-ucode](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files)                  | Microcode update files for Intel CPUs                                                                          |
| [interception-dual-function-keys](https://gitlab.com/interception/linux/plugins/dual-function-keys) | Interception plugin for dual-function keys: Tap for one key, hold for another                                  |
| [iwd](https://git.kernel.org/cgit/network/wireless/iwd.git/)                                        | Internet Wireless Daemon                                                                                       |
| [kdeconnect](https://kdeconnect.kde.org/)                                                           | Adds communication between KDE and your smartphone                                                             |
| [keychain](https://www.funtoo.org/Keychain)                                                         | A front-end to ssh-agent, allowing one long-running ssh-agent process per system, rather than per login        |
| [kismet](https://www.kismetwireless.net/)                                                           | 802.11 layer2 wireless network detector, sniffer, and intrusion detection system                               |
| [kmon](https://github.com/orhun/kmon)                                                               | Linux kernel manager and activity monitor                                                                      |
| [linux-firmware](https://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git)            | Firmware files for Linux                                                                                       |
| [lolcat](https://github.com/busyloop/lolcat)                                                        | Okay, no unicorns. But rainbows!!                                                                              |
| [lostfiles](https://github.com/graysky2/lostfiles)                                                  | Find orphaned files not owned by any Arch packages                                                             |
| [lxd](https://linuxcontainers.org/lxd)                                                              | Daemon based on liblxc offering a REST API to manage containers                                                |
| [macchanger](https://www.gnu.org/software/macchanger)                                               | A small utility to change your NIC's MAC address                                                               |
| [maim](https://github.com/naelstrof/maim)                                                           | Utility to take a screenshot using imlib2                                                                      |
| [make](https://www.gnu.org/software/make)                                                           | GNU make utility to maintain groups of programs                                                                |
| [mako](https://mako-project.org)                                                                    | Lightweight notification daemon for Wayland                                                                    |
| [man-db](https://gitlab.com/cjwatson/man-db)                                                        | A utility for reading man pages                                                                                |
| [mediainfo](https://mediaarea.net/)                                                                 | Supplies technical and tag information about a video or audio file (CLI interface)                             |
| [miller](https://github.com/johnkerl/miller)                                                        | Name-indexed data processing tool                                                                              |
| [mold](https://github.com/rui314/mold)                                                              | A Modern Linker                                                                                                |
| [mpv](https://mpv.io/)                                                                              | a free, open source, and cross-platform media player                                                           |
| [neofetch](https://github.com/dylanaraps/neofetch)                                                  | A CLI system information tool written in BASH that supports displaying images.                                 |
| [neovim](https://neovim.io)                                                                         | Fork of Vim aiming to improve user experience, plugins, and GUIs                                               |
| [nethogs](https://github.com/raboof/nethogs)                                                        | A net top tool which displays traffic used per process instead of per IP or interface                          |
| [nfs-utils](http://nfs.sourceforge.net)                                                             | Support programs for Network File Systems                                                                      |
| [noto-fonts-cjk](https://www.google.com/get/noto/)                                                  | Google Noto CJK fonts                                                                                          |
| [nyancat](https://nyancat.dakko.us/)                                                                | Nyancat rendered in your terminal.                                                                             |
| [obs-studio](https://obsproject.com)                                                                | Free, open source software for live streaming and recording                                                    |
| [okular](https://apps.kde.org/okular/)                                                              | Document Viewer                                                                                                |
| [onefetch](https://github.com/o2sh/onefetch)                                                        | Git repository summary on your terminal                                                                        |
| [pacgraph](http://kmkeen.com/pacgraph/)                                                             | Draws a graph of installed packages to PNG/SVG/GUI/console. Good for finding bloat.                            |
| [pacman-contrib](https://gitlab.archlinux.org/pacman/pacman-contrib)                                | Contributed scripts and tools for pacman systems                                                               |
| [pacutils](https://github.com/andrewgregory/pacutils)                                               | Helper tools for libalpm                                                                                       |
| [patch](https://www.gnu.org/software/patch/)                                                        | A utility to apply patch files to original sources                                                             |
| [pdfarranger](https://github.com/pdfarranger/pdfarranger)                                           | Helps merge or split PDF documents and rotate, crop and rearrange pages                                        |
| [perl-file-mimeinfo](https://metacpan.org/release/File-MimeInfo)                                    | Determine file type, includes mimeopen and mimetype                                                            |
| [pipewire-alsa](https://pipewire.org)                                                               | Low-latency audio/video router and processor - ALSA configuration                                              |
| [pipewire-pulse](https://pipewire.org)                                                              | Low-latency audio/video router and processor - PulseAudio replacement                                          |
| [pkgconf](https://github.com/pkgconf/pkgconf)                                                       | Package compiler and linker metadata toolkit                                                                   |
| [podman](https://github.com/containers/podman)                                                      | Tool and library for running OCI-based containers in pods                                                      |
| [procs](https://github.com/dalance/procs)                                                           | A modern replacement for ps written in Rust                                                                    |
| [progress](https://github.com/Xfennec/progress)                                                     | Shows running coreutils basic commands and displays stats                                                      |
| [ps_mem](https://github.com/pixelb/ps_mem)                                                          | List processes by memory usage                                                                                 |
| [pueue](https://github.com/nukesor/pueue)                                                           | A CLI tool for managing long running shell commands                                                            |
| [python-black](https://github.com/psf/black)                                                        | Uncompromising Python code formatter                                                                           |
| [python-pynvim](https://github.com/neovim/pynvim)                                                   | Python client for Neovim                                                                                       |
| [refind](https://www.rodsbooks.com/refind/)                                                         | An EFI boot manager                                                                                            |
| [reflector](https://xyne.dev/projects/reflector)                                                    | A Python 3 module and script to retrieve and filter the latest Pacman mirror list.                             |
| [ripgrep-all](https://github.com/phiresky/ripgrep-all)                                              | rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc.                            |
| [sad](https://github.com/ms-jpq/sad)                                                                | Space Age seD                                                                                                  |
| [scrcpy](https://github.com/Genymobile/scrcpy)                                                      | Display and control your Android device                                                                        |
| [sd](https://github.com/chmln/sd)                                                                   | Intuitive find &amp; replace                                                                                   |
| [shellcheck](https://www.shellcheck.net)                                                            | Shell script analysis tool                                                                                     |
| [shellharden](https://github.com/anordal/shellharden)                                               | Bash linter and syntax highlighter                                                                             |
| [slurp](https://github.com/emersion/slurp)                                                          | Select a region in a Wayland compositor                                                                        |
| [ssh-audit](https://github.com/jtesta/ssh-audit)                                                    | SSH server and client configuration auditing                                                                   |
| [sshfs](https://github.com/libfuse/sshfs)                                                           | FUSE client based on the SSH File Transfer Protocol                                                            |
| [starship](https://starship.rs/)                                                                    | The cross-shell prompt for astronauts                                                                          |
| [streamlink](https://streamlink.github.io/)                                                         | CLI program that launches streams from various streaming services in a custom video player (livestreamer fork) |
| [sudo](https://www.sudo.ws/sudo/)                                                                   | Give certain users the ability to run some commands as root                                                    |
| [swappy](https://github.com/jtheoof/swappy)                                                         | A Wayland native snapshot editing tool                                                                         |
| [sway](https://swaywm.org/)                                                                         | Tiling Wayland compositor and replacement for the i3 window manager                                            |
| [swayidle](https://github.com/swaywm/swayidle)                                                      | Idle management daemon for Wayland                                                                             |
| [swaylock](https://github.com/swaywm/swaylock)                                                      | Screen locker for Wayland                                                                                      |
| [syncthing](https://syncthing.net/)                                                                 | Open Source Continuous Replication / Cluster Synchronization Thing                                             |
| [tectonic](https://tectonic-typesetting.github.io/)                                                 | Modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive                            |
| [telegram-desktop](https://desktop.telegram.org/)                                                   | Official Telegram Desktop client                                                                               |
| [termshark](https://github.com/gcla/termshark)                                                      | Terminal UI for tshark, inspired by Wireshark                                                                  |
| [texinfo](https://www.gnu.org/software/texinfo/)                                                    | GNU documentation system for on-line information and printed output                                            |
| [texlive-latexextra](http://tug.org/texlive/)                                                       | TeX Live - Large collection of add-on packages for LaTeX                                                       |
| [tmux](https://github.com/tmux/tmux/wiki)                                                           | Terminal multiplexer                                                                                           |
| [tokei](https://github.com/XAMPPRocky/tokei)                                                        | A blazingly fast CLOC (Count Lines Of Code) program                                                            |
| [trash-cli](https://github.com/andreafrancia/trash-cli)                                             | Command line trashcan (recycle bin) interface                                                                  |
| [tree](https://gitlab.com/OldManProgrammer/unix-tree)                                               | A directory listing program displaying a depth indented list of files                                          |
| [ttf-firacode-nerd](https://github.com/ryanoasis/nerd-fonts)                                        | Patched font Fira (Fura) Code from nerd fonts library                                                          |
| [ttf-jetbrains-mono-nerd](https://github.com/ryanoasis/nerd-fonts)                                  | Patched font JetBrains Mono from nerd fonts library                                                            |
| [up](https://github.com/akavel/up)                                                                  | A tool for writing Linux pipes with instant live preview                                                       |
| [vagrant](https://vagrantup.com)                                                                    | Build and distribute virtualized development environments                                                      |
| [vi](https://ex-vi.sourceforge.net/)                                                                | The original ex/vi text editor                                                                                 |
| [virtualbox](https://virtualbox.org/)                                                               | Powerful x86 virtualization for enterprise as well as home use                                                 |
| [visidata](https://www.visidata.org)                                                                | Terminal spreadsheet multitool for discovering and arranging data                                              |
| [wavemon](https://github.com/uoaerg/wavemon)                                                        | Ncurses-based monitoring application for wireless network devices                                              |
| [waybar](https://github.com/Alexays/Waybar/)                                                        | Highly customizable Wayland bar for Sway and Wlroots based compositors                                         |
| [webhook](https://github.com/adnanh/webhook)                                                        | A lightweight incoming webhook server to run shell commands                                                    |
| [websocat](https://github.com/vi/websocat/)                                                         | Command-line client for web sockets, like netcat/curl/socat for ws://                                          |
| [which](https://savannah.gnu.org/projects/which/)                                                   | A utility to show the full path of commands                                                                    |
| [wireshark-qt](https://www.wireshark.org/)                                                          | Network traffic and protocol analyzer/sniffer - Qt GUI                                                         |
| [xorg-xwayland](https://xorg.freedesktop.org)                                                       | run X clients under wayland                                                                                    |
| [yadm](https://github.com/TheLocehiliosan/yadm)                                                     | Yet Another Dotfiles Manager                                                                                   |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp)                                                          | A youtube-dl fork with additional features and fixes                                                           |
| [zathura-pdf-mupdf](https://pwmt.org/projects/zathura-pdf-mupdf/)                                   | PDF support for Zathura (MuPDF backend) (Supports PDF, ePub, and OpenXPS)                                      |
| [zoxide](https://github.com/ajeetdsouza/zoxide)                                                     | A smarter cd command for your terminal                                                                         |

</div>

<div class="outline-2nil">

### Arch AUR Packages {#arch-aur-packages}

| Name                                                                                               | Description                                                                                                          |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [act](https://github.com/nektos/act)                                                               | Run your GitHub Actions locally                                                                                      |
| [advcpmv](https://github.com/jarun/advcpmv)                                                        | 'cp' and 'mv' utilities with progress bar patches                                                                    |
| [ancient-packages](http://public.files.xavion.name/Software/ancient-packages/ancient-packages.jpg) | Lists installed packages no longer available (anywhere)                                                              |
| [anki](https://apps.ankiweb.net/)                                                                  | Helps you remember facts (like words/phrases in a foreign language) efficiently                                      |
| [asdf-vm](https://asdf-vm.com)                                                                     | Extendable version manager with support for Ruby, Node.js, Elixir, Erlang &amp; more                                 |
| [buku](https://github.com/jarun/buku)                                                              | Bookmark manager like a text-based mini-web                                                                          |
| [cbonsai](https://gitlab.com/jallbrit/cbonsai)                                                     | A bonsai tree generator, written in C using ncurses                                                                  |
| [chars](https://github.com/antifuchs/chars)                                                        | Command line tool to display information about unicode characters.                                                   |
| [cheat](https://github.com/cheat/cheat)                                                            | Allows you to create and view interactive cheatsheets on the command-line                                            |
| [choose-rust-git](https://github.com/theryangeary/choose)                                          | A fast, human-friendly alternative to awk(1) and cut(1)                                                              |
| [clipman](https://github.com/yory8/clipman)                                                        | A simple clipboard manager for Wayland                                                                               |
| [code-minimap](https://github.com/wfxr/code-minimap)                                               | A high performance code minimap render                                                                               |
| [cpufetch](https://github.com/Dr-Noob/cpufetch)                                                    | Simple yet fancy CPU architecture fetching tool                                                                      |
| [dasel](https://github.com/TomWright/dasel)                                                        | Query and update data structures from the command line.                                                              |
| [desed](https://github.com/soptikha2/desed)                                                        | Debugger for sed, written in rust. Step through code and observe sed inner state.                                    |
| [elfcat](https://github.com/ruslashev/elfcat)                                                      | Generates HTML files from ELF binaries                                                                               |
| [fclones](https://github.com/pkolaczk/fclones)                                                     | Efficient Duplicate File Finder                                                                                      |
| [firefox-tridactyl-native](https://github.com/tridactyl/tridactyl)                                 | Tridactyl native messaging host application for Firefox (native: 0.3.6)                                              |
| [frangipanni](https://github.com/birchb1024/frangipanni)                                           | Program to convert lines of text into a tree structure                                                               |
| [gallery-dl](https://github.com/mikf/gallery-dl)                                                   | Command-line program to download image-galleries and collections from several image hosting sites                    |
| [gomi](https://github.com/b4b4r07/gomi)                                                            | Rm alternative written in Go                                                                                         |
| [google-chrome](https://www.google.com/chrome)                                                     | The popular and trusted web browser by Google (Stable Channel)                                                       |
| [graphtage](https://github.com/trailofbits/graphtage)                                              | A utility for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, and CSS files. |
| [hostctl](https://github.com/guumaster/hostctl)                                                    | Command-line tool to manage your hosts file                                                                          |
| [hr-bash](https://github.com/LuRsT/hr)                                                             | A horizontal ruler for your terminal                                                                                 |
| [ijq](https://git.sr.ht/~gpanders/ijq)                                                             | Interactive jq tool, like jqplay for the commandline                                                                 |
| [imgp](https://github.com/jarun/imgp)                                                              | Multi-core batch image resizer and rotator                                                                           |
| [libtree](https://github.com/haampie/libtree)                                                      | ldd as a tree                                                                                                        |
| [nnn-nerd](https://github.com/jarun/nnn)                                                           | The fastest terminal file manager ever written (with icon support using a patched nerd font).                        |
| [paru](https://github.com/morganamilo/paru)                                                        | Feature packed AUR helper                                                                                            |
| [passage-git](https://github.com/FiloSottile/passage)                                              | A fork of password-store that uses age as backend.                                                                   |
| [pmount](http://pmount.alioth.debian.org/)                                                         | mount removable devices as normal user                                                                               |
| [podman-tui](https://github.com/containers/podman-tui)                                             | Podman Terminal User Interface                                                                                       |
| [procdump](https://github.com/Sysinternals/ProcDump-for-Linux)                                     | Generate coredumps based off performance triggers                                                                    |
| [programmer-calculator](https://github.com/alt-romes/programmer-calculator)                        | A command line calculator made for programmers working with multiple number representations and close to the bits    |
| [quickemu](https://github.com/quickemu-project/quickemu)                                           | Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.                                  |
| [sampler](https://sampler.dev)                                                                     | A tool for shell commands execution, visualization and alerting. Configured with a simple YAML file.                 |
| [sfz](https://github.com/weihanglo/sfz)                                                            | A simple static file server                                                                                          |
| [sshping](https://github.com/spook/sshping)                                                        | ssh-based ping: measure character-echo latency and bandwidth for an interactive ssh session                          |
| [sysz](https://github.com/joehillen/sysz)                                                          | fzf terminal UI for systemctl                                                                                        |
| [teip](https://github.com/greymd/teip)                                                             | Highly efficient "Masking tape" for standard input                                                                   |
| [thelounge](https://thelounge.chat/)                                                               | Modern self-hosted web IRC client                                                                                    |
| [tsukae-git](https://github.com/irevenko/tsukae)                                                   | Show off your most used shell commands                                                                               |
| [ttf-twemoji](https://github.com/twitter/twemoji)                                                  | Twitter Color Emoji for everyone.                                                                                    |
| [typiskt](https://github.com/budlabs/typiskt)                                                      | touchtype training in the terminal                                                                                   |
| [tz](https://github.com/oz/tz)                                                                     | A time zone helper                                                                                                   |
| [wev](https://git.sr.ht/~sircmpwn/wev)                                                             | tool for debugging wayland events, similar to xev                                                                    |
| [wlay-git](https://github.com/atx/wlay)                                                            | Graphical output management for Wayland                                                                              |
| [wlsunset](https://sr.ht/~kennylevinsen/wlsunset)                                                  | Day/night gamma adjustments for Wayland compositors                                                                  |
| [wofi-emoji-git](https://github.com/dln/wofi-emoji)                                                | Emoji picker for Wayland using wofi and wtype                                                                        |
| [xdg-ninja-git](https://github.com/b3nj5m1n/xdg-ninja)                                             | A shell script which checks your $HOME for unwanted files and directories.                                           |
| [zotero-beta](https://www.zotero.org/support/dev_builds)                                           | Zotero is a free, easy-to-use tool to help you collect, organize, cite, and share research.                          |

</div>

<div class="outline-2nil">

### Mobile Apps {#mobile-apps}

Absolute dump. I use the [List My Apps](https://f-droid.org/packages/de.onyxbits.listmyapps/) app to generate the csv, the csv is then uploaded to dropbox from where airtable pulls it. When generating the org file my custom script fetches from airtable. I did not want this to be a rube goldberg machine but there doesn't seem to be a very clean way out in the way I need it at the moment.

[Notion](https://play.google.com/store/apps/details?id=notion.id) ○ [Adobe Acrobat](https://play.google.com/store/apps/details?id=com.adobe.reader) ○ [Habits](https://play.google.com/store/apps/details?id=org.isoron.uhabits) ○ [GuitarTuna](https://play.google.com/store/apps/details?id=com.ovelin.guitartuna) ○ [Adobe Scan](https://play.google.com/store/apps/details?id=com.adobe.scan.android) ○ [Zomato](https://play.google.com/store/apps/details?id=com.application.zomato) ○ [Embiggen](https://play.google.com/store/apps/details?id=com.briercan.embiggen) ○ [Snapseed](https://play.google.com/store/apps/details?id=com.niksoftware.snapseed) ○ [List My Apps](https://f-droid.org/repository/browse/?fdid=de.onyxbits.listmyapps) ○ [1.1.1.1](https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone) ○ [Ping Test Tool](https://play.google.com/store/apps/details?id=com.jjo.pingtest) ○ [F-Droid](https://www.google.com/search?q=org.fdroid.fdroid) ○ [PlantNet](https://play.google.com/store/apps/details?id=org.plantnet) ○ [Paytm](https://play.google.com/store/apps/details?id=net.one97.paytm) ○ [Quit Smoking](https://f-droid.org/repository/browse/?fdid=de.baumann.quitsmoking) ○ [Binary](https://play.google.com/store/apps/details?id=com.tomhogenkamp.binaircalculator) ○ [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) ○ [Forest](https://play.google.com/store/apps/details?id=cc.forestapp) ○ [Planta](https://play.google.com/store/apps/details?id=com.stromming.planta) ○ [Kite](https://play.google.com/store/apps/details?id=com.zerodha.kite3) ○ [Wolfram Alpha](https://play.google.com/store/apps/details?id=com.wolfram.android.alpha) ○ [Uber](https://play.google.com/store/apps/details?id=com.ubercab) ○ [Keep Notes](https://play.google.com/store/apps/details?id=com.google.android.keep) ○ [WhatsApp](https://play.google.com/store/apps/details?id=com.whatsapp) ○ [Awesome QR](https://play.google.com/store/apps/details?id=com.github.sumimakito.awesomeqrsample) ○ [Track](https://play.google.com/store/apps/details?id=com.nutritionix.nixtrack) ○ [Replit](https://play.google.com/store/apps/details?id=com.replit.app) ○ [Google Podcasts](https://play.google.com/store/apps/details?id=com.google.android.apps.podcasts) ○ [CRED](https://play.google.com/store/apps/details?id=com.dreamplug.androidapp) ○ [Protractor](https://play.google.com/store/apps/details?id=com.keuwl.protractor) ○ [Pocket](https://play.google.com/store/apps/details?id=com.ideashower.readitlater.pro) ○ [Grapevine](https://play.google.com/store/apps/details?id=com.app.gvine) ○ [Bluecoins](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) ○ [Url forwarder](https://play.google.com/store/apps/details?id=net.daverix.urlforward) ○ [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) ○ [Crayon](https://play.google.com/store/apps/details?id=com.jndapp.cartoon.crayon.iconpack) ○ [SoundCloud](https://play.google.com/store/apps/details?id=com.soundcloud.android) ○ [Track &amp; Graph](https://f-droid.org/repository/browse/?fdid=com.samco.trackandgraph) ○ [Unit Converter Ultimate](https://f-droid.org/repository/browse/?fdid=com.physphil.android.unitconverterultimate) ○ [Pinterest](https://play.google.com/store/apps/details?id=com.pinterest) ○ [GitHub](https://play.google.com/store/apps/details?id=com.github.android) ○ [VLC](https://play.google.com/store/apps/details?id=org.videolan.vlc) ○ [Telegram](https://play.google.com/store/apps/details?id=org.telegram.messenger) ○ [Airtable](https://play.google.com/store/apps/details?id=com.formagrid.airtable) ○ [Niagara Launcher](https://play.google.com/store/apps/details?id=bitpit.launcher) ○ [BHIM](https://play.google.com/store/apps/details?id=in.org.npci.upiapp) ○ [Shazam](https://play.google.com/store/apps/details?id=com.shazam.android) ○ [Drinkable](https://f-droid.org/repository/browse/?fdid=com.moimob.drinkable) ○ [Goodreads](https://play.google.com/store/apps/details?id=com.goodreads) ○ [Wikipedia](https://play.google.com/store/apps/details?id=org.wikipedia) ○ [Termux](https://f-droid.org/repository/browse/?fdid=com.termux) ○ [Discord](https://play.google.com/store/apps/details?id=com.discord) ○ [Signal](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) ○ [Product Hunt](https://play.google.com/store/apps/details?id=com.producthuntmobile) ○ [Coin](https://play.google.com/store/apps/details?id=com.zerodha.coin) ○ [SimpleLogin](https://play.google.com/store/apps/details?id=io.simplelogin.android) ○ [Syncthing](https://play.google.com/store/apps/details?id=com.nutomic.syncthingandroid) ○ [Tapo](https://play.google.com/store/apps/details?id=com.tplink.iot) ○ [Lithium](https://play.google.com/store/apps/details?id=com.faultexception.reader) ○ [Snipd](https://play.google.com/store/apps/details?id=ai.topicfinder.podcastdiscovery) ○ [Brave](https://play.google.com/store/apps/details?id=com.brave.browser) ○ [NetGuard](https://play.google.com/store/apps/details?id=eu.faircode.netguard) ○ [PhonePe](https://play.google.com/store/apps/details?id=com.phonepe.app) ○ [HTTP Shortcuts](https://play.google.com/store/apps/details?id=ch.rmy.android.http_shortcuts) ○ [BigO](https://play.google.com/store/apps/details?id=hieunguyen725.bigo) ○ [Splitwise](https://play.google.com/store/apps/details?id=com.Splitwise.SplitwiseMobile) ○ [Relay Pro](https://play.google.com/store/apps/details?id=reddit.news) ○ [Zoom](https://play.google.com/store/apps/details?id=us.zoom.videomeetings) ○ [Binance](https://play.google.com/store/apps/details?id=com.binance.dev) ○ [Just Another Workout Timer](https://f-droid.org/repository/browse/?fdid=com.blockbasti.justanotherworkouttimer) ○ [Chess](https://play.google.com/store/apps/details?id=com.chess) ○ [WiFiAnalyzer](https://f-droid.org/repository/browse/?fdid=com.vrem.wifianalyzer) ○ [Tasks](https://play.google.com/store/apps/details?id=com.google.android.apps.tasks) ○ [Rapido](https://play.google.com/store/apps/details?id=com.rapido.passenger) ○ [DiskUsage](https://play.google.com/store/apps/details?id=com.google.android.diskusage) ○ [TrebleShot](https://play.google.com/store/apps/details?id=com.genonbeta.TrebleShot) ○ [Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)

</div>

</div>
