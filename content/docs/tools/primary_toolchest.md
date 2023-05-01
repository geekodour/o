+++
title = "Primary tool-chest"
author = ["Hrishikesh Barman"]
draft = false
+++

My dotfiles are currently private, but they contain [my fish functions](https://github.com/geekodour/x/tree/main/.config/fish/functions)(aliases), [my yasnippets](https://github.com/geekodour/x/tree/main/.config/doom/snippets) and [cheats](https://cheats.geekodour.org/)

<div class="outline-1 smol-table">

## General development {#general-development}

{{< lft >}}
-   Online sandboxes: [CodeSandbox](https://codesandbox.io/s/), [StackBlitz](https://stackblitz.com/), [Replit](https://replit.com/), [Glitch](https://glitch.com/)
-   [Using AI tools](https://lobste.rs/s/dfmiko/using_github_copilot_for_unit_testing) for [development](https://lobste.rs/s/iualxr/ai_enhanced_development_makes_me_more).
-   Checking how [test containers](https://golang.testcontainers.org/) and [dev containers](https://containers.dev/) compare to my LXD workflow
-   Re-start OSS contributions, start maintaining some projects [and packages](https://github.com/jubalh/awesome-package-maintainer) of interest.
-   I am planning to write some aliases and function wrapper around ffmpeg and imagemagick for regular stuff. Most probably there are good tools out there, have to check.
{{< /lft >}}

{{< coolinks >}}
-   Debugging: [godbolt](https://godbolt.org/) | [CyberChef](https://gchq.github.io/CyberChef/) | [explainshell](https://explainshell.com/)
-   Info: [CPU info](https://www.cpu-world.com) | [GPU info](https://www.techpowerup.com/gpu-specs/)
-   Reference: [hyperpolyglot](/backupsites/hyperpolyglot.org/) | [coreutils](https://wiki.archlinux.org/title/core_utilities) | [ManKier](https://www.mankier.com/) | [Sysctl Explorer](https://sysctl-explorer.net/) | [procps-ng](https://gitlab.com/procps-ng/procps)
-   Conversion: [onlinelisttools](https://onlinelisttools.com/) | [Squoosh](https://squoosh.app/) | [transform.tools](https://transform.tools/)
{{< /coolinks >}}

Now how I do development has varied over the years. But I am constantly updating it. This section is a scratchpad area for links/notes about current or probable future workflow.

<div class="outline-2 smol-table">

### Editing text {#editing-text}

-   95% doom emacs(heavily customized), 5% neovim
-   I think I spent half of my year last year fighting with emacs, had me learn little bit of elisp and I am not sure if it was worth it, but if there's one thing I cannot live without, it has to be `org-mode`. helluvadrug.
-   For documentation lookup inside emacs, `eldoc` (using `elglot`), `M-x man`, `dev-docs` custom bindings for `eww`.
-   When I quickly need to check the contents of a repo, I use [GitHub1s](https://github1s.com/), pretty neat stuff.

</div>

<div class="outline-2 smol-table">

### Interface and dependencies {#interface-and-dependencies}

-   `fish` is my shell, have a love hate relationship ngl.
-   `pacman` and `paru` mostly have me covered
-   For different versions of stuff, I use `asdf` + `direnv`. I really like the global, local flexibility that `asdf` gives.
-   For virtual environments, I use `LXD` system containers with a custom cloud-init script. It's pretty neat. Thanks to the co-workers at my last workplace! (See my [notes on lxd](https://mogoz.geekodour.org/search/?query=lxd))

</div>

</div>

<div class="outline-1 smol-table">

## Domain specific {#domain-specific}

<div class="outline-2 smol-table">

### Web {#web}

{{< lft >}}
-   Experimenting w websockets, WebRTC, WebAssembly, webworkers other web engineering fun.
-   Experimenting w serverless functions (Mostly cf workers)
-   Really grokking HTTP, Headers, Cache, Cookies and Sessions
-   Getting better at Typescript
-   Experiment w [htmx](https://news.ycombinator.com/item?id=33218439), alpine.js(more) and [svelte](https://svelte.dev/)(not so much).
-   Also want to try out [Elixir, Phoenix and LiveView.](https://thinkingelixir.com/petal-stack-in-elixir/)
-   Explore more in web security side of things
{{< /lft >}}

{{< coolinks >}}
-   Info: [caniuse](https://caniuse.com/)
-   CSS &amp; Animations: [Almanac](https://css-tricks.com/almanac/) | [Animista](https://animista.net/play/basic/scale-up) | [SVG Artista](https://svgartista.net/)
{{< /coolinks >}}

-   Everything I learn here becomes obsolete in about six months
-   But I like the web and I want to build on it too
-   I am too bad at anything involving CSS so, tailwindcss is my best friend here.
-   I once tried doing react+vite+storybook with all the right config and other stuff, later I felt that I don't want to be worrying about a static site so much. So static sites or semi-static sites are basically an org-mode export or a next.js site for me now.
-   I think I learned react about 3 times and everytime, the documentation gets overhauled(good thing). But the last time I learned react, I [took notes](https://mogoz.geekodour.org/search/?query=react).
-   Don't ask me about framework preferences. I don't think I agree with myself here.

</div>

<div class="outline-2 smol-table">

### Python {#python}

-   I use asdf + poetry for all my python virtual env setups. Even if it's a project with a `requirements.txt`, I use poetry to create a venv there and pip install on it. I don't think i'll ever understand python virtual environments completely so I am going for the path of least resistance
-   Understanding python's [import system](https://mogoz.geekodour.org/posts/20221231140207-python/#imports) has done me wonders
-   `pudb` with `ipython` is pretty neat for debugging
-   I don't have any linting, formatter preference honestly I just use the defaults that work with my editor setup. If any project needs specific style, the CI/CD system should catch it.
-   Once [joblib](https://joblib.readthedocs.io/en/latest/index.html#) was very useful to me but I can't exactly remember when

</div>

</div>

<div class="outline-1 smol-table">

## Data {#data}

<div class="outline-2 smol-table">

### Database {#database}

{{< lft >}}
-   Experimenting more with: SQLite (and ecosystem), Postgres (and ecosystem), Clickhouse, DuckDB, Redis
-   Go through the excellent MySQL intermediate series by PlanetScale
{{< /lft >}}

-   I don't play with DBs on the daily but plan to.

</div>

<div class="outline-2 smol-table">

### Data Engineering {#data-engineering}

{{< lft >}}
-   Checking [centerofci/mathesar](https://github.com/centerofci/mathesar)
{{< /lft >}}

</div>

<div class="outline-2 smol-table">

### Data Analysis/Viz {#data-analysis-viz}

{{< lft >}}
-   Including [Desmos](https://www.desmos.com/) and [ObservableHQ](https://observablehq.com/) in my workflow
-   Use more of [Datasette](https://datasette.io/)
-   [Getting](https://stackoverflow.com/questions/2054364/firefox-how-do-i-list-installed-extensions-and-identify-them-in-a-list) [better](https://lzone.de/cheat-sheet/jq) w [jq](https://unix.stackexchange.com/questions/312697/merge-jq-output-into-a-comma-separated-string)
{{< /lft >}}

-   Airtable has been a good friend, I'll soon go for a selfhosted solution due to limitations in the free tire.

</div>

</div>

<div class="outline-1 smol-table">

## Infra &amp; Security {#infra-and-security}

<div class="outline-2 smol-table">

### Hosting stuff {#hosting-stuff}

-   Mostly use github and bitbucket for hosting code repositories
-   Netlify or Vercel for semi-static sites
-   Have not got around selfhosting stuff yet, except locally on my pi/laptop when it makes sense.

</div>

<div class="outline-2 smol-table">

### Infrastructure Management {#infrastructure-management}

{{< lft >}}
-   Try out [scrcpy](https://news.ycombinator.com/item?id=35749366), [sipcalc](https://news.ycombinator.com/item?id=35749594)
-   Check out [assh](https://github.com/moul/assh) for managing ssh stuff
-   Experiment w [ghidra](https://ghidra-sre.org/), see [notes](https://mogoz.geekodour.org/posts/20230418153328-reverse_engineering/)
-   Check [cilium/pwru](https://github.com/cilium/pwru) looks pretty cool
{{< /lft >}}

-   Ansible and Github actions are enough for my regular automation
-   I haven't fiddled with infra stuff in a while but it's always a combination of so many things. Shell scripts, custom programs, infra tools, external tools and so on. I plan to streamline this process eventually.

</div>

<div class="outline-2 smol-table">

### Troubleshooting {#troubleshooting}

-   I have a dedicated page called [Plumber Manual]({{< relref "plumber_manual#general" >}}) for this.

</div>

</div>

<div class="outline-1 smol-table">

## Non-tech {#non-tech}

<div class="outline-2 smol-table">

### Planning/Brainstorming/Curation {#planning-brainstorming-curation}

{{< lft >}}
-   I've been planning to setup a [nice zotero &amp; org-ref workflow](https://www.reddit.com/r/emacs/comments/vt0otx/using_the_power_of_zotero_in_emacs_orgmode_to/) but I am not an academic and I am not exactly sure how things will play out.
{{< /lft >}}

-   `org-mode` supremacy, notion and various markdown wiki veteran.
-   I have a page dedicated to [notetaking]({{< relref "notetaking" >}})
-   Github issues and Linear for project progress tracking.
-   Key is to think how to think about the specific problem and choose tools based on that. Meta.

</div>

<div class="outline-2 smol-table">

### Communication and Discussions {#communication-and-discussions}

-   I have a [communities]({{< relref "communities" >}}) page but I have serious [problems](http://www.catb.org/esr/faqs/smart-questions.html) communicating my thoughts, but that's another story.
-   Chat
    -   Matrix: Element as the backend, cinny as the chat ui
    -   IRC: [The Lounge](https://thelounge.chat/) runs locally on my pi
    -   Telegram, WhatsApp, Signal, Discord
-   Email
    -   Gmail, Zoho Mail (K9, Delta Chat) w [SimpleLogin](https://simplelogin.io/)

</div>

</div>

<div class="outline-1 smol-table">

## Misc {#misc}

<div class="outline-2 smol-table">

### Art/Design {#art-design}

{{< lft >}}
-   Experiment more with MagicaVoxel
{{< /lft >}}

I wants to do art/design but not at the moment. I also wanted to make weird game videos using assets etc (Neel, if you ever read this, yeah still at it). But I might have to pause that for a while as it does not directly feed into my primary goals but I definitely want to make time for it.

</div>

<div class="outline-2 smol-table">

### AI/ML experiments {#ai-ml-experiments}

{{< lft >}}
-   [Huggingface](https://huggingface.co/)
-   [jerryjliu/gpt_index](https://github.com/jerryjliu/gpt_index), [hwchase17/langchain](https://github.com/hwchase17/langchain), [gpt4all](https://news.ycombinator.com/item?id=35349608), [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui)
-   whisper.cpp, llma.cpp et al, [Web LLM](https://lobste.rs/s/prfiun/web_llm_runs_vicuna_7b_large_language) looks pretty sick.
{{< /lft >}}

-   When SD came out, played a lot with [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

</div>

</div>

<div class="outline-1 smol-table">

## Generated {#generated}

<div class="book-hint info">

> These following lists are generated [here](https://github.com/geekodour/systemfiles/) and not in sync with my system at all times.
</div>

<div class="outline-2 smol-table">

### Firefox Extensions {#firefox-extensions}

| Name                                                                                                                                                               | Description                                                                                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Tab Stash](https://addons.mozilla.org/en-US/firefox/addon/tab-stash/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=homepage-primary-hero)         | A no-fuss way to save and restore batches of tabs as bookmarks.                                                                                                                                                      |
| [Sidebery](https://addons.mozilla.org/en-US/firefox/addon/sidebery/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                        | Addon for managing tabs, containers (contextual identities) and bookmarks in sidebar. Supports both flat and tree tabs layouts, per-container include/exclude rules, proxy configs for each container and much more. |
| [Auto Tab Discard](https://addons.mozilla.org/en-US/firefox/addon/auto-tab-discard/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)        | Increase browser speed and reduce memory load when you have numerous open tabs.                                                                                                                                      |
| [Impulse Blocker](https://addons.mozilla.org/en-US/firefox/addon/impulse-blocker/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)          | Block distracting websites when you are browsing the web.                                                                                                                                                            |
| [Imagus](https://addons.mozilla.org/en-US/firefox/addon/imagus/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                            | Enlarge thumbnails, and show images/videos from links with a mouse hover.                                                                                                                                            |
| [Dark Reader](https://addons.mozilla.org/en-US/firefox/addon/darkreader/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                   | Dark mode for every website. Take care of your eyes, use dark theme for night and daily browsing.                                                                                                                    |
| [Cookie Quick Manager](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/)                                                                       | An addon to manage (view, search, create, edit, delete, backup, restore) cookies.                                                                                                                                    |
| [What Hacker News Says](https://addons.mozilla.org/en-US/firefox/addon/what-hacker-news-says/)                                                                     | Easily find Hacker News threads about the page you're currently browsing.                                                                                                                                            |
| [WhatFont](https://addons.mozilla.org/en-US/firefox/addon/zjm-whatfont/)                                                                                           | A wrapper for Chengyhin Liu's WhatFont tool                                                                                                                                                                          |
| [uMatrix](https://addons.mozilla.org/en-US/firefox/addon/umatrix/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)                            | Point &amp; click to forbid/allow any class of requests made by your browser. Use it to block scripts, iframes, ads, facebook, etc.                                                                                  |
| [Debug CSS](https://addons.mozilla.org/en-US/firefox/addon/pranay-joshi/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)                     | Adds outline to all elements on the page to show the culprit element which is changing desired layout                                                                                                                |
| [React Developer Tools](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)       | Adds React debugging tools to the Firefox Developer Tools.Created from revision 47f63dc54 on 12/6/2022.                                                                                                              |
| [Reddit Enhancement Suite](https://addons.mozilla.org/en-US/firefox/addon/reddit-enhancement-suite/)                                                               | A suite of modules that enhance your Reddit browsing experience                                                                                                                                                      |
| [Video Speed Controller](https://addons.mozilla.org/en-US/firefox/addon/videospeed/)                                                                               | Speed up, slow down, advance and rewind HTML5 audio/video with shortcuts                                                                                                                                             |
| [Tridactyl](https://addons.mozilla.org/en-US/firefox/addon/tridactyl-vim/)                                                                                         | &lt;nil&gt;                                                                                                                                                                                                          |
| [Stylus](https://addons.mozilla.org/en-US/firefox/addon/styl-us/)                                                                                                  | Redesign the web with Stylus, a user styles manager. Stylus allows you to easily install themes and skins for many popular sites.                                                                                    |
| [ClearURLs](https://addons.mozilla.org/en-US/firefox/addon/clearurls/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                      | Remove tracking elements from URLs.                                                                                                                                                                                  |
| [Hello, Goodbye](https://addons.mozilla.org/en-US/firefox/addon/hello-goodbye/)                                                                                    | Hello, Goodbye blocks annoying chat widgets.                                                                                                                                                                         |
| [Flagfox](https://addons.mozilla.org/en-US/firefox/addon/flagfox/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                          | Displays a flag depicting the location of the current server                                                                                                                                                         |
| [I don't care about cookies](https://addons.mozilla.org/en-US/firefox/addon/i-dont-care-about-cookies/)                                                            | &lt;nil&gt;                                                                                                                                                                                                          |
| [Library Extension](https://addons.mozilla.org/en-US/firefox/addon/libraryextension/)                                                                              | &lt;nil&gt;                                                                                                                                                                                                          |
| [Zotero Connector](https://www.zotero.org/download/connectors)                                                                                                     | Save references to Zotero from your web browser                                                                                                                                                                      |
| [Web Archives](https://addons.mozilla.org/en-US/firefox/addon/view-page-archive/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)           | View archived and cached versions of web pages on 10+ search engines, such as the Wayback Machine, Archive․is, Google, Bing and Yandex                                                                               |
| [SingleFile](https://addons.mozilla.org/en-US/firefox/addon/single-file/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                   | Save a complete page into a single HTML file                                                                                                                                                                         |
| [Control Panel for Twitter](https://addons.mozilla.org/en-US/firefox/addon/tweak-new-twitter/)                                                                     | Gives you more control over Twitter and adds missing features and UI improvements                                                                                                                                    |
| [Bitwarden - Free Password Manager](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/)                                                    | A secure and free password manager for all of your devices.                                                                                                                                                          |
| [Refined GitHub](https://addons.mozilla.org/en-US/firefox/addon/refined-github-/)                                                                                  | Simplifies the GitHub interface and adds useful features                                                                                                                                                             |
| [SponsorBlock for YouTube - Skip Sponsorships](https://addons.mozilla.org/en-US/firefox/addon/sponsorblock/)                                                       | Skip sponsorships, subscription begging and more on YouTube videos. Report sponsors on videos you watch to save others' time.                                                                                        |
| [uBlacklist](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/)                                                                                           | Blocks sites you specify from appearing in Google search results                                                                                                                                                     |
| [Emoji](https://addons.mozilla.org/en-US/firefox/addon/emoji-sav/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                          | Insert emojis using a web browser, and customise the experience and the add-on in Settings.                                                                                                                          |
| [LocalCDN](https://addons.mozilla.org/en-US/firefox/addon/localcdn-fork-of-decentraleyes/)                                                                         | Protects you against tracking through CDNs (Content Delivery Networks) by redirecting to local resources.                                                                                                            |
| [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)                                                                                     | Finally, an efficient blocker. Easy on CPU and memory.                                                                                                                                                               |
| [Enhancer for YouTube™](https://addons.mozilla.org/en-US/firefox/addon/enhancer-for-youtube/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) | Take control of YouTube and boost your user experience!                                                                                                                                                              |
| [SimpleLogin:Receive &amp; Send emails anonymously](https://addons.mozilla.org/en-US/firefox/addon/simplelogin/)                                                   | Easily create a different email for each website to hide your real email. Protect your inbox against spams, phishing, data breaches                                                                                  |
| [Consent-O-Matic](https://addons.mozilla.org/en-US/firefox/addon/consent-o-matic/)                                                                                 | Automatic handling of GDPR consent forms                                                                                                                                                                             |
| [Violentmonkey](https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/)                                                                                     | An open source userscript manager that supports a lot of browsers                                                                                                                                                    |
| [MarkDownload - Markdown Web Clipper](https://addons.mozilla.org/en-US/firefox/addon/markdownload/)                                                                | This extension works like a web clipper, but it downloads articles in markdown format.                                                                                                                               |

</div>

<div class="outline-2 smol-table">

### Arch Official Packages {#arch-official-packages}

| Name                                                                                                | Description                                                                                                    |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [adobe-source-han-sans-jp-fonts](https://github.com/adobe-fonts/source-han-sans)                    | Adobe Source Han Sans Subset OTF - Japanese OpenType/CFF fonts                                                 |
| [age](https://github.com/FiloSottile/age)                                                           | A simple, modern and secure file encryption tool                                                               |
| [aircrack-ng](https://www.aircrack-ng.org)                                                          | Key cracker for the 802.11 WEP and WPA-PSK protocols                                                           |
| [alacritty](https://github.com/alacritty/alacritty)                                                 | A cross-platform, GPU-accelerated terminal emulator                                                            |
| [alsa-utils](https://www.alsa-project.org)                                                          | Advanced Linux Sound Architecture - Utilities                                                                  |
| [ansible](https://pypi.org/project/ansible/)                                                        | Official assortment of Ansible collections                                                                     |
| [ansible-lint](https://github.com/ansible/ansible-lint)                                             | Checks playbooks for practices and behaviour that could potentially be improved.                               |
| [atop](https://www.atoptool.nl/)                                                                    | A system and process level monitor                                                                             |
| [bandwhich](https://github.com/imsnif/bandwhich)                                                    | Terminal bandwidth utilization tool                                                                            |
| [base](https://www.archlinux.org)                                                                   | Minimal package set to define a basic Arch Linux installation                                                  |
| [base-devel](https://www.archlinux.org)                                                             | Basic tools to build Arch Linux packages                                                                       |
| [bash-language-server](https://github.com/bash-lsp/bash-language-server)                            | Bash language server implementation based on Tree Sitter and its grammar for Bash                              |
| [bat](https://github.com/sharkdp/bat)                                                               | Cat clone with syntax highlighting and git integration                                                         |
| [beep](https://github.com/spkr-beep/beep)                                                           | Advanced PC speaker beeping program                                                                            |
| [biber](https://github.com/plk/biber)                                                               | A Unicode-capable BibTeX replacement for biblatex users                                                        |
| [bluez-utils](http://www.bluez.org/)                                                                | Development and debugging utilities for the bluetooth protocol stack                                           |
| [bmon](https://github.com/tgraf/bmon/)                                                              | Portable bandwidth monitor and rate estimator                                                                  |
| [bottom](https://github.com/ClementTsang/bottom)                                                    | A graphical process/system monitor                                                                             |
| [bpftrace](https://github.com/iovisor/bpftrace)                                                     | High-level tracing language for Linux eBPF                                                                     |
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
| [earlyoom](https://github.com/rfjakob/earlyoom)                                                     | Early OOM Daemon for Linux                                                                                     |
| [ebook-tools](https://sourceforge.net/projects/ebook-tools/)                                        | Tools for accessing and converting various ebook file formats                                                  |
| [editorconfig-core-c](https://github.com/editorconfig/editorconfig-core-c)                          | EditorConfig core code written in C (for use by plugins supporting EditorConfig parsing)                       |
| [electron19](https://electronjs.org/)                                                               | Build cross platform desktop apps with web technologies                                                        |
| [element-desktop](https://element.io)                                                               | Glossy Matrix collaboration client — desktop version.                                                          |
| [emacs-nativecomp](https://www.gnu.org/software/emacs/emacs.html)                                   | The extensible, customizable, self-documenting real-time display editor with native compilation enabled        |
| [eva](https://github.com/nerdypepper/eva)                                                           | simple calculator REPL, similar to bc(1)                                                                       |
| [evtest](https://cgit.freedesktop.org/evtest/)                                                      | Input device event monitor and query tool                                                                      |
| [exa](https://the.exa.website/)                                                                     | ls replacement                                                                                                 |
| [fd](https://github.com/sharkdp/fd)                                                                 | Simple, fast and user-friendly alternative to find                                                             |
| [feh](https://feh.finalrewind.org/)                                                                 | Fast and light imlib2-based image viewer                                                                       |
| [figlet](http://www.figlet.org/)                                                                    | A program for making large letters out of ordinary text                                                        |
| [firefox](https://www.mozilla.org/firefox/)                                                         | Standalone web browser from mozilla.org                                                                        |
| [fish](https://fishshell.com/)                                                                      | Smart and user friendly shell intended mostly for interactive use                                              |
| [gfold](https://github.com/nickgerace/gfold)                                                        | A CLI tool to help keep track of Git repositories                                                              |
| [ghidra](https://ghidra-sre.org/)                                                                   | Software reverse engineering framework                                                                         |
| [git-delta](https://github.com/dandavison/delta)                                                    | Syntax-highlighting pager for git and diff output                                                              |
| [glances](https://nicolargo.github.io/glances/)                                                     | CLI curses-based monitoring tool                                                                               |
| [glow](https://github.com/charmbracelet/glow)                                                       | Command-line markdown renderer                                                                                 |
| [gnu-netcat](http://netcat.sourceforge.net/)                                                        | GNU rewrite of netcat, the network piping application                                                          |
| [gopls](https://github.com/golang/tools/tree/master/gopls)                                          | Language server for Go programming language                                                                    |
| [gping](https://github.com/orf/gping)                                                               | Ping, but with a graph                                                                                         |
| [grex](https://github.com/pemistahl/grex)                                                           | A command-line tool for generating regular expressions from user-provided input strings                        |
| [grim](https://git.sr.ht/~emersion/grim)                                                            | Screenshot utility for Wayland                                                                                 |
| [heaptrack](http://milianw.de/tag/heaptrack)                                                        | A heap memory profiler for Linux                                                                               |
| [hexyl](https://github.com/sharkdp/hexyl)                                                           | Colored command-line hex viewer                                                                                |
| [htop](https://htop.dev/)                                                                           | Interactive process viewer                                                                                     |
| [httrack](https://www.httrack.com/)                                                                 | An easy-to-use offline browser utility                                                                         |
| [hugo](https://gohugo.io/)                                                                          | Fast and Flexible Static Site Generator in Go                                                                  |
| [hunspell-en_us](http://wordlist.aspell.net/dicts/)                                                 | US English hunspell dictionaries                                                                               |
| [hyperfine](https://github.com/sharkdp/hyperfine)                                                   | A command-line benchmarking tool                                                                               |
| [imv](https://sr.ht/~exec64/imv/)                                                                   | Image viewer for Wayland and X11                                                                               |
| [intel-ucode](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files)                  | Microcode update files for Intel CPUs                                                                          |
| [interception-dual-function-keys](https://gitlab.com/interception/linux/plugins/dual-function-keys) | Interception plugin for dual-function keys: Tap for one key, hold for another                                  |
| [iotop](http://guichaz.free.fr/iotop/)                                                              | View I/O usage of processes                                                                                    |
| [iwd](https://git.kernel.org/cgit/network/wireless/iwd.git/)                                        | Internet Wireless Daemon                                                                                       |
| [keychain](https://www.funtoo.org/Keychain)                                                         | A front-end to ssh-agent, allowing one long-running ssh-agent process per system, rather than per login        |
| [kismet](https://www.kismetwireless.net/)                                                           | 802.11 layer2 wireless network detector, sniffer, and intrusion detection system                               |
| [kmon](https://github.com/orhun/kmon)                                                               | Linux kernel manager and activity monitor                                                                      |
| [linux-firmware](https://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git)            | Firmware files for Linux                                                                                       |
| [lnav](http://lnav.org/)                                                                            | A curses-based tool for viewing and analyzing log files                                                        |
| [lolcat](https://github.com/busyloop/lolcat)                                                        | Okay, no unicorns. But rainbows!!                                                                              |
| [lostfiles](https://github.com/graysky2/lostfiles)                                                  | Find orphaned files not owned by any Arch packages                                                             |
| [lshw](https://ezix.org/project/wiki/HardwareLiSter)                                                | A small tool to provide detailed information on the hardware configuration of the machine.                     |
| [lsof](https://github.com/lsof-org/lsof)                                                            | Lists open files for running Unix processes                                                                    |
| [ltrace](https://www.ltrace.org/)                                                                   | Tracks runtime library calls in dynamically linked programs                                                    |
| [lxd](https://linuxcontainers.org/lxd)                                                              | Daemon based on liblxc offering a REST API to manage containers                                                |
| [macchanger](https://www.gnu.org/software/macchanger)                                               | A small utility to change your NIC's MAC address                                                               |
| [maim](https://github.com/naelstrof/maim)                                                           | Utility to take a screenshot using imlib2                                                                      |
| [mako](https://mako-project.org)                                                                    | Lightweight notification daemon for Wayland                                                                    |
| [man-db](https://gitlab.com/cjwatson/man-db)                                                        | A utility for reading man pages                                                                                |
| [man-pages](https://www.kernel.org/doc/man-pages/)                                                  | Linux man pages                                                                                                |
| [mediainfo](https://mediaarea.net)                                                                  | Supplies technical and tag information about media files (CLI interface)                                       |
| [miller](https://github.com/johnkerl/miller)                                                        | Name-indexed data processing tool                                                                              |
| [mold](https://github.com/rui314/mold)                                                              | A Modern Linker                                                                                                |
| [mpv](https://mpv.io/)                                                                              | a free, open source, and cross-platform media player                                                           |
| [nasm](https://www.nasm.us)                                                                         | 80x86 assembler designed for portability and modularity                                                        |
| [neofetch](https://github.com/dylanaraps/neofetch)                                                  | A CLI system information tool written in BASH that supports displaying images.                                 |
| [neovim](https://neovim.io)                                                                         | Fork of Vim aiming to improve user experience, plugins, and GUIs                                               |
| [nethogs](https://github.com/raboof/nethogs)                                                        | A net top tool which displays traffic used per process instead of per IP or interface                          |
| [nfs-utils](http://nfs.sourceforge.net)                                                             | Support programs for Network File Systems                                                                      |
| [ngrep](https://github.com/jpr5/ngrep/)                                                             | A grep-like utility that allows you to search for network packets on an interface.                             |
| [nmap](https://nmap.org/)                                                                           | Utility for network discovery and security auditing                                                            |
| [noto-fonts-cjk](https://www.google.com/get/noto/)                                                  | Google Noto CJK fonts                                                                                          |
| [nyancat](https://nyancat.dakko.us/)                                                                | Nyancat rendered in your terminal.                                                                             |
| [obs-studio](https://obsproject.com)                                                                | Free, open source software for live streaming and recording                                                    |
| [okular](https://apps.kde.org/okular/)                                                              | Document Viewer                                                                                                |
| [onefetch](https://github.com/o2sh/onefetch)                                                        | Git repository summary on your terminal                                                                        |
| [pacman-contrib](https://gitlab.archlinux.org/pacman/pacman-contrib)                                | Contributed scripts and tools for pacman systems                                                               |
| [pacutils](https://github.com/andrewgregory/pacutils)                                               | Helper tools for libalpm                                                                                       |
| [paperkey](https://www.jabberwocky.com/software/paperkey/)                                          | Archive OpenPGP keys on paper                                                                                  |
| [parallel](https://www.gnu.org/software/parallel/)                                                  | A shell tool for executing jobs in parallel                                                                    |
| [pass](https://www.passwordstore.org/)                                                              | Stores, retrieves, generates, and synchronizes passwords securely                                              |
| [pdfarranger](https://github.com/pdfarranger/pdfarranger)                                           | Helps merge or split PDF documents and rotate, crop and rearrange pages                                        |
| [perl-file-mimeinfo](https://metacpan.org/release/File-MimeInfo)                                    | Determine file type, includes mimeopen and mimetype                                                            |
| [pipewire-alsa](https://pipewire.org)                                                               | Low-latency audio/video router and processor - ALSA configuration                                              |
| [pipewire-pulse](https://pipewire.org)                                                              | Low-latency audio/video router and processor - PulseAudio replacement                                          |
| [podman](https://github.com/containers/podman)                                                      | Tool and library for running OCI-based containers in pods                                                      |
| [prettier](https://prettier.io/)                                                                    | An opinionated code formatter for JS, JSON, CSS, YAML and much more                                            |
| [procs](https://github.com/dalance/procs)                                                           | A modern replacement for ps written in Rust                                                                    |
| [progress](https://github.com/Xfennec/progress)                                                     | Shows running coreutils basic commands and displays stats                                                      |
| [pueue](https://github.com/nukesor/pueue)                                                           | A CLI tool for managing long running shell commands                                                            |
| [pv](http://www.ivarch.com/programs/pv.shtml)                                                       | A terminal-based tool for monitoring the progress of data through a pipeline.                                  |
| [pyright](https://github.com/microsoft/pyright)                                                     | Type checker for the Python language                                                                           |
| [python-isort](https://github.com/PyCQA/isort)                                                      | A Python utility / library to sort Python imports                                                              |
| [python-pynvim](https://github.com/neovim/pynvim)                                                   | Python client for Neovim                                                                                       |
| [qbittorrent](https://www.qbittorrent.org)                                                          | An advanced BitTorrent client programmed in C++, based on Qt toolkit and libtorrent-rasterbar                  |
| [qrencode](https://fukuchi.org/works/qrencode/)                                                     | C library for encoding data in a QR Code symbol.                                                               |
| [refind](https://www.rodsbooks.com/refind/)                                                         | An EFI boot manager                                                                                            |
| [reflector](https://xyne.dev/projects/reflector)                                                    | A Python 3 module and script to retrieve and filter the latest Pacman mirror list.                             |
| [ripgrep-all](https://github.com/phiresky/ripgrep-all)                                              | rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc.                            |
| [sad](https://github.com/ms-jpq/sad)                                                                | Space Age seD                                                                                                  |
| [scrcpy](https://github.com/Genymobile/scrcpy)                                                      | Display and control your Android device                                                                        |
| [sd](https://github.com/chmln/sd)                                                                   | Intuitive find &amp; replace                                                                                   |
| [shellcheck](https://www.shellcheck.net)                                                            | Shell script analysis tool                                                                                     |
| [shellharden](https://github.com/anordal/shellharden)                                               | Bash linter and syntax highlighter                                                                             |
| [shfmt](https://github.com/mvdan/sh)                                                                | Format shell programs                                                                                          |
| [slurp](https://github.com/emersion/slurp)                                                          | Select a region in a Wayland compositor                                                                        |
| [smartmontools](http://smartmontools.sourceforge.net)                                               | Control and monitor S.M.A.R.T. enabled ATA and SCSI Hard Drives                                                |
| [ssh-audit](https://github.com/jtesta/ssh-audit)                                                    | SSH server and client configuration auditing                                                                   |
| [sshfs](https://github.com/libfuse/sshfs)                                                           | FUSE client based on the SSH File Transfer Protocol                                                            |
| [starship](https://starship.rs/)                                                                    | The cross-shell prompt for astronauts                                                                          |
| [strace](https://strace.io/)                                                                        | A diagnostic, debugging and instructional userspace tracer                                                     |
| [streamlink](https://streamlink.github.io/)                                                         | CLI program that launches streams from various streaming services in a custom video player (livestreamer fork) |
| [swappy](https://github.com/jtheoof/swappy)                                                         | A Wayland native snapshot editing tool                                                                         |
| [sway](https://swaywm.org/)                                                                         | Tiling Wayland compositor and replacement for the i3 window manager                                            |
| [swayidle](https://github.com/swaywm/swayidle)                                                      | Idle management daemon for Wayland                                                                             |
| [swaylock](https://github.com/swaywm/swaylock)                                                      | Screen locker for Wayland                                                                                      |
| [syncthing](https://syncthing.net/)                                                                 | Open Source Continuous Replication / Cluster Synchronization Thing                                             |
| [sysstat](http://pagesperso-orange.fr/sebastien.godard/)                                            | a collection of performance monitoring tools (iostat,isag,mpstat,pidstat,sadf,sar)                             |
| [tcpdump](https://www.tcpdump.org/)                                                                 | Powerful command-line packet analyzer                                                                          |
| [tcpflow](https://github.com/simsong/tcpflow)                                                       | Captures data transmitted as part of TCP connections then stores the data conveniently                         |
| [tectonic](https://tectonic-typesetting.github.io/)                                                 | Modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive                            |
| [telegram-desktop](https://desktop.telegram.org/)                                                   | Official Telegram Desktop client                                                                               |
| [termshark](https://github.com/gcla/termshark)                                                      | Terminal UI for tshark, inspired by Wireshark                                                                  |
| [texlive-latexextra](http://tug.org/texlive/)                                                       | TeX Live - Large collection of add-on packages for LaTeX                                                       |
| [tmux](https://github.com/tmux/tmux/wiki)                                                           | Terminal multiplexer                                                                                           |
| [tokei](https://github.com/XAMPPRocky/tokei)                                                        | A blazingly fast CLOC (Count Lines Of Code) program                                                            |
| [traceroute](http://traceroute.sourceforge.net/)                                                    | Tracks the route taken by packets over an IP network                                                           |
| [trash-cli](https://github.com/andreafrancia/trash-cli)                                             | Command line trashcan (recycle bin) interface                                                                  |
| [ttf-firacode-nerd](https://github.com/ryanoasis/nerd-fonts)                                        | Patched font Fira (Fura) Code from nerd fonts library                                                          |
| [ttf-jetbrains-mono-nerd](https://github.com/ryanoasis/nerd-fonts)                                  | Patched font JetBrains Mono from nerd fonts library                                                            |
| [unarchiver](https://github.com/MacPaw/XADMaster)                                                   | unar and lsar: Objective-C tools for uncompressing archive files                                               |
| [unzip](http://infozip.sourceforge.net/UnZip.html)                                                  | For extracting and viewing files in .zip archives                                                              |
| [up](https://github.com/akavel/up)                                                                  | A tool for writing Linux pipes with instant live preview                                                       |
| [vi](https://ex-vi.sourceforge.net/)                                                                | The original ex/vi text editor                                                                                 |
| [virtualbox](https://virtualbox.org/)                                                               | Powerful x86 virtualization for enterprise as well as home use                                                 |
| [visidata](https://www.visidata.org)                                                                | Terminal spreadsheet multitool for discovering and arranging data                                              |
| [wavemon](https://github.com/uoaerg/wavemon)                                                        | Ncurses-based monitoring application for wireless network devices                                              |
| [waybar](https://github.com/Alexays/Waybar/)                                                        | Highly customizable Wayland bar for Sway and Wlroots based compositors                                         |
| [webhook](https://github.com/adnanh/webhook)                                                        | A lightweight incoming webhook server to run shell commands                                                    |
| [websocat](https://github.com/vi/websocat/)                                                         | Command-line client for web sockets, like netcat/curl/socat for ws://                                          |
| [whois](https://github.com/rfc1036/whois)                                                           | Intelligent WHOIS client                                                                                       |
| [wireshark-qt](https://www.wireshark.org/)                                                          | Network traffic and protocol analyzer/sniffer - Qt GUI                                                         |
| [xorg-xwayland](https://xorg.freedesktop.org)                                                       | run X clients under wayland                                                                                    |
| [yadm](https://github.com/TheLocehiliosan/yadm)                                                     | Yet Another Dotfiles Manager                                                                                   |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp)                                                          | A youtube-dl fork with additional features and fixes                                                           |
| [zathura-pdf-mupdf](https://pwmt.org/projects/zathura-pdf-mupdf/)                                   | PDF support for Zathura (MuPDF backend) (Supports PDF, ePub, and OpenXPS)                                      |
| [zbar](https://github.com/mchehab/zbar)                                                             | Application and library for reading bar codes from various sources                                             |
| [zoxide](https://github.com/ajeetdsouza/zoxide)                                                     | A smarter cd command for your terminal                                                                         |

</div>

<div class="outline-2 smol-table">

### Arch AUR Packages {#arch-aur-packages}

| Name                                                                                               | Description                                                                                                          |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [advcpmv](https://github.com/jarun/advcpmv)                                                        | 'cp' and 'mv' utilities with progress bar patches                                                                    |
| [ancient-packages](http://public.files.xavion.name/Software/ancient-packages/ancient-packages.jpg) | Lists installed packages no longer available (anywhere)                                                              |
| [anki-bin](https://apps.ankiweb.net/)                                                              | Helps you remember facts (like words/phrases in a foreign language) efficiently. Installed with wheel.               |
| [asdf-vm](https://asdf-vm.com)                                                                     | Extendable version manager with support for Ruby, Node.js, Elixir, Erlang &amp; more                                 |
| [cbonsai](https://gitlab.com/jallbrit/cbonsai)                                                     | A bonsai tree generator, written in C using ncurses                                                                  |
| [chars](https://github.com/antifuchs/chars)                                                        | Command line tool to display information about unicode characters.                                                   |
| [cheat](https://github.com/cheat/cheat)                                                            | Allows you to create and view interactive cheatsheets on the command-line                                            |
| [choose-rust-git](https://github.com/theryangeary/choose)                                          | A fast, human-friendly alternative to awk(1) and cut(1)                                                              |
| [cinny-desktop-bin](https://cinny.in/)                                                             | Matrix client focusing primarily on a simple, elegant and secure interface (binary release)                          |
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
| [loggedfs-git](https://rflament.github.io/loggedfs/)                                               | Filesystem monitoring with Fuse                                                                                      |
| [nnn-nerd](https://github.com/jarun/nnn)                                                           | The fastest terminal file manager ever written (with icon support using a patched nerd font).                        |
| [nwg-look-bin](https://github.com/nwg-piotr/nwg-look)                                              | GTK3 settings editor adapted to work in the sway/wlroots environment (binary package)                                |
| [pacgraph](http://kmkeen.com/pacgraph/)                                                            | Draws a graph of installed packages to PNG/SVG/GUI/console. Good for finding bloat.                                  |
| [paru](https://github.com/morganamilo/paru)                                                        | Feature packed AUR helper                                                                                            |
| [pmount](http://pmount.alioth.debian.org/)                                                         | mount removable devices as normal user                                                                               |
| [podman-tui](https://github.com/containers/podman-tui)                                             | Podman Terminal User Interface                                                                                       |
| [procdump](https://github.com/Sysinternals/ProcDump-for-Linux)                                     | Generate coredumps based off performance triggers                                                                    |
| [programmer-calculator](https://github.com/alt-romes/programmer-calculator)                        | A command line calculator made for programmers working with multiple number representations and close to the bits    |
| [ps_mem](https://github.com/pixelb/ps_mem)                                                         | List processes by memory usage                                                                                       |
| [quickemu](https://github.com/quickemu-project/quickemu)                                           | Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.                                  |
| [sampler](https://sampler.dev)                                                                     | A tool for shell commands execution, visualization and alerting. Configured with a simple YAML file.                 |
| [seer-gdb-git](https://github.com/epasveer/seer.git)                                               | Seer - a gui frontend to gdb                                                                                         |
| [sfz](https://github.com/weihanglo/sfz)                                                            | A simple static file server                                                                                          |
| [sshping](https://github.com/spook/sshping)                                                        | ssh-based ping: measure character-echo latency and bandwidth for an interactive ssh session                          |
| [sysz](https://github.com/joehillen/sysz)                                                          | fzf terminal UI for systemctl                                                                                        |
| [teip](https://github.com/greymd/teip)                                                             | Highly efficient "Masking tape" for standard input                                                                   |
| [tsukae-git](https://github.com/irevenko/tsukae)                                                   | Show off your most used shell commands                                                                               |
| [ttf-twemoji](https://github.com/twitter/twemoji)                                                  | Twitter Color Emoji for everyone.                                                                                    |
| [typiskt](https://github.com/budlabs/typiskt)                                                      | touchtype training in the terminal                                                                                   |
| [tz](https://github.com/oz/tz)                                                                     | A time zone helper                                                                                                   |
| [vale](https://github.com/errata-ai/vale)                                                          | A customizable, syntax-aware linter for prose                                                                        |
| [wev-git](https://git.sr.ht/~sircmpwn/wev)                                                         | Print wayland events, like xev(1)                                                                                    |
| [wlay-git](https://github.com/atx/wlay)                                                            | Graphical output management for Wayland                                                                              |
| [wlsunset](https://sr.ht/~kennylevinsen/wlsunset)                                                  | Day/night gamma adjustments for Wayland compositors                                                                  |
| [wofi-emoji-git](https://github.com/dln/wofi-emoji)                                                | Emoji picker for Wayland using wofi and wtype                                                                        |
| [xdg-ninja-git](https://github.com/b3nj5m1n/xdg-ninja)                                             | A shell script which checks your $HOME for unwanted files and directories.                                           |
| [zotero](https://github.com/zotero/zotero)                                                         | A free, easy-to-use tool to help you collect, organize, cite, and share your research sources.                       |

</div>

<div class="outline-2 smol-table">

### Mobile Apps {#mobile-apps}

Absolute dump. I use the [List My Apps](https://f-droid.org/packages/de.onyxbits.listmyapps/) app to generate the csv, the csv is then uploaded to dropbox from where airtable pulls it. When generating the org file my custom script fetches from airtable. I did not want this to be a rube goldberg machine but there doesn't seem to be a very clean way out in the way I need it at the moment.

[Notion](https://play.google.com/store/apps/details?id=notion.id) ○ [Adobe Acrobat](https://play.google.com/store/apps/details?id=com.adobe.reader) ○ [Habits](https://play.google.com/store/apps/details?id=org.isoron.uhabits) ○ [GuitarTuna](https://play.google.com/store/apps/details?id=com.ovelin.guitartuna) ○ [Adobe Scan](https://play.google.com/store/apps/details?id=com.adobe.scan.android) ○ [Zomato](https://play.google.com/store/apps/details?id=com.application.zomato) ○ [Embiggen](https://play.google.com/store/apps/details?id=com.briercan.embiggen) ○ [Snapseed](https://play.google.com/store/apps/details?id=com.niksoftware.snapseed) ○ [List My Apps](https://f-droid.org/repository/browse/?fdid=de.onyxbits.listmyapps) ○ [1.1.1.1](https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone) ○ [Ping Test Tool](https://play.google.com/store/apps/details?id=com.jjo.pingtest) ○ [F-Droid](https://www.google.com/search?q=org.fdroid.fdroid) ○ [PlantNet](https://play.google.com/store/apps/details?id=org.plantnet) ○ [Paytm](https://play.google.com/store/apps/details?id=net.one97.paytm) ○ [Quit Smoking](https://f-droid.org/repository/browse/?fdid=de.baumann.quitsmoking) ○ [Binary](https://play.google.com/store/apps/details?id=com.tomhogenkamp.binaircalculator) ○ [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) ○ [Forest](https://play.google.com/store/apps/details?id=cc.forestapp) ○ [Planta](https://play.google.com/store/apps/details?id=com.stromming.planta) ○ [Kite](https://play.google.com/store/apps/details?id=com.zerodha.kite3) ○ [Wolfram Alpha](https://play.google.com/store/apps/details?id=com.wolfram.android.alpha) ○ [Uber](https://play.google.com/store/apps/details?id=com.ubercab) ○ [Keep Notes](https://play.google.com/store/apps/details?id=com.google.android.keep) ○ [WhatsApp](https://play.google.com/store/apps/details?id=com.whatsapp) ○ [Awesome QR](https://play.google.com/store/apps/details?id=com.github.sumimakito.awesomeqrsample) ○ [Track](https://play.google.com/store/apps/details?id=com.nutritionix.nixtrack) ○ [Replit](https://play.google.com/store/apps/details?id=com.replit.app) ○ [Google Podcasts](https://play.google.com/store/apps/details?id=com.google.android.apps.podcasts) ○ [CRED](https://play.google.com/store/apps/details?id=com.dreamplug.androidapp) ○ [Protractor](https://play.google.com/store/apps/details?id=com.keuwl.protractor) ○ [Pocket](https://play.google.com/store/apps/details?id=com.ideashower.readitlater.pro) ○ [Grapevine](https://play.google.com/store/apps/details?id=com.app.gvine) ○ [Bluecoins](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) ○ [Url forwarder](https://play.google.com/store/apps/details?id=net.daverix.urlforward) ○ [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) ○ [Crayon](https://play.google.com/store/apps/details?id=com.jndapp.cartoon.crayon.iconpack) ○ [SoundCloud](https://play.google.com/store/apps/details?id=com.soundcloud.android) ○ [Track &amp; Graph](https://f-droid.org/repository/browse/?fdid=com.samco.trackandgraph) ○ [Unit Converter Ultimate](https://f-droid.org/repository/browse/?fdid=com.physphil.android.unitconverterultimate) ○ [Pinterest](https://play.google.com/store/apps/details?id=com.pinterest) ○ [GitHub](https://play.google.com/store/apps/details?id=com.github.android) ○ [VLC](https://play.google.com/store/apps/details?id=org.videolan.vlc) ○ [Telegram](https://play.google.com/store/apps/details?id=org.telegram.messenger) ○ [Airtable](https://play.google.com/store/apps/details?id=com.formagrid.airtable) ○ [Niagara Launcher](https://play.google.com/store/apps/details?id=bitpit.launcher) ○ [BHIM](https://play.google.com/store/apps/details?id=in.org.npci.upiapp) ○ [Shazam](https://play.google.com/store/apps/details?id=com.shazam.android) ○ [Drinkable](https://f-droid.org/repository/browse/?fdid=com.moimob.drinkable) ○ [Goodreads](https://play.google.com/store/apps/details?id=com.goodreads) ○ [Wikipedia](https://play.google.com/store/apps/details?id=org.wikipedia) ○ [Termux](https://f-droid.org/repository/browse/?fdid=com.termux) ○ [Discord](https://play.google.com/store/apps/details?id=com.discord) ○ [Signal](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) ○ [Product Hunt](https://play.google.com/store/apps/details?id=com.producthuntmobile) ○ [Coin](https://play.google.com/store/apps/details?id=com.zerodha.coin) ○ [SimpleLogin](https://play.google.com/store/apps/details?id=io.simplelogin.android) ○ [Syncthing](https://play.google.com/store/apps/details?id=com.nutomic.syncthingandroid) ○ [Tapo](https://play.google.com/store/apps/details?id=com.tplink.iot) ○ [Lithium](https://play.google.com/store/apps/details?id=com.faultexception.reader) ○ [Snipd](https://play.google.com/store/apps/details?id=ai.topicfinder.podcastdiscovery) ○ [Brave](https://play.google.com/store/apps/details?id=com.brave.browser) ○ [NetGuard](https://play.google.com/store/apps/details?id=eu.faircode.netguard) ○ [PhonePe](https://play.google.com/store/apps/details?id=com.phonepe.app) ○ [HTTP Shortcuts](https://play.google.com/store/apps/details?id=ch.rmy.android.http_shortcuts) ○ [BigO](https://play.google.com/store/apps/details?id=hieunguyen725.bigo) ○ [Splitwise](https://play.google.com/store/apps/details?id=com.Splitwise.SplitwiseMobile) ○ [Relay Pro](https://play.google.com/store/apps/details?id=reddit.news) ○ [Zoom](https://play.google.com/store/apps/details?id=us.zoom.videomeetings) ○ [Binance](https://play.google.com/store/apps/details?id=com.binance.dev) ○ [Just Another Workout Timer](https://f-droid.org/repository/browse/?fdid=com.blockbasti.justanotherworkouttimer) ○ [Chess](https://play.google.com/store/apps/details?id=com.chess) ○ [WiFiAnalyzer](https://f-droid.org/repository/browse/?fdid=com.vrem.wifianalyzer) ○ [Tasks](https://play.google.com/store/apps/details?id=com.google.android.apps.tasks) ○ [Rapido](https://play.google.com/store/apps/details?id=com.rapido.passenger) ○ [DiskUsage](https://play.google.com/store/apps/details?id=com.google.android.diskusage) ○ [TrebleShot](https://play.google.com/store/apps/details?id=com.genonbeta.TrebleShot) ○ [Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)

</div>

</div>
