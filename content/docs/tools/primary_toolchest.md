+++
title = "Primary tool-chest"
author = ["Hrishikesh Barman"]
draft = false
+++

My dotfiles are currently private, but they contain [my fish functions](https://github.com/geekodour/x/tree/main/.config/fish/functions)(aliases), [my yasnippets](https://github.com/geekodour/x/tree/main/.config/doom/snippets) and [cheats](https://cheats.geekodour.org/)

<div class="outline-1 smol-table">

## Komputeer Ussah {#komputeer-ussah}

As a non-ai system, I like to interact with a physical computer. I like its novelty.

{{< coolinks >}}
-   Music: [lofi.cafe](https://www.lofi.cafe/) | [earth.fm](https://earth.fm) | [threesixfive](https://daily.threesixfive.shop/) | [Radio Garden](http://radio.garden/visit/jaipur/QSlnmGmG) | [90's TV](https://www.my90stv.com/) | [relax//five](https://relax.five.sh/) | [chiptune](https://chiptune.app/)
-   Info: [tosdr](https://tosdr.org/) | [W3Survey](https://w3techs.com/technologies) 🌟 | [undertheradar](https://undertheradar.io/) | [webcompact](https://webcompat.com/) | [endoflife.date](https://endoflife.date/) | [Farside](https://farside.link/) | [Climate Reanalyzer](https://climatereanalyzer.org/clim/sst_daily/) | [BrutalistReport](https://brutalist.report/)
-   Conversion/Gen: [onlinelisttools](https://onlinelisttools.com/) | [Squoosh](https://squoosh.app/) | [transform.tools](https://transform.tools/) | [Barcode Generator](https://barcode.tec-it.com/en) | [QR Code Gen](https://qrcode.antfu.me/) | [Metric-time](https://metric-time.com/)
-   Free computers: [WINDOWS93](https://www.windows93.net/) | [SegFault](https://shell.segfault.net/#/dashboard) | [Virtual x86 WASM](https://copy.sh/v86/) | [WebVM](https://webvm.io/)
{{< /coolinks >}}

</div>

<div class="outline-1 smol-table">

## General development {#general-development}

Now how I do development has varied over the years. But I am constantly updating it.

{{< lft >}}
-   Urgent AF
    -   [Using AI tools](https://lobste.rs/s/dfmiko/using_github_copilot_for_unit_testing) for [development](https://lobste.rs/s/iualxr/ai_enhanced_development_makes_me_more).
-   Sooner the better
    -   Re-start OSS contributions, start maintaining some projects [and packages](https://github.com/jubalh/awesome-package-maintainer) of interest.
    -   Learn how to use sourcegraph for codesearch better
-   Lazy Sunday
    -   I think I want to run [gprofiler](https://github.com/Granulate/gprofiler) on my machine
    -   Check out these search related projects and see how they work UTH, [stork](https://github.com/jameslittle230/stork), [meilisearch](https://github.com/meilisearch/meilisearch), [edgesearch](https://github.com/wilsonzlin/edgesearch), [pagefind](https://github.com/CloudCannon/pagefind)
    -   Check if I can use [runno](https://runno.dev/) in my blog
    -   Check if want to adopt  [renovatebot](https://docs.renovatebot.com/)
{{< /lft >}}

{{< coolinks >}}
-   Exploration: [CyberChef](https://gchq.github.io/CyberChef/) | [AST explorer](https://astexplorer.net/) | [Text Encoding Detect](https://charsetnormalizerweb-ousret.vercel.app/)
-   Helper tools: [githistory](https://githistory.xyz/) | [hadoukenify](https://reibitto.github.io/hadoukenify/) | [starhistory](https://star-history.com) | [gh-badges](https://badgers.space/) |  [SpeedSheet](https://speedsheet.io/)
-   Reference: [hyperpolyglot](/backupsites/hyperpolyglot.org/) | [ManKier](https://www.mankier.com/) | [OWASP Cheats](https://cheatsheetseries.owasp.org/index.html) | [coreutils](https://www.maizure.org/projects/decoded-gnu-coreutils/) | [DADS](https://xlinux.nist.gov/dads/) | [OEIS](https://oeis.org/)
-   Numbers: [units](https://frinklang.org/frinkdata/units.txt) | [facts](http://www-formal.stanford.edu/jmc/facts.txt) | [File Magic Numbers](https://www.garykessler.net/library/file_sigs.html) | [managing units](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2981r1.html)
{{< /coolinks >}}

<div class="outline-2 smol-table">

### Editing text {#editing-text}

I didn't really care what my editor was until I met neel and pritam in my previous workplace.

{{< lft >}}
-   Urgent AF
-   Sooner the better
-   Lazy Sunday
{{< /lft >}}

-   95% doom emacs(heavily customized), 5% neovim
-   I think I spent half of my year last year fighting with emacs, had me learn little bit of elisp and I am not sure if it was worth it, but if there's one thing I cannot live without, it has to be `org-mode`. helluvadrug.
-   For documentation lookup inside emacs, `eldoc` (using `elglot`), `M-x man`, `dev-docs` custom bindings for `eww`.
-   When I quickly need to check the contents of a repo, I use [GitHub1s](https://github1s.com/), pretty neat stuff. I use Replit for quick prototypes etc, pretty neat but need to get back offline as soon as I need to do anything that involves more than 2 files(when writing from scratch).

</div>

<div class="outline-2 smol-table">

### Interface and dependencies {#interface-and-dependencies}

{{< lft >}}
-   Urgent AF
-   Sooner the better
-   Lazy Sunday
    -   Checking how [test containers](https://golang.testcontainers.org/) and [dev containers](https://containers.dev/) compare to my LXD workflow
    -   Checkout [NixOS](https://news.ycombinator.com/item?id=36260626)
    -   I am planning to write some aliases and function wrapper around [ffmpeg](https://img.ly/blog/ultimate-guide-to-ffmpeg/) and imagemagick for regular stuff. Most probably there are good tools out there, have to check.
{{< /lft >}}

-   `fish` is my shell, have a love hate relationship ngl.
-   `pacman` and `paru` mostly have me covered
-   For different versions of stuff, I use `asdf` + `direnv`. I really like the global, local flexibility that `asdf` gives.
-   For virtual environments, I use `LXD` system containers with a custom cloud-init script. It's pretty neat. Thanks to the co-workers at my last workplace! (See my [notes on lxd](https://mogoz.geekodour.org/search/?query=lxd))
-   [svu](https://github.com/caarlos0/svu) is great for quick help on semantic versions
-   [entr](https://jvns.ca/blog/2020/06/28/entr/) and running tests in watchmode is essential

</div>

</div>

<div class="outline-1 smol-table">

## Language specific {#language-specific}

<div class="outline-2 smol-table">

### JS/TS {#js-ts}

{{< lft >}}
-   Urgent AF
    -   Getting better at Typescript
-   Sooner the better
    -   Experiment w [workers](https://github.com/BuilderIO/partytown) and nodejs [threadpool libraries](https://github.com/tinylibs/tinypool).
-   Lazy Sunday
    -   Need to check what is [unifiedjs](https://unifiedjs.com/)
{{< /lft >}}

{{< coolinks >}}
-   Info: [Package Phobia](https://packagephobia.com/) | [bundlephobia](https://bundlephobia.com)
{{< /coolinks >}}

</div>

<div class="outline-2 smol-table">

### Python {#python}

{{< lft >}}
-   Urgent AF
    -   Need to check [fastapi](https://github.com/tiangolo/fastapi) has to offer
-   Sooner the better
    -   Check memray and [gaogaotiantian/viztracer](https://github.com/gaogaotiantian/viztracer)
-   Lazy Sunday
    -   Checkout tqdm and more-itertools, toolz
    -   Check [tuna](https://github.com/nschloe/tuna), [jamesturk/jellyfish](https://github.com/jamesturk/jellyfish) (create something), [networkx](https://news.ycombinator.com/item?id=38578185)
    -   Use [cog](https://news.ycombinator.com/item?id=38610851) in one of my projects, it's the embed go thing in markdown that i used
{{< /lft >}}

{{< coolinks >}}
-   Info: [PyPI Data](https://py-code.org/stats)
-   Reference: [Common Gotchas](https://docs.python-guide.org/writing/gotchas/)
{{< /coolinks >}}

-   I use asdf + poetry for all my python virtual env setups. Even if it's a project with a `requirements.txt`, I use poetry to create a venv there and pip install on it. I don't think i'll ever understand python virtual environments completely so I am going for the path of least resistance
-   Understanding python's [import system](https://mogoz.geekodour.org/posts/20221231140207-python/#imports) has done me wonders
-   `pudb` with `ipython` is pretty neat for debugging
-   I don't have any linting, formatter preference honestly I just use the defaults that work with my editor setup. If any project needs specific style, the CI/CD system should catch it.
-   Once [joblib](https://joblib.readthedocs.io/en/latest/index.html#) was very useful to me but I can't exactly remember when (also `more-itertools`)

</div>

<div class="outline-2 smol-table">

### Golang {#golang}

{{< lft >}}
-   Urgent AF
    -   Try out [failsafe-go](https://github.com/failsafe-go/failsafe-go)
    -   Try out [samber/lo](https://github.com/samber/lo)  (lodash for go)
-   Sooner the better
    -   check [autogold](https://github.com/hexops/autogold)
-   Lazy Sunday
    -   I don't think I'll immediately need it but [gotraceui](https://github.com/dominikh/gotraceui) looks neat
{{< /lft >}}

-   Haven't done anything in a while

</div>

<div class="outline-2 smol-table">

### C {#c}

{{< coolinks >}}
-   References: [C coding style](https://nullprogram.com/blog/2023/10/08/)
{{< /coolinks >}}

</div>

<div class="outline-2 smol-table">

### Ocaml {#ocaml}

{{< coolinks >}}
-   References: [OCaml Syntax Cheatsheet](https://ocamlsyntax.com/)
{{< /coolinks >}}

</div>

</div>

<div class="outline-1 smol-table">

## Domain specific {#domain-specific}

<div class="outline-2 smol-table">

### Web {#web}

Working on web things is fun, I am terrible at anything that involves css but I think it's pretty neat.

{{< lft >}}
-   Urgent AF
    -   Really grokking HTTP, Headers, Cache, Cookies and Sessions
    -   Experimenting w [WebAssembly](https://github.com/stealthrocket/timecraft), [webworkers](https://github.com/GoogleChromeLabs/comlink) [other](https://news.ycombinator.com/item?id=37035178) web engineering fun.
    -   Experiment w backends offering user auth, [pocketbase](https://pocketbase.io/), supabase.
    -   I think I need to explore webcomponts etc. what's all the fuss about.
    -   Also hypermedia. damn.
-   Sooner the better
    -   Experimenting w serverless functions (Mostly cf workers)
    -   Faking libraries are great, need to see which one to use when. Candidates, [json-server](https://github.com/typicode/json-server), [faker](https://github.com/faker-js/faker), [json-schema-faker](https://github.com/json-schema-faker/json-schema-faker),[msw](https://github.com/mswjs/msw)
    -   Explore more in web security side of things
    -   Check out API testing stuff: [stepci](https://github.com/stepci/stepci), [scanapi](https://github.com/scanapi/scanapi), [oha](https://github.com/hatoo/oha)
-   Lazy Sunday
    -   Check [puck](https://github.com/measuredco/puck), if we can do something similar for svelte
    -   [Elixir, Phoenix and LiveView.](https://thinkingelixir.com/petal-stack-in-elixir/)
        -   LiveView is different in a way that instead of using HTTP and large-grain data exchange, it uses websockets and sends fine-grained updates.
{{< /lft >}}

{{< coolinks >}}
-   Info/Exploration: [caniuse](https://caniuse.com/) | [Browserleaks](https://browserleaks.com/) | [KeyCDN Tools](https://tools.keycdn.com/) | [CSP Evaluator](https://csp-evaluator.withgoogle.com/) | [Authentication Test](https://authenticationtest.com/) | [Request Catcher](https://requestcatcher.com/) | [WebBrowserTools](https://webbrowsertools.com/)
-   References: [rosettatype/hyperglot](https://hyperglot.rosettatype.com/) | [image codec](https://storage.googleapis.com/demos.webmproject.org/webp/cmp/index.html) | [DOM Events](https://domevents.dev/) | [worker playground](https://worker-playground.glitch.me/) | [TLSFast](https://istlsfastyet.com/) | [Console Utilities API reference](https://developer.chrome.com/docs/devtools/console/utilities/#recent)
-   CSS &amp; Animations: [Almanac](https://css-tricks.com/almanac/) | [Animista](https://animista.net/play/basic/scale-up) | [Type Scale](https://typescale.com/) | [Utopia](https://utopia.fyi/) | [shadcn/ui](https://ui.shadcn.com/) | [tailwind cheat](https://umeshmk.github.io/Tailwindcss-cheatsheet/)
-   SVG: [SVG Artista](https://svgartista.net/) | [SVG Reference](https://fffuel.co/sssvg/) | [SVGcode](https://svgco.de/)
-   Toolchain: [Import Map](https://generator.jspm.io)
-   API/Requests: [httpbin](https://httpbin.org/#/) | [REDbot Caching](https://redbot.org/) | [Mozilla Observatory](https://observatory.mozilla.org/)
-   Better no-code: [mmm.page](https://build.mmm.page/)
{{< /coolinks >}}

-   Everything I learn here becomes obsolete in about six months
-   But I like the web and I want to build on it too
-   I am too bad at anything involving CSS so, tailwindcss is my best friend here.
-   I once tried doing react+vite+storybook with all the right config and other stuff, later I felt that I don't want to be worrying about a static site so much. So static sites or semi-static sites are basically an org-mode export or a next.js site for me now.
-   I think I learned react about 3 times and everytime, the documentation gets overhauled(good thing). But the last time I learned react, I [took notes](https://mogoz.geekodour.org/search/?query=react).
-   Don't ask me about framework preferences. I don't think I agree with myself here.
-   I played around w using [verb](https://github.com/federicotdn/verb) for documenting api calls. I like it. It's not suitable for all usecases but for some its gold. Otherwise insomnia or postman as required.
-   Finally tried svelte with my wscribe-editor project, it was fun. But need to play with it more to have better gasp.

</div>

<div class="outline-2 smol-table">

### UI &amp; Interface {#ui-and-interface}

I like building small tools and usually they need interfaces.

{{< lft >}}
-   Urgent AF
    -   CLI stuff: [imtui](https://github.com/ggerganov/imtui), [Textualize](https://www.textualize.io/), [tview](https://github.com/rivo/tview/), [bubbletea](https://github.com/charmbracelet/bubbletea), [ink](https://github.com/vadimdemedes/ink)
-   Sooner the better
-   Lazy Sunday
    -   Check out GUI stuff: [wailsapp/wails](https://github.com/wailsapp/wails), [tauri](https://tauri.app/), [fyne](https://github.com/fyne-io/fyne), [imgui](https://github.com/ocornut/imgui), [lvgl](https://github.com/lvgl/lvgl)
{{< /lft >}}

</div>

<div class="outline-2 smol-table">

### Systems {#systems}

This includes all things systems.

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Check if I can write scripts faster with [google/zx](https://github.com/google/zx)
-   Lazy Sunday
    -   I don't know many c/cpp libraries but would try to use [zpl-c/zpl](https://github.com/zpl-c/zpl) next time I get an opportunity to work on something similar.
    -   I don't play w proto stuff that much but think [protodot could](https://github.com/seamia/protodot) be v.useful
    -   Learn what [multiformats](https://multiformats.io/) is about. Specifically interested in multibase.
    -   Memory profiling is interesting, I never got to try gdb, [rr](https://rr-project.org/)(tried rr, some issues in nixos), [valgrind](https://m-peko.github.io/craft-cpp/posts/valgrind-a-neglected-tool-from-the-shadows-or-a-serious-debugging-tool/) and friends properly. So someday/someweek might hack around and see how these can be useful. [Valgrind and Address sanitizers](https://github.com/google/sanitizers/wiki/AddressSanitizerComparisonOfMemoryTools), simpler tools like [bytehound](https://github.com/koute/bytehound/issues/4#issuecomment-493762691)
    -   Cool tool to see changes before making, [check it out](https://github.com/binpash/try)
{{< /lft >}}

{{< coolinks >}}
-   Debugging: [godbolt](https://godbolt.org/) | [explainshell](https://explainshell.com/) | [Dogbolt](https://dogbolt.org/)
-   Reference: [coreutils](https://maizure.org/projects/decoded-gnu-coreutils/) | [Sysctl Explorer](https://sysctl-explorer.net/) | [procps-ng](https://gitlab.com/procps-ng/procps) | [sh-bible](https://github.com/dylanaraps/pure-sh-bible) | [Map of Linux](https://makelinux.github.io/kernel/map/)
{{< /coolinks >}}

</div>

<div class="outline-2 smol-table">

### Distributed systems &amp; sync &amp; offline {#distributed-systems-and-sync-and-offline}

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Play w [maelstrom](https://github.com/jepsen-io/maelstrom) probably via the fly.io challenge
-   Lazy Sunday
    -   Check out [stateright](https://github.com/stateright/stateright)
    -   Play w sync libs [yjs](https://github.com/yjs/yjs) and [automerge](https://github.com/automerge/automerge)
    -   Play w [Replicache](https://replicache.dev/), [Ditto](https://www.ditto.live/)
{{< /lft >}}

</div>

<div class="outline-2 smol-table">

### Network programming &amp; P2P {#network-programming-and-p2p}

I love networks, I love p2p more.

{{< lft >}}
-   Urgent AF
    -   Experimenting w [websockets](https://mogoz.geekodour.org/posts/20230222181643-websockets/), [WebRTC](https://mogoz.geekodour.org/posts/20230318150409-webrtc/) and other fun stuff
-   Sooner the better
-   Lazy Sunday
    -   Check if [shadow simulator](https://github.com/shadow/shadow) will be useful to run p2p/learning experiments
{{< /lft >}}

{{< coolinks >}}
-   Tools: [BGP.Tools](https://bgp.tools/)
{{< /coolinks >}}

</div>

<div class="outline-2 smol-table">

### Programming languages {#programming-languages}

{{< lft >}}
-   Urgent AF
    -   [ohm](https://github.com/ohmjs/ohm) looks super interesting. Can be useful for creative programming stuff aswell I think. (This is something i want to explore for bml transpilation aswell)
-   Sooner the better
-   Lazy Sunday
    -   [Make](https://github.com/tabatkins/railroad-diagrams) [rails](https://github.com/dundalek/GrammKit)
    -   Check [this](https://github.com/maciejhirsz/logos), [this](https://github.com/pest-parser/pest), and [this](https://github.com/antlr/antlr4)
    -   Check [semgrep](https://semgrep.dev/blog/2021/semgrep-a-static-analysis-journey/)
{{< /lft >}}

</div>

<div class="outline-2 smol-table">

### Creative programming &amp; HCI {#creative-programming-and-hci}

So these are things I am just starting to learn. Creative programming is something I want to do for fun, HCI is something that really interests me. I have syllabus entries for it aswell iirc.

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Get started w creative programming, see [notes](https://mogoz.geekodour.org/posts/20230326125239-creative_programming/). Think it'll be p5 for the start. Also check [G9](https://news.ycombinator.com/item?id=37058674)
-   Lazy Sunday
    -   Create explorable explanations, check [Idyll](https://idyll-lang.org/docs). also [want](https://dustingmixon.wordpress.com/2023/08/04/math-exposition-on-youtube/) to check [cindy](https://cindyjs.org/), [matter.js](https://brm.io/matter-js/) and [manim](https://github.com/3b1b/manim), [mathbox](https://github.com/unconed/mathbox), [mafs](https://mafs.dev/), [Motion Canvas](https://motioncanvas.io/), also check [making of a circle](https://www.redblobgames.com/making-of/circle-drawing/)
    -   Explore hypercard [related](https://beyondloom.com/decker/index.html) projects. [vipercard](https://github.com/moltenform/vipercard)
{{< /lft >}}

{{< coolinks >}}
-   Reference: [Web render benchmarks](https://benchmarks.slaylines.io/pixi.html)
-   Showcases: [Explorable Explanations](https://explorabl.es/) | [awesome-explorables](https://github.com/blob42/awesome-explorables) | [wolframdemos](https://demonstrations.wolfram.com/)
-   Helper tools: [drawingbots](https://drawingbots.net/) | [SPACE TYPE](https://spacetypegenerator.com/) | [shapecatcher](https://shapecatcher.com/)
-   Layouts and elements: [98.css](https://github.com/jdan/98.css) | [winbox](https://github.com/nextapps-de/winbox) | [RoughNotations](https://github.com/rough-stuff/rough-notation) | [cursor-effects](https://tholman.com/cursor-effects/) | [omnio](https://github.com/bopwerks/omnino)
{{< /coolinks >}}

</div>

</div>

<div class="outline-1 smol-table">

## Data {#data}

<div class="outline-2 smol-table">

### Database {#database}

{{< lft >}}
-   Urgent AF
    -   Check [centerofci/mathesar](https://github.com/centerofci/mathesar) and see if can help in learning
    -   Go through the excellent MySQL intermediate series by PlanetScale
-   Sooner the better
    -   Experimenting more with SQLite (and ecosystem), Postgres (and ecosystem), Clickhouse, DuckDB, Redis.
-   Lazy Sunday
    -   Check what's [PRQL](https://prql-lang.org/)'s about
    -   Checkout [sqlglot - sql parser](https://github.com/tobymao/sqlglot)
{{< /lft >}}

{{< coolinks >}}
-   Resources: [DB-Engines Ranking](https://db-engines.com/en/ranking) | [Database of Databases](https://dbdb.io/) | [Troublesome words in SQL](https://modern-sql.com/reserved-words-empirical-list)
-   PG: [PG Lock Conflicts](https://pglocks.org/) | [Postgres locks explorer](https://leontrolski.github.io/pglockpy.html) | [PGTune](https://pgtune.leopard.in.ua/#%2F=) | [PostgreSQL Observability](https://pgstats.dev/) | [postgresqlco](https://postgresqlco.nf/doc/en/param/) | [pg-browser(wasm)](https://github.com/datawan-labs/pg)
-   PG EXPLAIN viz: [EXPLAIN Visualizer(pev)](http://tatiyants.com/pev/#/plans) | [Explain Viz](https://explain.depesz.com/)
{{< /coolinks >}}

-   I don't play with DBs on the daily but plan to.

</div>

<div class="outline-2 smol-table">

### Data Engineering {#data-engineering}

{{< lft >}}
-   Urgent AF
-   Sooner the better
-   Lazy Sunday
    -   Try out [steampipe](https://til.simonwillison.net/sqlite/steampipe)
{{< /lft >}}

-   `jq` w `ijq` has been useful in the past. I think there are 2 totally different projects named `ijq`, it's the one that I have installed. `dasel` was also pretty neat once.

</div>

<div class="outline-2 smol-table">

### Data Analysis/Viz {#data-analysis-viz}

{{< lft >}}
-   Urgent AF
    -   Try viz platforms: [Datawrapper](https://www.datawrapper.de/), [Desmos](https://www.desmos.com/), [ObservableHQ](https://observablehq.com/), [quarto](https://quarto.org/), [rath](https://github.com/Kanaries/Rath)
-   Sooner the better
    -   CLI [stuff](https://github.com/devottys/darkdraw)
    -   Checkout [streamlit](https://streamlit.io/), [gradio](https://github.com/gradio-app/gradio) and [datapane](https://github.com/datapane/datapane)
-   Lazy Sunday
    -   Try viz tools: D3, [SandDance](https://microsoft.github.io/SandDance/), [ObservablePlots](https://observablehq.com/plot/), [Vega](https://vega.github.io/vega/), [plouc/nivo](https://github.com/plouc/nivo).
    -   Check out [Directus](https://directus.io/), [baserow](https://baserow.io/), [nocodb](https://github.com/nocodb/nocodb) if it can replace airtable for me.
    -   Play w [kats](https://engineering.fb.com/2021/06/21/open-source/kats/)
    -   Check out [Gephi Lite](https://gephi.org/gephi-lite/), [Perspective](https://perspective.finos.org/), [Quadratic](https://www.quadratichq.com/), [marimo](https://marimo.io/)
    -   check [nomic atlas](https://atlas.nomic.ai/)
{{< /lft >}}

{{< coolinks >}}
-   Showcases: [Visualization Browser](https://textvis.lnu.se/) | [Flowing Media](http://flowingmedia.com/gallery.html) | [datavizproject](https://datavizproject.com/)
-   References: [Eng Statistical Methods](https://www.itl.nist.gov/div898/handbook/index.htm)
{{< /coolinks >}}

-   I use Airtable extensively as my data-store for things. I'll probably move to something else if I ever hit limits.
-   Occasionally I'd use Datasette but I want to use more of it. esp the sqlite-utils stuff looks interesting.
-   To explore datasets I use visidata. It [is awesome](https://www.visidata.org/docs/formats/). Not only csv, parquet but also json, sqlite, postgres, shapefiles/mbtiles, pcap files! etc.

</div>

<div class="outline-2 smol-table">

### AI/ML experiments {#ai-ml-experiments}

I by no means know anything about what's happening in that space but I've been watching from far and I can tell, I cannot afford to blink. I have to take the dive sometime. I already have courses and stuff lined up and brushing up on math.

{{< lft >}}
-   Urgent AF
    -   Properly checkout [Huggingface](https://huggingface.co/) and what can I do with [auto](https://huggingface.co/autotrain) [ML?](https://github.com/autogluon/autogluon)
    -   Check [Web AI Model Testing](https://news.ycombinator.com/item?id=39017607)
-   Sooner the better
    -   Check if I can add semantic search to my wiki using [txtai](https://github.com/neuml/txtai) and [stenence transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
    -   Check [label-studio](https://github.com/HumanSignal/label-studio) and if I can use it for some of my usecases
-   Lazy Sunday
    -   whisper.cpp (also [bark](https://github.com/suno-ai/bark)), [llma.cpp](https://gist.github.com/rain-1/8cc12b4b334052a21af8029aa9c4fafc) et al, [Web LLM](https://lobste.rs/s/prfiun/web_llm_runs_vicuna_7b_large_language) [looks](https://github.com/mlc-ai/web-stable-diffusion) pretty sick.
    -   Read [nanoGPT](https://github.com/karpathy/nanoGPT), check [weightwatcher](https://weightwatcher.ai/)
    -   What's up with [paddle](https://github.com/PaddlePaddle/PaddleOCR) [paddle](https://github.com/PaddlePaddle/PaddleGAN) and [other](https://huggingface.co/docs/transformers/model_doc/markuplm) [document](https://github.com/deepdoctection/deepdoctection) [extraction](https://github.com/mindee/doctr) [stuff](https://github.com/JaidedAI/EasyOCR).
{{< /lft >}}

{{< coolinks >}}
-   Visualizers: [netron](https://github.com/lutzroeder/netron) | [Attention Viz](http://attentionviz.com/) | [Diffusion Explainer](https://poloclub.github.io/diffusion-explainer/) | [VRAM Calculator](https://vram.asmirnov.xyz/)
-   Reference: [Cloud GPU Guide](https://gpus.llm-utils.org/the-gpu-guide/) | [Timeline of AI Models](https://ai.v-gar.de/ml/transformer/timeline/index.html) | [LLM Benchmarks](https://benchmarks.llmonitor.com/)
-   Leaderboards: [OpenLLM](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) | [HumanEval](https://paperswithcode.com/sota/code-generation-on-humaneval) | [lmsys](https://chat.lmsys.org/?leaderboard) | [AlpacaEval](https://tatsu-lab.github.io/alpaca_eval/) |[oobabooga](https://github.com/oobabooga/oobabooga.github.io/blob/main/arena/results.md) | [chatbot](https://lmsys.org/blog/2023-05-25-leaderboard/)
-   Tools: [chub](https://www.chub.ai/) | [lllmahub](https://llamahub.ai/)
{{< /coolinks >}}

-   When SD came out, played a lot with [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

</div>

<div class="outline-2 smol-table">

### Archiving and Scraping {#archiving-and-scraping}

{{< lft >}}
-   Urgent AF
    -   I have some [Scraping](https://mogoz.geekodour.org/posts/20230115032823-scraping/) and [Archival](https://mogoz.geekodour.org/posts/20230115032923-archival/) notes that I have to go through
-   Sooner the better
    -   [ ] Check [webrecorder](https://webrecorder.net/) [and](https://docs.wabarc.eu.org/) [friends](https://conifer.rhizome.org/)
    -   [ ] Setup [archivebox](https://github.com/ArchiveBox/ArchiveBox), I feel guilty because I don't contribute to the archive-warrior team and use their service heavily. I'll 100% contribute once I start making money or something.
-   Lazy Sunday
    -   [ ] Check out out [kiwix](https://news.ycombinator.com/item?id=33274186), [Internet in a Box](https://news.ycombinator.com/item?id=35750165), [piratebox](https://piratebox.cc/goals), [dwebmirror](https://github.com/internetarchive/dweb-mirror)
    -   [ ] I need to setup linkchecker in my sites, candidates are [muffet](https://github.com/raviqqe/muffet)(used prev), [deadlink](https://github.com/nschloe/deadlink), [lychee](https://github.com/lycheeverse/lychee), [awesome_bot](https://github.com/dkhamsing/awesome_bot) and [linkinator](https://github.com/JustinBeckwith/linkinator). I also want to write my own link checker but if one of these work out, which i think it would g2g.
{{< /lft >}}

{{< coolinks >}}
-   Query: [Quarry for Wikipedia](https://quarry.wmcloud.org/)
-   Bot detection tests: [Bot / Headless Chrome Detection Tests](https://bot.incolumitas.com/) | [Pixelscan](https://pixelscan.net/) | [Antibot](https://bot.sannysoft.com/) | [CreepJS](https://abrahamjuliot.github.io/creepjs/) | [Detect WebGL Fingerprint](https://webbrowsertools.com/webgl-fingerprint/)
{{< /coolinks >}}

-   If the page is somewhat structured, Can use underlying parsers(lxml, html5lib, requests-html etc.) directly. See my Reconnaissance Checklist :)
-   [Playwright](https://github.com/TheWebScrapingClub/webscraping-from-0-to-hero/blob/main/Pages/3.Free%20Tools/Playwright.md): When requirement is rendered browser.
    -   Playwright &gt; Puppeter &gt; Selenium
    -   Randomize mouse movements, consistent combination of device to emulate, slow_mo option, brave browser etc
    -   Support multiple web browsers, such as Chromium, Firefox, and Webkit-based Safari, out of the box
    -   Suggestions: [playwright_stealth](https://github.com/TheWebScrapingClub/webscraping-from-0-to-hero/blob/main/Pages/3.Free%20Tools/Playwright_stealth.md), [Making Chrome Headless Undetectable](https://intoli.com/blog/making-chrome-headless-undetectable/), [recorder and codegen](https://playwright.dev/docs/codegen), [crawlee(anti-bot/scraping framework)](https://crawlee.dev/)
-   [Scrapy](https://github.com/TheWebScrapingClub/webscraping-from-0-to-hero/blob/main/Pages/3.Free%20Tools/Scrapy.md): Fist thing to reach out for.
    -   Useful for complex projects that require scraping multiple sites in various ways. ez flow when no anti-bot.
    -   Suggestions: [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash), [adv-scrapy-proxies](https://github.com/reanalytics-databoutique/advanced-scrapy-proxies)
-   BS4
    -   Minimal version of Scrapy with only a fraction of the functionality. Good for unstructured HTML pages
    -   Use it for simple projects where all you need to do is scrape the elements of one web page.
    -   Extensions: [MechanicalSoup](https://github.com/MechanicalSoup/MechanicalSoup)
-   [cheerio](https://cheerio.js.org/): Like BS4 but in Javascript
-   [colly](https://github.com/gocolly/colly): Like Bs4 but in Golang, no js rendering.

</div>

<div class="outline-2 smol-table">

### Geo stuff {#geo-stuff}

I am interested in maps because it's crazy how we managed to actually map the real world into some other form and reason about. It's just mind blowing to me. Basically I think it's a [notation](https://github.com/prathyvsh/notation) and [notations](https://github.com/k-qy/notation) are fascinating to me. Also I want to do a lot of geo based visualizations and study.

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Checkout [felt](https://felt.com/about)
-   Lazy Sunday
    -   Check out [Literate Visualization](https://github.com/gicentre/litvis) for I am a sucker for Literate programming
    -   Try out [Every Door](https://every-door.app/) and [StreetComplete](https://streetcomplete.app/?lang=en) and see which one I'd want to use
    -   Check [terra-draw](https://github.com/JamesLMilner/terra-draw)
{{< /lft >}}

{{< coolinks >}}
-   Map services: [mapy.cz](https://en.mapy.cz/)(see [this](https://news.ycombinator.com/item?id=33491697)) | [mapcomplete](https://mapcomplete.osm.be)
-   Helper tools: [OSM filter](https://overpass-turbo.eu/) | [mapshaper](https://mapshaper.org/) | [BBBike extract](https://extract.bbbike.org/)
-   Reference: [Web maps examples](https://maps4html.org/HTML-Map-Element-UseCases-Requirements/examples/create-map.html)
-   Others: [GPSJAM GPS/GNSS Interference Map](https://gpsjam.org/)
{{< /coolinks >}}

-   The [openinfra](https://news.ycombinator.com/item?id=39109185) map is interesting
-   I really need to make a page for all map stuff man

</div>

</div>

<div class="outline-1 smol-table">

## Infra &amp; Network &amp; Security {#infra-and-network-and-security}

<div class="outline-2 smol-table">

### Infrastructure experiments {#infrastructure-experiments}

{{< lft >}}
-   Urgent AF
    -   Haven't played w containers in a while, get upto speed w podman. Also check, [distroless](https://github.com/GoogleContainerTools/distroless) and [slim](https://github.com/slimtoolkit/slim)
    -   Check if I should include [earthly](https://github.com/earthly/earthly) and [ctop](https://github.com/bcicen/ctop) to my workflow, also see [cdebug](https://github.com/iximiuz/cdebug)
    -   Haven't touched k8s in a while, [kubectx &amp; kubens](https://github.com/ahmetb/kubectx), [k9s](https://github.com/derailed/k9s), [lens](https://k8slens.dev/)
-   Sooner the better
    -   Check [tunneling stuff](https://mogoz.geekodour.org/posts/20230429192853-tunneling/)
    -   think useful [k8s-capacity](https://github.com/robscott/kube-capacity), [netshoot](https://github.com/nicolaka/netshoot), [krane](https://github.com/appvia/krane), [kubiscan](https://github.com/cyberark/KubiScan)
    -   I plan to manage my personal infra via [nomad](https://mrkaran.dev/posts/nomad-k8s-showdown/) so need to check that out.
    -   Play w [localstack](https://github.com/localstack/localstack)
    -   I like pipes and glued together scripts but node based automation is probably more useful in certain cases, checkout [n8n](https://news.ycombinator.com/item?id=37274052)
-   Lazy Sunday
    -   [some file sharing](https://mogoz.geekodour.org/posts/20230419105440-file_sharing/) tools
    -   [steampipe](https://github.com/turbot/steampipe) looks interesting, problem is i do not have monie for cloud but would explore, would this work w localstack? hmm.
    -   I currently use goatcounter free on my homepage, but I find it a little rigid for my workflow. I want to checkout alternatives and status pages for my other services etc.
        -   Analytics: [umami](https://umami.is/), [plausible](https://github.com/plausible/analytics), [ping](https://github.com/parkr/ping), [fathom](https://github.com/usefathom/fathom), [shynet](https://github.com/milesmcc/shynet), [analytics](https://github.com/DavidWells/analytics), [offen](https://github.com/offen/offen), [counterscale](https://benv.ca/blog/posts/counterscale-and-the-new-self-hosted)
        -   Status: [uptime-kuma](https://github.com/louislam/uptime-kuma), [vigil](https://github.com/valeriansaliou/vigil), [gatus](https://github.com/TwiN/gatus), [upptime](https://github.com/upptime/upptime)
    -   Hit my stuff w [k6](https://github.com/grafana/k6)
{{< /lft >}}

{{< coolinks >}}
-   Reference: [CPU info](https://www.cpu-world.com) | [GPU info](https://www.techpowerup.com/gpu-specs/) | [CIDR.xyz](https://cidr.xyz/) | [syscall table](https://syscalls.mebeim.net/?table=x86%2F64%2Fx64%2Flatest)
-   Tools: [traefik.me](http://traefik.me/) (xip.io, wildcard dns) | [dns.netmeister.org](https://github.com/jschauma/dns-rrs/)
-   Info: [DOH providers](https://github.com/curl/curl/wiki/DNS-over-HTTPS)
{{< /coolinks >}}

-   Ansible and Github actions are enough for my regular automation
-   See my summary on [Logging](https://mogoz.geekodour.org/posts/20221101183142-logging/)
-   I haven't fiddled with infra stuff in a while but I plan to streamline things eventually.
-   Mostly use github and bitbucket for hosting code repositories
-   Netlify or Vercel for semi-static sites
-   Have not got around selfhosting stuff yet, except locally on my pi/laptop when it makes sense.
-   I mostly use github actions for personal projects, I found that the local runner `act` is only useful for basic things like debugging why some environment variable etc is not getting set, playing around with "contexts" etc. Neat tool when learning.

</div>

<div class="outline-2 smol-table">

### Observability stuff {#observability-stuff}

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Need to check how useful continuous profiling be for my usecases, [parca](https://github.com/parca-dev/parca), [pyroscope](https://github.com/grafana/pyroscope)
    -   Lot of logging tools, some of these I used once or twice but want to do proper check and write a comparison blogpost as a summary maybe and link it back here. [angle-grinder](https://github.com/rcoh/angle-grinder), [logmine](https://github.com/trungdq88/logmine), [rhit](https://github.com/Canop/rhit)(nginx), [goaccess](https://github.com/allinurl/goaccess), [lnav](https://github.com/tstack/lnav), [pidcat](https://github.com/JakeWharton/pidcat)
-   Lazy Sunday
    -   I see so many elastic search alternatives [quickwit](https://github.com/quickwit-oss/quickwit), [sonic](https://github.com/valeriansaliou/sonic), [zinc](https://github.com/zincsearch/zincsearch), [manticore](https://github.com/manticoresoftware/manticoresearch), [toshi](https://github.com/toshi-search/Toshi), [Typesense](https://typesense.org/)
{{< /lft >}}

{{< coolinks >}}
Prometheus references: [exporterhub.io](https://github.com/NexClipper/exporterhub.io) | [promql cheatsheet](https://promlabs.com/promql-cheat-sheet/)  | [promlens(promql explainer)](https://demo.promlens.com/) | [relabel explainer](https://relabeler.promlabs.com/)
{{< /coolinks >}}

</div>

<div class="outline-2 smol-table">

### Security, Network and Tinkering {#security-network-and-tinkering}

{{< lft >}}
-   Urgent AF
    -   Often find myself needing to inspect AF_UNIX, I am not sure how to do it w [socat/tcpdump](https://superuser.com/questions/484671/can-i-monitor-a-local-unix-domain-socket-like-tcpdump) but this one using ebpf looks interesting: [sockdump](https://github.com/mechpen/sockdump)
-   Sooner the better
    -   Check out [assh](https://github.com/moul/assh) for managing ssh stuff
    -   Check [cilium/pwru](https://github.com/cilium/pwru) and [sniffnet](https://github.com/GyulyVGC/sniffnet), also check if [nudin/iptable_vis](https://github.com/Nudin/iptable_vis) does what it says because it'll be so cool.
    -   l7 tcpdump: [netpeek](https://github.com/darshanime/netpeek)
-   Lazy Sunday
    -   Check [sipcalc](https://news.ycombinator.com/item?id=35749594), [trystereo](https://github.com/dmotz/trystero/), [janus](https://janus.conf.meetecho.com/),  [p2pcf](https://github.com/gfodor/p2pcf)
    -   Experiment w [ghidra](https://ghidra-sre.org/), see [notes](https://mogoz.geekodour.org/posts/20230418153328-reverse_engineering/)
    -   These two identification tools look juicy [pywhat](https://github.com/bee-san/pyWhat), [ciphy](https://github.com/Ciphey/Ciphey), [unblob](https://github.com/onekey-sec/unblob).
    -   Check if i need to replace qbittorrent w [tribler](https://github.com/Tribler/tribler), think not.
    -   Want to [up](https://ittavern.com/getting-started-with-nmap/) [my](https://zwischenzugs.com/2018/11/25/six-ways-to-level-up-your-nmap-game/) port [scanning](https://github.com/RustScan/RustScan) [game](https://github.com/v-byte-cpu/sx) and do some experiments [on the](https://github.com/robertdavidgraham/masscan) [web](https://github.com/zmap/zmap).
{{< /lft >}}

{{< coolinks >}}
-   Investigation: [PimEyes](https://pimeyes.com/en) | [Browserleaks](https://browserleaks.com/) | [εxodus android](https://reports.exodus-privacy.eu.org/en/) | [dnsdumpster](https://dnsdumpster.com/)
-   Vulnerabilities: [OSV Database](https://osv.dev/list) | [OpenCVE](https://www.opencve.io/)(signed-in) | [HackerOne Hackactivity](https://hackerone.com/hacktivity/)
-   Tools: [adhoc webhook](https://webhook.site)
-   Reference: [GTFOBins](https://gtfobins.github.io/) | [LOLBAS](https://lolbas-project.github.io/#)
-   Info: [CPU info](https://www.cpu-world.com) | [GPU info](https://www.techpowerup.com/gpu-specs/) | [SLSA](https://slsa.dev/)
-   Visual: [CIDR.xyz](https://cidr.xyz/) | [Virtual x86 WASM](https://copy.sh/v86/)
{{< /coolinks >}}

-   I have a dedicated page called [Plumber Manual]({{< relref "plumber_manual#general" >}}) for things related to this.
-   [vulnix](https://github.com/nix-community/vulnix) is pretty cool, it lists the CVEs for your installed packages and then you can spend hours reading source-code of the dependencies you use and also learn a thing or two about security.

</div>

</div>

<div class="outline-1 smol-table">

## Non-dev {#non-dev}

<div class="outline-2 smol-table">

### Planning/Brainstorming/Curation {#planning-brainstorming-curation}

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Understand [4+1 architectural view model](https://en.wikipedia.org/wiki/4%2B1_architectural_view_model) and [c4model](https://c4model.com/)
-   Lazy Sunday
    -   Try out some [weird](https://natto.dev) [mindmapping](https://markwhen.com/) [like](https://www.mermaidchart.com/blog/posts/sequence-diagrams-the-good-thing-uml-brought-to-software-development) tools. Also check [whimsical](https://whimsical.com/pricing)
    -   Experiment [w](https://johnwickerson.wordpress.com/2019/08/08/block-diagrams/) [idea](https://sketch.systems/) [drawing](https://stately.ai/) [tools](https://xosh.org/text-to-diagram/), [Mermaid](https://mermaid.js.org/) [being](https://bluefishjs.org/) [talked](https://github.com/mingrammer/diagrams) [about](https://github.com/tone-row/flowchart-fun) a lot. Also check [typograms](https://google.github.io/typograms/)
{{< /lft >}}

{{< coolinks >}}
-   Mindmapping: [Kinopio](https://kinopio.club/)
-   Diagramming: [Swimlanes](https://swimlanes.io/), [text-to-diagram-tools-comparision](https://text-to-diagram.com/) 🌟 (maybe selfhost this)
-   Helpful tools: [Loudreader](https://www.loudreader.com/)
{{< /coolinks >}}

-   `org-mode` supremacy, notion and various markdown wiki veteran.
-   I have a page dedicated to [notetaking]({{< relref "notetaking" >}})
-   Github issues and Linear for project progress tracking.
-   Key is to think how to think about the specific problem and choose tools based on that. Meta.

</div>

<div class="outline-2 smol-table">

### Communication and Discussions {#communication-and-discussions}

{{< coolinks >}}
-   Translations: [Words2Emoji](https://www.words2emoji.com/) | [emojikitchen](https://emojikitchen.dev/)
-   Deciding: [dont.build](https://dont.build/) | [Bootstrapping Calculator](https://bootstrappingcalculator.com/)
-   Search: [netsplit](https://netsplit.de/) | [IRC Driven](https://www.ircdriven.com/) | [subredditstats](https://subredditstats.com/subreddit-user-overlaps/slatestarcodex)
{{< /coolinks >}}

-   I have a [communities]({{< relref "communities" >}}) page but I have serious [problems](http://www.catb.org/esr/faqs/smart-questions.html) communicating my thoughts, but that's another story.
-   Chat
    -   Matrix: Element as [the backend](https://akselmo.dev/2022/12/29/How-To-Use-Matrix.html), cinny as the chat ui
    -   IRC: [The Lounge](https://thelounge.chat/) runs locally on my pi
    -   Telegram, WhatsApp, Signal, Discord
-   Email
    -   Gmail, Zoho Mail (K9, Delta Chat) w [SimpleLogin](https://simplelogin.io/)

</div>

<div class="outline-2 smol-table">

### Research {#research}

I have never done any real research but I want to experiment things and write about those this formally. I have some nice stuff in syllabus which I'll move over here when I go through them.

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Check mathpix
-   Lazy Sunday
    -   I've been planning to setup a [nice zotero &amp; org-ref workflow](https://www.reddit.com/r/emacs/comments/vt0otx/using_the_power_of_zotero_in_emacs_orgmode_to/) but I am not an academic and I am not exactly sure how things will play out.
{{< /lft >}}

</div>

<div class="outline-2 smol-table">

### Match &amp; Problem solving {#match-and-problem-solving}

{{< coolinks >}}
-   Calculators: [derivative](https://www.derivative-calculator.net/) | [integral](https://www.integral-calculator.com/)
{{< /coolinks >}}

</div>

</div>

<div class="outline-1 smol-table">

## Misc {#misc}

<div class="outline-2 smol-table">

### Music {#music}

-   <https://chord.rocks>

</div>

<div class="outline-2 smol-table">

### Art/Design {#art-design}

{{< lft >}}
-   Urgent AF
-   Sooner the better
    -   Well, video editors. Long story. Anyway need to check [LosslessCut](https://mifi.no/losslesscut/), [Runway](https://runwayml.com/), [Source Filmmaker](https://store.steampowered.com/app/1840/Source_Filmmaker/), [remotion](https://github.com/remotion-dev/remotion), [FFrames](https://fframes.studio/)
    -   Check [muted](https://muted.io/) and [making videos](https://www.youtube.com/watch?v=yaa13eehgzo&t=1s)
-   Lazy Sunday
    -   Experiment more with MagicaVoxel
    -   Experiment w pixel editors, [rx](https://github.com/cloudhead/rx), [pixelcraft](https://github.com/rgab1508/PixelCraft), [piskel](https://github.com/piskelapp/piskel), [aseprite](https://github.com/aseprite/aseprite)
    -   Try creating some posters with [sharkdp/binocle](https://github.com/sharkdp/binocle) and do some [weird](https://github.com/deepfakes/faceswap) shit
{{< /lft >}}

I wants to do art/design but not at the moment. I also wanted to make weird game videos using assets etc (Neel, if you ever read this, yeah still at it). But I might have to pause that for a while as it does not directly feed into my primary goals but I definitely want to make time for it.

</div>

<div class="outline-2 smol-table">

### Mobile experiments {#mobile-experiments}

{{< lft >}}
-   Urgent AF
-   Sooner the better
-   Lazy Sunday
    -   Some emulation tools I want to try, [remote-android/redroid-doc](https://github.com/remote-android/redroid-doc), [scrcpy](https://news.ycombinator.com/item?id=35749366)
    -   I want to check some apps, see if [this helps](https://github.com/androguard/androguard)
{{< /lft >}}

{{< coolinks >}}
-   Tools: [Mobile JS console](https://eruda.liriliri.io/)
{{< /coolinks >}}

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
| [Sidebery](https://addons.mozilla.org/en-US/firefox/addon/sidebery/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                        | Addon for managing tabs, containers (contextual identities) and bookmarks in sidebar. Supports both flat and tree tabs layouts, per-container include/exclude rules, proxy configs for each container and much more. |
| [Auto Tab Discard](https://addons.mozilla.org/en-US/firefox/addon/auto-tab-discard/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)        | Increase browser speed and reduce memory load when you have numerous open tabs.                                                                                                                                      |
| [Impulse Blocker](https://addons.mozilla.org/en-US/firefox/addon/impulse-blocker/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)          | Block distracting websites when you are browsing the web.                                                                                                                                                            |
| [Imagus](https://addons.mozilla.org/en-US/firefox/addon/imagus/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                            | Enlarge thumbnails, and show images/videos from links with a mouse hover.                                                                                                                                            |
| [Cookie Quick Manager](https://addons.mozilla.org/en-US/firefox/addon/cookie-quick-manager/)                                                                       | An addon to manage (view, search, create, edit, delete, backup, restore) cookies.                                                                                                                                    |
| [What Hacker News Says](https://addons.mozilla.org/en-US/firefox/addon/what-hacker-news-says/)                                                                     | Easily find Hacker News threads about the page you're currently browsing.                                                                                                                                            |
| [WhatFont](https://addons.mozilla.org/en-US/firefox/addon/zjm-whatfont/)                                                                                           | A wrapper for Chengyhin Liu's WhatFont tool                                                                                                                                                                          |
| [Debug CSS](https://addons.mozilla.org/en-US/firefox/addon/pranay-joshi/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)                     | Adds outline to all elements on the page to show the culprit element which is changing desired layout                                                                                                                |
| [Video Speed Controller](https://addons.mozilla.org/en-US/firefox/addon/videospeed/)                                                                               | Speed up, slow down, advance and rewind HTML5 audio/video with shortcuts                                                                                                                                             |
| [Tridactyl](https://addons.mozilla.org/en-US/firefox/addon/tridactyl-vim/)                                                                                         | &lt;nil&gt;                                                                                                                                                                                                          |
| [ClearURLs](https://addons.mozilla.org/en-US/firefox/addon/clearurls/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                      | Remove tracking elements from URLs.                                                                                                                                                                                  |
| [Web Archives](https://addons.mozilla.org/en-US/firefox/addon/view-page-archive/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)           | View archived and cached versions of web pages on 10+ search engines, such as the Wayback Machine, Archive․is, Google, Bing and Yandex                                                                               |
| [Enhancer for YouTube™](https://addons.mozilla.org/en-US/firefox/addon/enhancer-for-youtube/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) | Take control of YouTube and boost your user experience!                                                                                                                                                              |
| [SimpleLogin:Receive &amp; Send emails anonymously](https://addons.mozilla.org/en-US/firefox/addon/simplelogin/)                                                   | Easily create a different email for each website to hide your real email. Protect your inbox against spams, phishing, data breaches                                                                                  |
| [Consent-O-Matic](https://addons.mozilla.org/en-US/firefox/addon/consent-o-matic/)                                                                                 | Automatic handling of GDPR consent forms                                                                                                                                                                             |
| [Violentmonkey](https://addons.mozilla.org/en-US/firefox/addon/violentmonkey/)                                                                                     | An open source userscript manager that supports a lot of browsers                                                                                                                                                    |
| [MarkDownload - Markdown Web Clipper](https://addons.mozilla.org/en-US/firefox/addon/markdownload/)                                                                | This extension works like a web clipper, but it downloads articles in markdown format.                                                                                                                               |
| [Smart TOC](https://addons.mozilla.org/en-US/firefox/addon/smart_toc/)                                                                                             | Webpage outliner                                                                                                                                                                                                     |
| [Dark Reader](https://addons.mozilla.org/en-US/firefox/addon/darkreader/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                   | Dark mode for every website. Take care of your eyes, use dark theme for night and daily browsing.                                                                                                                    |
| [Hello, Goodbye](https://addons.mozilla.org/en-US/firefox/addon/hello-goodbye/)                                                                                    | Hello, Goodbye blocks annoying chat widgets.                                                                                                                                                                         |
| [I don't care about cookies](https://addons.mozilla.org/en-US/firefox/addon/i-dont-care-about-cookies/)                                                            | &lt;nil&gt;                                                                                                                                                                                                          |
| [Tab Stash](https://addons.mozilla.org/en-US/firefox/addon/tab-stash/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=homepage-primary-hero)         | A no-fuss way to save and restore batches of tabs as bookmarks.                                                                                                                                                      |
| [Library Extension](https://addons.mozilla.org/en-US/firefox/addon/libraryextension/)                                                                              | &lt;nil&gt;                                                                                                                                                                                                          |
| [Stylus](https://addons.mozilla.org/en-US/firefox/addon/styl-us/)                                                                                                  | Redesign the web with Stylus, a user styles manager. Stylus allows you to easily install themes and skins for many popular sites.                                                                                    |
| [React Developer Tools](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search)       | Adds React debugging tools to the Firefox Developer Tools.Created from revision 2468a8735 on 5/19/2023.                                                                                                              |
| [Reddit Enhancement Suite](https://addons.mozilla.org/en-US/firefox/addon/reddit-enhancement-suite/)                                                               | A suite of modules that enhance your Reddit browsing experience                                                                                                                                                      |
| [Emoji](https://addons.mozilla.org/en-US/firefox/addon/emoji-sav/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                          | Insert emojis using a web browser, and customise the experience and the add-on in Settings.                                                                                                                          |
| [SponsorBlock for YouTube - Skip Sponsorships](https://addons.mozilla.org/en-US/firefox/addon/sponsorblock/)                                                       | Skip sponsorships, subscription begging and more on YouTube videos. Report sponsors on videos you watch to save others' time.                                                                                        |
| [Refined GitHub](https://addons.mozilla.org/en-US/firefox/addon/refined-github-/)                                                                                  | Simplifies the GitHub interface and adds useful features                                                                                                                                                             |
| [Control Panel for Twitter](https://addons.mozilla.org/en-US/firefox/addon/tweak-new-twitter/)                                                                     | Gives you more control over Twitter and adds missing features and UI improvements                                                                                                                                    |
| [Flagfox](https://addons.mozilla.org/en-US/firefox/addon/flagfox/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=featured)                          | Displays a flag depicting the location of the current server                                                                                                                                                         |
| [LocalCDN](https://addons.mozilla.org/en-US/firefox/addon/localcdn-fork-of-decentraleyes/)                                                                         | Protects you against tracking through CDNs (Content Delivery Networks) by redirecting to local resources.                                                                                                            |
| [Bitwarden - Free Password Manager](https://addons.mozilla.org/en-US/firefox/addon/bitwarden-password-manager/)                                                    | A secure and free password manager for all of your devices.                                                                                                                                                          |
| [uBlacklist](https://addons.mozilla.org/en-US/firefox/addon/ublacklist/)                                                                                           | Blocks sites you specify from appearing in Google search results                                                                                                                                                     |
| [Zotero Connector](https://www.zotero.org/download/connectors)                                                                                                     | Save references to Zotero from your web browser                                                                                                                                                                      |
| [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)                                                                                     | Finally, an efficient blocker. Easy on CPU and memory.                                                                                                                                                               |

</div>

<div class="outline-2 smol-table">

### Arch Official Packages {#arch-official-packages}

| Name                                                                                                      | Description                                                                                                    |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [adobe-source-han-sans-jp-fonts](https://github.com/adobe-fonts/source-han-sans)                          | Adobe Source Han Sans Subset OTF - Japanese OpenType/CFF fonts                                                 |
| [age](https://github.com/FiloSottile/age)                                                                 | A simple, modern and secure file encryption tool                                                               |
| [aircrack-ng](https://www.aircrack-ng.org)                                                                | Key cracker for the 802.11 WEP and WPA-PSK protocols                                                           |
| [alacritty](https://github.com/alacritty/alacritty)                                                       | A cross-platform, GPU-accelerated terminal emulator                                                            |
| [alsa-utils](https://www.alsa-project.org)                                                                | Advanced Linux Sound Architecture - Utilities                                                                  |
| [ansible](https://pypi.org/project/ansible/)                                                              | Official assortment of Ansible collections                                                                     |
| [ansible-lint](https://github.com/ansible/ansible-lint)                                                   | Checks playbooks for practices and behaviour that could potentially be improved.                               |
| [arandr](https://christian.amsuess.com/tools/arandr/)                                                     | Provide a simple visual front end for XRandR 1.2.                                                              |
| [atop](https://www.atoptool.nl/)                                                                          | A system and process level monitor                                                                             |
| [bandwhich](https://github.com/imsnif/bandwhich)                                                          | Terminal bandwidth utilization tool                                                                            |
| [base](https://www.archlinux.org)                                                                         | Minimal package set to define a basic Arch Linux installation                                                  |
| [base-devel](https://www.archlinux.org)                                                                   | Basic tools to build Arch Linux packages                                                                       |
| [bash-language-server](https://github.com/bash-lsp/bash-language-server)                                  | Bash language server implementation based on Tree Sitter and its grammar for Bash                              |
| [bat](https://github.com/sharkdp/bat)                                                                     | Cat clone with syntax highlighting and git integration                                                         |
| [beep](https://github.com/spkr-beep/beep)                                                                 | Advanced PC speaker beeping program                                                                            |
| [biber](https://github.com/plk/biber)                                                                     | A Unicode-capable BibTeX replacement for biblatex users                                                        |
| [bluez-utils](http://www.bluez.org/)                                                                      | Development and debugging utilities for the bluetooth protocol stack                                           |
| [bmon](https://github.com/tgraf/bmon/)                                                                    | Portable bandwidth monitor and rate estimator                                                                  |
| [bottom](https://github.com/ClementTsang/bottom)                                                          | A graphical process/system monitor                                                                             |
| [bpftrace](https://github.com/iovisor/bpftrace)                                                           | High-level tracing language for Linux eBPF                                                                     |
| [brightnessctl](https://github.com/Hummer12007/brightnessctl)                                             | Lightweight brightness control tool                                                                            |
| [catimg](https://github.com/posva/catimg)                                                                 | Print images in a terminal with 256 colors support                                                             |
| [cgasm](https://github.com/bnagy/cgasm)                                                                   | CLI tool for browsing documentation for x86 Assembly                                                           |
| [chafa](https://hpjansson.org/chafa/)                                                                     | Image-to-text converter supporting a wide range of symbols and palettes, transparency, animations, etc.        |
| [cloudflared](https://github.com/cloudflare/cloudflared)                                                  | Command-line client for Cloudflare Tunnel                                                                      |
| [cmake](https://www.cmake.org/)                                                                           | A cross-platform open-source make system                                                                       |
| [cmus](https://cmus.github.io/)                                                                           | Feature-rich ncurses-based music player                                                                        |
| [cool-retro-term](https://github.com/Swordfish90/cool-retro-term)                                         | A good looking terminal emulator which mimics the old cathode display                                          |
| [cowsay](https://web.archive.org/web/20120225123719/http://www.nog.net/~tony/warez/cowsay.shtml)          | Configurable talking cow (and a few other creatures)                                                           |
| [curlie](https://curlie.io)                                                                               | The power of curl, the ease of use of httpie.                                                                  |
| [dbeaver](https://dbeaver.io/)                                                                            | Free universal SQL Client for developers and database administrators (community edition)                       |
| [diffoscope](https://diffoscope.org/)                                                                     | Tool for in-depth comparison of files, archives, and directories                                               |
| [discord](https://discord.com)                                                                            | All-in-one voice and text chat for gamers                                                                      |
| [dive](https://github.com/wagoodman/dive)                                                                 | A tool for exploring layers in a docker image                                                                  |
| [dog](https://github.com/ogham/dog)                                                                       | Command-line DNS client like dig                                                                               |
| [dstat](http://dag.wieers.com/home-made/dstat/)                                                           | A versatile resource statistics tool                                                                           |
| [dua-cli](https://github.com/Byron/dua-cli)                                                               | A tool to conveniently learn about the disk usage of directories, fast!                                        |
| [duf](https://github.com/muesli/duf)                                                                      | Disk Usage/Free Utility                                                                                        |
| [earlyoom](https://github.com/rfjakob/earlyoom)                                                           | Early OOM Daemon for Linux                                                                                     |
| [ebook-tools](https://sourceforge.net/projects/ebook-tools/)                                              | Tools for accessing and converting various ebook file formats                                                  |
| [editorconfig-core-c](https://github.com/editorconfig/editorconfig-core-c)                                | EditorConfig core code written in C (for use by plugins supporting EditorConfig parsing)                       |
| [element-desktop](https://element.io)                                                                     | Glossy Matrix collaboration client — desktop version.                                                          |
| [emacs-nativecomp](https://www.gnu.org/software/emacs/emacs.html)                                         | The extensible, customizable, self-documenting real-time display editor with native compilation enabled        |
| [entr](http://eradman.com/entrproject)                                                                    | Run arbitrary commands when files change                                                                       |
| [eva](https://github.com/nerdypepper/eva)                                                                 | simple calculator REPL, similar to bc(1)                                                                       |
| [evtest](https://cgit.freedesktop.org/evtest/)                                                            | Input device event monitor and query tool                                                                      |
| [eza](https://github.com/eza-community/eza)                                                               | A modern replacement for ls (community fork of exa)                                                            |
| [fd](https://github.com/sharkdp/fd)                                                                       | Simple, fast and user-friendly alternative to find                                                             |
| [feh](https://feh.finalrewind.org/)                                                                       | Fast and light imlib2-based image viewer                                                                       |
| [figlet](http://www.figlet.org/)                                                                          | A program for making large letters out of ordinary text                                                        |
| [firefox](https://www.mozilla.org/firefox/)                                                               | Standalone web browser from mozilla.org                                                                        |
| [fish](https://fishshell.com/)                                                                            | Smart and user friendly shell intended mostly for interactive use                                              |
| [gfold](https://github.com/nickgerace/gfold)                                                              | A CLI tool to help keep track of Git repositories                                                              |
| [ghidra](https://ghidra-sre.org/)                                                                         | Software reverse engineering framework                                                                         |
| [gimp](https://www.gimp.org/)                                                                             | GNU Image Manipulation Program                                                                                 |
| [git-delta](https://github.com/dandavison/delta)                                                          | Syntax-highlighting pager for git and diff output                                                              |
| [glances](https://nicolargo.github.io/glances/)                                                           | CLI curses-based monitoring tool                                                                               |
| [glow](https://github.com/charmbracelet/glow)                                                             | Command-line markdown renderer                                                                                 |
| [gnu-netcat](http://netcat.sourceforge.net/)                                                              | GNU rewrite of netcat, the network piping application                                                          |
| [gopls](https://github.com/golang/tools/tree/master/gopls)                                                | Language server for Go programming language                                                                    |
| [gping](https://github.com/orf/gping)                                                                     | Ping, but with a graph                                                                                         |
| [grex](https://github.com/pemistahl/grex)                                                                 | A command-line tool for generating regular expressions from user-provided input strings                        |
| [grim](https://git.sr.ht/~emersion/grim)                                                                  | Screenshot utility for Wayland                                                                                 |
| [heaptrack](http://milianw.de/tag/heaptrack)                                                              | A heap memory profiler for Linux                                                                               |
| [hexyl](https://github.com/sharkdp/hexyl)                                                                 | Colored command-line hex viewer                                                                                |
| [htop](https://htop.dev/)                                                                                 | Interactive process viewer                                                                                     |
| [httrack](https://www.httrack.com/)                                                                       | An easy-to-use offline browser utility                                                                         |
| [hugo](https://gohugo.io/)                                                                                | Fast and Flexible Static Site Generator in Go                                                                  |
| [hunspell-en_us](http://wordlist.aspell.net/dicts/)                                                       | US English hunspell dictionaries                                                                               |
| [hyperfine](https://github.com/sharkdp/hyperfine)                                                         | A command-line benchmarking tool                                                                               |
| [imv](https://sr.ht/~exec64/imv/)                                                                         | Image viewer for Wayland and X11                                                                               |
| [intel-ucode](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files)                        | Microcode update files for Intel CPUs                                                                          |
| [inter-font](https://github.com/rsms/inter/)                                                              | A typeface specially designed for user interfaces                                                              |
| [interception-dual-function-keys](https://gitlab.com/interception/linux/plugins/dual-function-keys)       | Interception plugin for dual-function keys: Tap for one key, hold for another                                  |
| [iotop](http://guichaz.free.fr/iotop/)                                                                    | View I/O usage of processes                                                                                    |
| [iwd](https://git.kernel.org/cgit/network/wireless/iwd.git/)                                              | Internet Wireless Daemon                                                                                       |
| [jedi-language-server](https://github.com/pappasam/jedi-language-server)                                  | Language server for Jedi                                                                                       |
| [john](https://www.openwall.com/john)                                                                     | John the Ripper password cracker                                                                               |
| [keychain](https://www.funtoo.org/Keychain)                                                               | A front-end to ssh-agent, allowing one long-running ssh-agent process per system, rather than per login        |
| [kismet](https://www.kismetwireless.net/)                                                                 | 802.11 layer2 wireless network detector, sniffer, and intrusion detection system                               |
| [kmon](https://github.com/orhun/kmon)                                                                     | Linux kernel manager and activity monitor                                                                      |
| [libmicrodns](https://github.com/videolabs/libmicrodns)                                                   | Minimal mDNS resolver library                                                                                  |
| [libreoffice-still](https://www.libreoffice.org/)                                                         | LibreOffice maintenance branch                                                                                 |
| [linux-firmware](https://git.kernel.org/?p=linux/kernel/git/firmware/linux-firmware.git)                  | Firmware files for Linux                                                                                       |
| [lnav](http://lnav.org/)                                                                                  | A curses-based tool for viewing and analyzing log files                                                        |
| [lolcat](https://github.com/busyloop/lolcat)                                                              | Okay, no unicorns. But rainbows!!                                                                              |
| [lostfiles](https://github.com/graysky2/lostfiles)                                                        | Find orphaned files not owned by any Arch packages                                                             |
| [lshw](https://ezix.org/project/wiki/HardwareLiSter)                                                      | A small tool to provide detailed information on the hardware configuration of the machine.                     |
| [lsof](https://github.com/lsof-org/lsof)                                                                  | Lists open files for running Unix processes                                                                    |
| [ltrace](https://www.ltrace.org/)                                                                         | Tracks runtime library calls in dynamically linked programs                                                    |
| [lxd](https://ubuntu.com/lxd)                                                                             | Daemon based on liblxc offering a REST API to manage containers                                                |
| [macchanger](https://www.gnu.org/software/macchanger)                                                     | A small utility to change your NIC's MAC address                                                               |
| [maim](https://github.com/naelstrof/maim)                                                                 | Utility to take a screenshot using imlib2                                                                      |
| [mako](https://mako-project.org)                                                                          | Lightweight notification daemon for Wayland                                                                    |
| [man-db](https://gitlab.com/man-db/man-db)                                                                | A utility for reading man pages                                                                                |
| [man-pages](https://www.kernel.org/doc/man-pages/)                                                        | Linux man pages                                                                                                |
| [mediainfo](https://mediaarea.net)                                                                        | Supplies technical and tag information about media files (CLI interface)                                       |
| [miller](https://github.com/johnkerl/miller)                                                              | Name-indexed data processing tool                                                                              |
| [mold](https://github.com/rui314/mold)                                                                    | A Modern Linker                                                                                                |
| [mpv](https://mpv.io/)                                                                                    | a free, open source, and cross-platform media player                                                           |
| [nasm](https://www.nasm.us)                                                                               | 80x86 assembler designed for portability and modularity                                                        |
| [neofetch](https://github.com/dylanaraps/neofetch)                                                        | A CLI system information tool written in BASH that supports displaying images.                                 |
| [neovim](https://neovim.io)                                                                               | Fork of Vim aiming to improve user experience, plugins, and GUIs                                               |
| [nethogs](https://github.com/raboof/nethogs)                                                              | A net top tool which displays traffic used per process instead of per IP or interface                          |
| [nfs-utils](http://nfs.sourceforge.net)                                                                   | Support programs for Network File Systems                                                                      |
| [ngrep](https://github.com/jpr5/ngrep/)                                                                   | A grep-like utility that allows you to search for network packets on an interface.                             |
| [nix](https://nixos.org/nix)                                                                              | A purely functional package manager                                                                            |
| [nmap](https://nmap.org/)                                                                                 | Utility for network discovery and security auditing                                                            |
| [noto-fonts-cjk](https://www.google.com/get/noto/)                                                        | Google Noto CJK fonts                                                                                          |
| [ntfs-3g](https://www.tuxera.com/community/open-source-ntfs-3g/)                                          | NTFS filesystem driver and utilities                                                                           |
| [nyancat](https://nyancat.dakko.us/)                                                                      | Nyancat rendered in your terminal.                                                                             |
| [obs-studio](https://obsproject.com)                                                                      | Free, open source software for live streaming and recording                                                    |
| [okular](https://apps.kde.org/okular/)                                                                    | Document Viewer                                                                                                |
| [ollama](https://github.com/jmorganca/ollama)                                                             | Create, run and share large language models (LLMs)                                                             |
| [onefetch](https://github.com/o2sh/onefetch)                                                              | Git repository summary on your terminal                                                                        |
| [opam](https://opam.ocaml.org/)                                                                           | OCaml package manager                                                                                          |
| [opensnitch](https://github.com/evilsocket/opensnitch)                                                    | A GNU/Linux application firewall                                                                               |
| [pacman-contrib](https://gitlab.archlinux.org/pacman/pacman-contrib)                                      | Contributed scripts and tools for pacman systems                                                               |
| [pacutils](https://github.com/andrewgregory/pacutils)                                                     | Helper tools for libalpm                                                                                       |
| [paperkey](https://www.jabberwocky.com/software/paperkey/)                                                | Archive OpenPGP keys on paper                                                                                  |
| [parallel](https://www.gnu.org/software/parallel/)                                                        | A shell tool for executing jobs in parallel                                                                    |
| [pass](https://www.passwordstore.org/)                                                                    | Stores, retrieves, generates, and synchronizes passwords securely                                              |
| [pdfarranger](https://github.com/pdfarranger/pdfarranger)                                                 | Helps merge or split PDF documents and rotate, crop and rearrange pages                                        |
| [perl-file-mimeinfo](https://metacpan.org/release/File-MimeInfo)                                          | Determine file type, includes mimeopen and mimetype                                                            |
| [perl-image-exiftool](https://exiftool.org/)                                                              | Reader and rewriter of EXIF information that supports raw files                                                |
| [pgformatter](https://github.com/darold/pgformatter)                                                      | A PostgreSQL SQL syntax beautifier                                                                             |
| [pipewire-alsa](https://pipewire.org)                                                                     | Low-latency audio/video router and processor - ALSA configuration                                              |
| [pipewire-pulse](https://pipewire.org)                                                                    | Low-latency audio/video router and processor - PulseAudio replacement                                          |
| [podman](https://github.com/containers/podman)                                                            | Tool and library for running OCI-based containers in pods                                                      |
| [postgresql](https://www.postgresql.org/)                                                                 | Sophisticated object-relational DBMS                                                                           |
| [prettier](https://prettier.io/)                                                                          | An opinionated code formatter for JS, JSON, CSS, YAML and much more                                            |
| [procs](https://github.com/dalance/procs)                                                                 | A modern replacement for ps written in Rust                                                                    |
| [progress](https://github.com/Xfennec/progress)                                                           | Shows running coreutils basic commands and displays stats                                                      |
| [pueue](https://github.com/nukesor/pueue)                                                                 | A CLI tool for managing long running shell commands                                                            |
| [pv](https://www.ivarch.com/programs/pv.shtml)                                                            | A terminal-based tool for monitoring the progress of data through a pipeline                                   |
| [python-isort](https://github.com/PyCQA/isort)                                                            | A Python utility / library to sort Python imports                                                              |
| [python-pipx](https://github.com/pipxproject/pipx)                                                        | Install and Run Python Applications in Isolated Environments                                                   |
| [python-pynvim](https://github.com/neovim/pynvim)                                                         | Python client for Neovim                                                                                       |
| [qbittorrent](https://www.qbittorrent.org)                                                                | An advanced BitTorrent client programmed in C++, based on Qt toolkit and libtorrent-rasterbar                  |
| [qrencode](https://fukuchi.org/works/qrencode/)                                                           | C library for encoding data in a QR Code symbol.                                                               |
| [refind](https://www.rodsbooks.com/refind/)                                                               | An EFI boot manager                                                                                            |
| [reflector](https://xyne.dev/projects/reflector)                                                          | A Python 3 module and script to retrieve and filter the latest Pacman mirror list.                             |
| [ripgrep-all](https://github.com/phiresky/ripgrep-all)                                                    | rga: ripgrep, but also search in PDFs, E-Books, Office documents, zip, tar.gz, etc.                            |
| [rust-analyzer](https://rust-analyzer.github.io/)                                                         | Rust compiler front-end for IDEs                                                                               |
| [sad](https://github.com/ms-jpq/sad)                                                                      | Space Age seD                                                                                                  |
| [scrcpy](https://github.com/Genymobile/scrcpy)                                                            | Display and control your Android device                                                                        |
| [sd](https://github.com/chmln/sd)                                                                         | Intuitive find &amp; replace                                                                                   |
| [shellcheck](https://www.shellcheck.net)                                                                  | Shell script analysis tool                                                                                     |
| [shellharden](https://github.com/anordal/shellharden)                                                     | Bash linter and syntax highlighter                                                                             |
| [shfmt](https://github.com/mvdan/sh)                                                                      | Format shell programs                                                                                          |
| [slurp](https://github.com/emersion/slurp)                                                                | Select a region in a Wayland compositor                                                                        |
| [smartmontools](http://smartmontools.sourceforge.net)                                                     | Control and monitor S.M.A.R.T. enabled ATA and SCSI Hard Drives                                                |
| [sniffnet](https://github.com/GyulyVGC/sniffnet)                                                          | Application to comfortably monitor your network traffic                                                        |
| [ssh-audit](https://github.com/jtesta/ssh-audit)                                                          | SSH configuration auditing                                                                                     |
| [sshfs](https://github.com/libfuse/sshfs)                                                                 | FUSE client based on the SSH File Transfer Protocol                                                            |
| [starship](https://starship.rs/)                                                                          | The cross-shell prompt for astronauts                                                                          |
| [strace](https://strace.io/)                                                                              | A diagnostic, debugging and instructional userspace tracer                                                     |
| [streamlink](https://streamlink.github.io/)                                                               | CLI program that launches streams from various streaming services in a custom video player (livestreamer fork) |
| [svelte-language-server](https://github.com/sveltejs/language-tools/tree/master/packages/language-server) | Language server for Svelte                                                                                     |
| [swappy](https://github.com/jtheoof/swappy)                                                               | A Wayland native snapshot editing tool                                                                         |
| [sway](https://swaywm.org/)                                                                               | Tiling Wayland compositor and replacement for the i3 window manager                                            |
| [swayidle](https://github.com/swaywm/swayidle)                                                            | Idle management daemon for Wayland                                                                             |
| [swaylock](https://github.com/swaywm/swaylock)                                                            | Screen locker for Wayland                                                                                      |
| [syncthing](https://syncthing.net/)                                                                       | Open Source Continuous Replication / Cluster Synchronization Thing                                             |
| [sysstat](http://pagesperso-orange.fr/sebastien.godard/)                                                  | a collection of performance monitoring tools (iostat,isag,mpstat,pidstat,sadf,sar)                             |
| [tailscale](https://tailscale.com)                                                                        | A mesh VPN that makes it easy to connect your devices, wherever they are.                                      |
| [tcpdump](https://www.tcpdump.org/)                                                                       | Powerful command-line packet analyzer                                                                          |
| [tcpflow](https://github.com/simsong/tcpflow)                                                             | Captures data transmitted as part of TCP connections then stores the data conveniently                         |
| [tectonic](https://tectonic-typesetting.github.io/)                                                       | Modernized, complete, self-contained TeX/LaTeX engine, powered by XeTeX and TeXLive                            |
| [telegram-desktop](https://desktop.telegram.org/)                                                         | Official Telegram Desktop client                                                                               |
| [termshark](https://github.com/gcla/termshark)                                                            | Terminal UI for tshark, inspired by Wireshark                                                                  |
| [texlive-fontsrecommended](http://tug.org/texlive/)                                                       | TeX Live - Recommended fonts                                                                                   |
| [texlive-latexextra](http://tug.org/texlive/)                                                             | TeX Live - LaTeX additional packages                                                                           |
| [texlive-plaingeneric](http://tug.org/texlive/)                                                           | TeX Live - Plain (La)TeX packages                                                                              |
| [texlive-xetex](http://tug.org/texlive/)                                                                  | TeX Live - XeTeX and packages                                                                                  |
| [thunderbird](https://www.thunderbird.net/)                                                               | Standalone mail and news reader from mozilla.org                                                               |
| [tmux](https://github.com/tmux/tmux/wiki)                                                                 | Terminal multiplexer                                                                                           |
| [tokei](https://github.com/XAMPPRocky/tokei)                                                              | A blazingly fast CLOC (Count Lines Of Code) program                                                            |
| [traceroute](http://traceroute.sourceforge.net/)                                                          | Tracks the route taken by packets over an IP network                                                           |
| [trash-cli](https://github.com/andreafrancia/trash-cli)                                                   | Command line trashcan (recycle bin) interface                                                                  |
| [ttf-firacode-nerd](https://github.com/ryanoasis/nerd-fonts)                                              | Patched font Fira (Fura) Code from nerd fonts library                                                          |
| [ttf-jetbrains-mono-nerd](https://github.com/ryanoasis/nerd-fonts)                                        | Patched font JetBrains Mono from nerd fonts library                                                            |
| [typescript-language-server](https://github.com/typescript-language-server/typescript-language-server)    | Language Server Protocol (LSP) implementation for TypeScript using tsserver                                    |
| [unarchiver](https://github.com/MacPaw/XADMaster)                                                         | unar and lsar: Objective-C tools for uncompressing archive files                                               |
| [up](https://github.com/akavel/up)                                                                        | A tool for writing Linux pipes with instant live preview                                                       |
| [usbip](https://www.kernel.org)                                                                           | An USB device sharing system over IP network                                                                   |
| [vi](https://ex-vi.sourceforge.net/)                                                                      | The original ex/vi text editor                                                                                 |
| [virtualbox](https://virtualbox.org/)                                                                     | Powerful x86 virtualization for enterprise as well as home use                                                 |
| [visidata](https://www.visidata.org)                                                                      | Terminal spreadsheet multitool for discovering and arranging data                                              |
| [wavemon](https://github.com/uoaerg/wavemon)                                                              | Ncurses-based monitoring application for wireless network devices                                              |
| [waybar](https://github.com/Alexays/Waybar/)                                                              | Highly customizable Wayland bar for Sway and Wlroots based compositors                                         |
| [webhook](https://github.com/adnanh/webhook)                                                              | A lightweight incoming webhook server to run shell commands                                                    |
| [websocat](https://github.com/vi/websocat/)                                                               | Command-line client for web sockets, like netcat/curl/socat for ws://                                          |
| [whois](https://github.com/rfc1036/whois)                                                                 | Intelligent WHOIS client                                                                                       |
| [wireshark-qt](https://www.wireshark.org/)                                                                | Network traffic and protocol analyzer/sniffer - Qt GUI                                                         |
| [xdg-desktop-portal-wlr](https://github.com/emersion/xdg-desktop-portal-wlr)                              | xdg-desktop-portal backend for wlroots                                                                         |
| [xorg-xwayland](https://xorg.freedesktop.org)                                                             | run X clients under wayland                                                                                    |
| [yadm](https://github.com/TheLocehiliosan/yadm)                                                           | Yet Another Dotfiles Manager                                                                                   |
| [yaml-language-server](https://github.com/redhat-developer/yaml-language-server)                          | YAML Language Server                                                                                           |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp)                                                                | A youtube-dl fork with additional features and fixes                                                           |
| [zathura-pdf-mupdf](https://pwmt.org/projects/zathura-pdf-mupdf/)                                         | PDF support for Zathura (MuPDF backend) (Supports PDF, ePub, and OpenXPS)                                      |
| [zbar](https://github.com/mchehab/zbar)                                                                   | Application and library for reading bar codes from various sources                                             |
| [zoxide](https://github.com/ajeetdsouza/zoxide)                                                           | A smarter cd command for your terminal                                                                         |

</div>

<div class="outline-2 smol-table">

### Arch AUR Packages {#arch-aur-packages}

| Name                                                                                               | Description                                                                                                                                               |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [advcpmv](https://github.com/jarun/advcpmv)                                                        | 'cp' and 'mv' utilities with progress bar patches                                                                                                         |
| [ancient-packages](http://public.files.xavion.name/Software/ancient-packages/ancient-packages.jpg) | Lists installed packages no longer available (anywhere)                                                                                                   |
| [anki-bin](https://apps.ankiweb.net/)                                                              | Helps you remember facts (like words/phrases in a foreign language) efficiently. Installed with wheel.                                                    |
| [asdf-vm](https://asdf-vm.com)                                                                     | Extendable version manager with support for Ruby, Node.js, Elixir, Erlang &amp; more                                                                      |
| [cbonsai](https://gitlab.com/jallbrit/cbonsai)                                                     | A bonsai tree generator, written in C using ncurses                                                                                                       |
| [chars](https://github.com/antifuchs/chars)                                                        | Command line tool to display information about unicode characters.                                                                                        |
| [cheat](https://github.com/cheat/cheat)                                                            | Allows you to create and view interactive cheatsheets on the command-line                                                                                 |
| [choose-rust-git](https://github.com/theryangeary/choose)                                          | A fast, human-friendly alternative to awk(1) and cut(1)                                                                                                   |
| [cinny-desktop-bin](https://cinny.in/)                                                             | Matrix client focusing primarily on a simple, elegant and secure interface (binary release)                                                               |
| [clipman](https://github.com/yory8/clipman)                                                        | A simple clipboard manager for Wayland                                                                                                                    |
| [code-minimap](https://github.com/wfxr/code-minimap)                                               | A high performance code minimap render                                                                                                                    |
| [cpufetch](https://github.com/Dr-Noob/cpufetch)                                                    | Simple yet fancy CPU architecture fetching tool                                                                                                           |
| [dasel](https://github.com/TomWright/dasel)                                                        | Query and update data structures from the command line.                                                                                                   |
| [desed](https://github.com/soptikha2/desed)                                                        | Debugger for sed, written in rust. Step through code and observe sed inner state.                                                                         |
| [electron19](https://electronjs.org/)                                                              | Build cross platform desktop apps with web technologies                                                                                                   |
| [elfcat](https://github.com/ruslashev/elfcat)                                                      | Generates HTML files from ELF binaries                                                                                                                    |
| [fclones-bin](https://github.com/pkolaczk/fclones)                                                 | Efficient Duplicate File Finder                                                                                                                           |
| [firefox-tridactyl-native](https://github.com/tridactyl/tridactyl)                                 | Tridactyl native messaging host application for Firefox (native: 0.3.6)                                                                                   |
| [frangipanni](https://github.com/birchb1024/frangipanni)                                           | Program to convert lines of text into a tree structure                                                                                                    |
| [gallery-dl](https://github.com/mikf/gallery-dl)                                                   | Command-line program to download image-galleries and collections from several image hosting sites                                                         |
| [gomi](https://github.com/b4b4r07/gomi)                                                            | Rm alternative written in Go                                                                                                                              |
| [google-chrome](https://www.google.com/chrome)                                                     | The popular web browser by Google (Stable Channel)                                                                                                        |
| [graphtage](https://github.com/trailofbits/graphtage)                                              | A utility for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, and CSS files.                                      |
| [hostctl](https://github.com/guumaster/hostctl)                                                    | Command-line tool to manage your hosts file                                                                                                               |
| [hr-bash](https://github.com/LuRsT/hr)                                                             | A horizontal ruler for your terminal                                                                                                                      |
| [httpstat-go](https://github.com/davecheney/httpstat)                                              | It's like curl -v, with colours.                                                                                                                          |
| [ijq](https://git.sr.ht/~gpanders/ijq)                                                             | Interactive jq tool, like jqplay for the commandline                                                                                                      |
| [imgp](https://github.com/jarun/imgp)                                                              | Multi-core batch image resizer and rotator                                                                                                                |
| [insomnia-bin](https://insomnia.rest)                                                              | API Client and Design Platform for GraphQL and REST                                                                                                       |
| [libtree](https://github.com/haampie/libtree)                                                      | ldd as a tree                                                                                                                                             |
| [loggedfs-git](https://rflament.github.io/loggedfs/)                                               | Filesystem monitoring with Fuse                                                                                                                           |
| [nnn-nerd](https://github.com/jarun/nnn)                                                           | The fastest terminal file manager ever written (with icon support using a patched nerd font).                                                             |
| [nwg-look-bin](https://github.com/nwg-piotr/nwg-look)                                              | GTK3 settings editor adapted to work w/ wlroots-based compositors (binary package)                                                                        |
| [pacgraph](http://kmkeen.com/pacgraph/)                                                            | Draws a graph of installed packages to PNG/SVG/GUI/console. Good for finding bloat.                                                                       |
| [paru](https://github.com/morganamilo/paru)                                                        | Feature packed AUR helper                                                                                                                                 |
| [pmount](http://pmount.alioth.debian.org/)                                                         | mount removable devices as normal user                                                                                                                    |
| [podman-tui](https://github.com/containers/podman-tui)                                             | Podman Terminal User Interface                                                                                                                            |
| [procdump](https://github.com/Sysinternals/ProcDump-for-Linux)                                     | Generate coredumps based off performance triggers                                                                                                         |
| [programmer-calculator](https://github.com/alt-romes/programmer-calculator)                        | A command line calculator made for programmers working with multiple number representations and close to the bits                                         |
| [ps_mem](https://github.com/pixelb/ps_mem)                                                         | List processes by memory usage                                                                                                                            |
| [quickemu](https://github.com/quickemu-project/quickemu)                                           | Quickly create and run optimised Windows, macOS and Linux desktop virtual machines.                                                                       |
| [sampler](https://sampler.dev)                                                                     | A tool for shell commands execution, visualization and alerting. Configured with a simple YAML file.                                                      |
| [sftpgo-bin](https://github.com/drakkan/sftpgo)                                                    | Fully featured and highly configurable SFTP server with optional HTTP, FTP/S and WebDAV support. It can serve local filesystem, S3, GCS, Azure Blob, SFTP |
| [sfz](https://github.com/weihanglo/sfz)                                                            | A simple static file server                                                                                                                               |
| [sshping](https://github.com/spook/sshping)                                                        | ssh-based ping: measure character-echo latency and bandwidth for an interactive ssh session                                                               |
| [sysz](https://github.com/joehillen/sysz)                                                          | fzf terminal UI for systemctl                                                                                                                             |
| [teip](https://github.com/greymd/teip)                                                             | Highly efficient "Masking tape" for standard input                                                                                                        |
| [tsukae-git](https://github.com/irevenko/tsukae)                                                   | Show off your most used shell commands                                                                                                                    |
| [ttf-twemoji](https://github.com/twitter/twemoji)                                                  | Twitter Color Emoji for everyone.                                                                                                                         |
| [typiskt](https://github.com/budlabs/typiskt)                                                      | touchtype training in the terminal                                                                                                                        |
| [tz](https://github.com/oz/tz)                                                                     | A time zone helper                                                                                                                                        |
| [vale](https://github.com/errata-ai/vale)                                                          | A customizable, syntax-aware linter for prose                                                                                                             |
| [vlc-pause-click-plugin](https://github.com/nurupo/vlc-pause-click-plugin)                         | Plugin for VLC that pauses/plays video on mouse click                                                                                                     |
| [wev-git](https://git.sr.ht/~sircmpwn/wev)                                                         | Print wayland events, like xev(1)                                                                                                                         |
| [wlay-git](https://github.com/atx/wlay)                                                            | Graphical output management for Wayland                                                                                                                   |
| [wlsunset](https://sr.ht/~kennylevinsen/wlsunset)                                                  | Day/night gamma adjustments for Wayland compositors                                                                                                       |
| [wofi-emoji-git](https://github.com/dln/wofi-emoji)                                                | Emoji picker for Wayland using wofi and wtype                                                                                                             |
| [xdg-ninja-git](https://github.com/b3nj5m1n/xdg-ninja)                                             | A shell script which checks your $HOME for unwanted files and directories.                                                                                |
| [zoom](https://zoom.us/)                                                                           | Video Conferencing and Web Conferencing Service                                                                                                           |
| [zotero-bin](https://www.zotero.org/download)                                                      | Zotero Standalone. Is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources.                                      |

</div>

<div class="outline-2 smol-table">

### Mobile Apps {#mobile-apps}

Absolute dump. I use the [List My Apps](https://f-droid.org/packages/de.onyxbits.listmyapps/) app to generate the csv, the csv is then uploaded to dropbox from where airtable pulls it. When generating the org file my custom script fetches from airtable. I did not want this to be a rube goldberg machine but there doesn't seem to be a very clean way out in the way I need it at the moment.

[Notion](https://play.google.com/store/apps/details?id=notion.id) ○ [Adobe Acrobat](https://play.google.com/store/apps/details?id=com.adobe.reader) ○ [Habits](https://play.google.com/store/apps/details?id=org.isoron.uhabits) ○ [GuitarTuna](https://play.google.com/store/apps/details?id=com.ovelin.guitartuna) ○ [Adobe Scan](https://play.google.com/store/apps/details?id=com.adobe.scan.android) ○ [Zomato](https://play.google.com/store/apps/details?id=com.application.zomato) ○ [Embiggen](https://play.google.com/store/apps/details?id=com.briercan.embiggen) ○ [Snapseed](https://play.google.com/store/apps/details?id=com.niksoftware.snapseed) ○ [List My Apps](https://f-droid.org/repository/browse/?fdid=de.onyxbits.listmyapps) ○ [1.1.1.1](https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone) ○ [Ping Test Tool](https://play.google.com/store/apps/details?id=com.jjo.pingtest) ○ [F-Droid](https://www.google.com/search?q=org.fdroid.fdroid) ○ [PlantNet](https://play.google.com/store/apps/details?id=org.plantnet) ○ [Paytm](https://play.google.com/store/apps/details?id=net.one97.paytm) ○ [Quit Smoking](https://f-droid.org/repository/browse/?fdid=de.baumann.quitsmoking) ○ [Binary](https://play.google.com/store/apps/details?id=com.tomhogenkamp.binaircalculator) ○ [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) ○ [Forest](https://play.google.com/store/apps/details?id=cc.forestapp) ○ [Planta](https://play.google.com/store/apps/details?id=com.stromming.planta) ○ [Kite](https://play.google.com/store/apps/details?id=com.zerodha.kite3) ○ [Wolfram Alpha](https://play.google.com/store/apps/details?id=com.wolfram.android.alpha) ○ [Uber](https://play.google.com/store/apps/details?id=com.ubercab) ○ [Keep Notes](https://play.google.com/store/apps/details?id=com.google.android.keep) ○ [WhatsApp](https://play.google.com/store/apps/details?id=com.whatsapp) ○ [Awesome QR](https://play.google.com/store/apps/details?id=com.github.sumimakito.awesomeqrsample) ○ [Track](https://play.google.com/store/apps/details?id=com.nutritionix.nixtrack) ○ [Replit](https://play.google.com/store/apps/details?id=com.replit.app) ○ [Google Podcasts](https://play.google.com/store/apps/details?id=com.google.android.apps.podcasts) ○ [CRED](https://play.google.com/store/apps/details?id=com.dreamplug.androidapp) ○ [Protractor](https://play.google.com/store/apps/details?id=com.keuwl.protractor) ○ [Pocket](https://play.google.com/store/apps/details?id=com.ideashower.readitlater.pro) ○ [Grapevine](https://play.google.com/store/apps/details?id=com.app.gvine) ○ [Bluecoins](https://play.google.com/store/apps/details?id=com.rammigsoftware.bluecoins) ○ [Url forwarder](https://play.google.com/store/apps/details?id=net.daverix.urlforward) ○ [AnkiDroid](https://play.google.com/store/apps/details?id=com.ichi2.anki) ○ [Crayon](https://play.google.com/store/apps/details?id=com.jndapp.cartoon.crayon.iconpack) ○ [SoundCloud](https://play.google.com/store/apps/details?id=com.soundcloud.android) ○ [Track &amp; Graph](https://f-droid.org/repository/browse/?fdid=com.samco.trackandgraph) ○ [Unit Converter Ultimate](https://f-droid.org/repository/browse/?fdid=com.physphil.android.unitconverterultimate) ○ [Pinterest](https://play.google.com/store/apps/details?id=com.pinterest) ○ [GitHub](https://play.google.com/store/apps/details?id=com.github.android) ○ [VLC](https://play.google.com/store/apps/details?id=org.videolan.vlc) ○ [Telegram](https://play.google.com/store/apps/details?id=org.telegram.messenger) ○ [Airtable](https://play.google.com/store/apps/details?id=com.formagrid.airtable) ○ [Niagara Launcher](https://play.google.com/store/apps/details?id=bitpit.launcher) ○ [BHIM](https://play.google.com/store/apps/details?id=in.org.npci.upiapp) ○ [Shazam](https://play.google.com/store/apps/details?id=com.shazam.android) ○ [Drinkable](https://f-droid.org/repository/browse/?fdid=com.moimob.drinkable) ○ [Goodreads](https://play.google.com/store/apps/details?id=com.goodreads) ○ [Wikipedia](https://play.google.com/store/apps/details?id=org.wikipedia) ○ [Termux](https://f-droid.org/repository/browse/?fdid=com.termux) ○ [Discord](https://play.google.com/store/apps/details?id=com.discord) ○ [Signal](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms) ○ [Product Hunt](https://play.google.com/store/apps/details?id=com.producthuntmobile) ○ [Coin](https://play.google.com/store/apps/details?id=com.zerodha.coin) ○ [SimpleLogin](https://play.google.com/store/apps/details?id=io.simplelogin.android) ○ [Syncthing](https://play.google.com/store/apps/details?id=com.nutomic.syncthingandroid) ○ [Tapo](https://play.google.com/store/apps/details?id=com.tplink.iot) ○ [Lithium](https://play.google.com/store/apps/details?id=com.faultexception.reader) ○ [Snipd](https://play.google.com/store/apps/details?id=ai.topicfinder.podcastdiscovery) ○ [Brave](https://play.google.com/store/apps/details?id=com.brave.browser) ○ [NetGuard](https://play.google.com/store/apps/details?id=eu.faircode.netguard) ○ [PhonePe](https://play.google.com/store/apps/details?id=com.phonepe.app) ○ [HTTP Shortcuts](https://play.google.com/store/apps/details?id=ch.rmy.android.http_shortcuts) ○ [BigO](https://play.google.com/store/apps/details?id=hieunguyen725.bigo) ○ [Splitwise](https://play.google.com/store/apps/details?id=com.Splitwise.SplitwiseMobile) ○ [Relay Pro](https://play.google.com/store/apps/details?id=reddit.news) ○ [Zoom](https://play.google.com/store/apps/details?id=us.zoom.videomeetings) ○ [Binance](https://play.google.com/store/apps/details?id=com.binance.dev) ○ [Just Another Workout Timer](https://f-droid.org/repository/browse/?fdid=com.blockbasti.justanotherworkouttimer) ○ [Chess](https://play.google.com/store/apps/details?id=com.chess) ○ [WiFiAnalyzer](https://f-droid.org/repository/browse/?fdid=com.vrem.wifianalyzer) ○ [Tasks](https://play.google.com/store/apps/details?id=com.google.android.apps.tasks) ○ [Rapido](https://play.google.com/store/apps/details?id=com.rapido.passenger) ○ [DiskUsage](https://play.google.com/store/apps/details?id=com.google.android.diskusage) ○ [TrebleShot](https://play.google.com/store/apps/details?id=com.genonbeta.TrebleShot) ○ [Authenticator](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2)

</div>

<div class="outline-2 smol-table">

### Datasets {#datasets}

{{< lft >}}
-   Need to read [this](https://news.ycombinator.com/item?id=34558054)
{{< /lft >}}

{{< coolinks >}}
-   Hubs: [/r/datasets](https://www.reddit.com/r/datasets/) | [Our World in Data](https://ourworldindata.org/) | [WBO Data](https://data.worldbank.org/) | [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | [kaggle](https://www.kaggle.com/datasets) | [HDX](https://data.humdata.org/) | [AWS DE](https://aws.amazon.com/data-exchange/) | [public-apis](https://github.com/public-apis/public-apis) | [FreeGIS500+](https://freegisdata.rtwilson.com/) | [Academic Torrents](https://academictorrents.com/) | [HugginFace Datasets](https://huggingface.co/datasets) | [devdatalabs](https://www.devdatalab.org/shrug) | [Socrata](https://dev.socrata.com/) |  [Components One Datasets](https://components.one/datasets) | [moar datasets](https://news.ycombinator.com/item?id=40482845) | [datacommons](https://datacommons.org/)
{{< /coolinks >}}

| Name                                                                                                                              | Remark                                                                                                                                       | Category                                |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| [Marvel Comics API](https://news.ycombinator.com/item?id=7648860)                                                                 | Marvel Comics API                                                                                                                            | ['Fun', 'Media']                        |
| [Security Datasets](https://github.com/OTRF/Security-Datasets)                                                                    | Re-play Security Events                                                                                                                      | ['Global', 'Tech']                      |
| [emoji-data](https://github.com/iamcal/emoji-data)                                                                                | Easy to parse data and spritesheets for emoji                                                                                                | ['Fun', 'Code']                         |
| [UK House Price Index](https://landregistry.data.gov.uk/app/ukhpi)                                                                |                                                                                                                                              | ['Geo', 'Outside India']                |
| [Payments System Data](https://gitlab.com/CashlessConsumer/data-analysis-notebooks/-/wikis/Payments-System-Data-Dashboard)        | Comprehensive one stop place for all accessing, visualizing payments system data (PSD) in India                                              | ['Finance', 'India']                    |
| [farmsubsidy](https://farmsubsidy.org/)                                                                                           | Detailed data relating to payments and recipients of farm subsidies in every EU state                                                        | ['Geo', 'Outside India']                |
| [Common Crawl](https://commoncrawl.org/)                                                                                          | repository of web crawl data                                                                                                                 | ['DNS', 'Documents']                    |
| [taxonworks](https://taxonworks.org/)                                                                                             | web-based workbench for taxonomists and biodiversity scientists.                                                                             | ['Geo']                                 |
| [Umbrella Popularity List](https://s3-us-west-1.amazonaws.com/umbrella-static/index.html)                                         | The popularity list contains our most queried domains based on passive DNS usage                                                             | ['Global', 'Code', 'DNS']               |
| [OS OpenData](https://osdatahub.os.uk/downloads/open)                                                                             | Ordnance Survey OpenData                                                                                                                     | ['Global', 'Geo']                       |
| [Data Gov India](https://data.gov.in/)                                                                                            | Data on India                                                                                                                                | ['India']                               |
| [yrno](https://developer.yr.no/)                                                                                                  | Online weather service from the Norwegian Meteorological Institute                                                                           | ['Geo', 'Global']                       |
| [daylightmap](https://daylightmap.org/)                                                                                           | Daylight is a complete distribution of global, open map data that’s freely available with support from community and professional mapmakers. | ['Global', 'Geo']                       |
| [ Open Transit Data (Delhi)](https://otd.delhi.gov.in/)                                                                           | IITD collab                                                                                                                                  | ['Geo', 'India']                        |
| [lobbyfacts](https://www.lobbyfacts.eu/)                                                                                          | Exposing lobbying in the European institutions                                                                                               | ['Outside India', 'Documents']          |
| [GPT-4-LLM](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM)                                                           | Instruction GPT (GPT4 generated)                                                                                                             | ['LLM']                                 |
| [JusticeHub](https://justicehub.in/)                                                                                              | Legal &amp; Justice Data                                                                                                                     | ['India']                               |
| [wigglenet](https://wigle.net/?s=09)                                                                                              | Wireless network database                                                                                                                    | ['Geo', 'DNS', 'Code']                  |
| [handschriftenportal](https://handschriftenportal.de/info/about)                                                                  | Old manuscripts                                                                                                                              | ['Documents', 'Media']                  |
| [punpedia](https://punpedia.org/)                                                                                                 | Pun encyclopedia                                                                                                                             | ['Fun']                                 |
| [emailserverlist](https://dismail.de/serverlist.html)                                                                             | list of email providers and some data abt them                                                                                               | ['DNS']                                 |
| [WorldAtlas](https://github.com/topojson/world-atlas)                                                                             | Pre-built TopoJSON from Natural Earth.                                                                                                       | ['Global', 'Geo']                       |
| [Theatricalia](https://github.com/dracos/Theatricalia)                                                                            | A database of past and future theatre productions                                                                                            | ['Outside India', 'Fun']                |
| [ SpaceX-API](https://github.com/r-spacex/SpaceX-API)                                                                             | Open Source REST API for SpaceX launch, rocket, core, capsule, starlink, launchpad, and landing pad data.                                    | ['Global', 'Fun']                       |
| [Geolocation Database](https://ipapi.is/geolocation.html)                                                                         | IP - Geo Mapping                                                                                                                             | ['Geo', 'DNS']                          |
| [cities](https://github.com/tidwall/cities)                                                                                       | 10,000 Cities with Latitude, Longitude, and Elevation                                                                                        | ['Global', 'Geo']                       |
| [Subtree of Life](https://sol.vandenoever.info/)                                                                                  | relationships between different species.                                                                                                     | ['Geo']                                 |
| [Govt on github](https://news.ycombinator.com/item?id=36256538)                                                                   | Govts putting their stuff on github                                                                                                          | ['Global', 'Govt']                      |
| [factbook](https://github.com/factbook/factbook.json)                                                                             | World Factbook Country Profiles in JSON                                                                                                      | ['Global', 'Geo']                       |
| [asterank](https://github.com/typpo/asterank)                                                                                     | asteroid database, interactive visualizations, and discovery tools                                                                           | ['Geo', 'Global']                       |
| [ GH Archive ](https://www.gharchive.org/)                                                                                        | GH Archive is a project to record the public GitHub timeline                                                                                 | ['Code']                                |
| [overturemaps](https://overturemaps.org/)                                                                                         | open map data intended primarily to demonstrate the potential and possibilities for open map data                                            | ['Global', 'Geo']                       |
| [irail.be](https://docs.irail.be/)                                                                                                | iRail api allows anyone to query trains, stations, liveboards and connections.                                                               | ['Geo', 'Outside India']                |
| [GPTeacher](https://github.com/teknium1/GPTeacher)                                                                                | Modular datasets generated by GPT-4                                                                                                          | ['LLM']                                 |
| [Lobster users database](https://lobste.rs/users)                                                                                 | We can create a graph out of it                                                                                                              | ['Fun', 'Global']                       |
| [postcodes](https://github.com/ideal-postcodes/postcodes.io)                                                                      | UK postcode &amp; geolocation API, serving up open data                                                                                      | ['Global', 'Geo']                       |
| [mobilitydata](https://database.mobilitydata.org/)                                                                                | The Mobility Database catalogs is a repository of 1800+ mobility datasets across the world.                                                  | ['Global', 'Geo']                       |
| [USDA_Pomological_Watercolors](https://www.openculture.com/2019/06/the-us-government-commissioned-7500-watercolor-paintings.html) | 7,500 Watercolor Paintings of Every Known Fruit in the World: Download Them in High Resolution                                               | ['Global', 'Media']                     |
| [Icelandic Saga Database](https://www.sagadb.org/)                                                                                | online resource dedicated to publishing the Sagas of the Icelanders                                                                          | ['Outside India', 'Media', 'Documents'] |
| [Tranco](https://tranco-list.eu/)                                                                                                 | A Research-Oriented Top Sites Ranking Hardened Against Manipulation                                                                          | ['Global', 'Code', 'DNS']               |
| [samanantar](https://ai4bharat.iitm.ac.in/samanantar)                                                                             | publicly available parallel corpora collection for Indic languages                                                                           | ['India']                               |
| [Digitized Manuscripts](https://digitale-sammlungen.de/en/)                                                                       | Digitized Manuscripts, Prints, Music, Maps, Photographs, Newspapers and Magazine                                                             | ['Documents', 'Media']                  |
| [OpenFlights](https://news.ycombinator.com/item?id=26956271)                                                                      | Various flight related data providers                                                                                                        | ['Geo']                                 |
| [opentopography](https://opentopography.org/)                                                                                     | OpenTopography facilitates community access to high-resolution, Earth science-oriented, topography data, and related tools and resources.    | ['Global', 'Geo']                       |
| [The Majestic Million](https://majestic.com/reports/majestic-million)                                                             | The million domains we find with the most referring subnets                                                                                  | ['Global', 'Code', 'DNS']               |
| [PlaneCrashList](http://www.airsafe.com/events/models/rate_mod.htm)                                                               | Plane crash rates by model                                                                                                                   | ['Geo', 'Global']                       |
| [Apple domains](https://cdn.smoot.apple.com/static/autofill_tld_whitelist_url)                                                    |                                                                                                                                              | ['Global', 'Code', 'DNS']               |
| [JSON Against Humanity](https://crhallberg.com/cah/)                                                                              | Cards Against Humanity® as plain text and JSON.                                                                                              | ['Fun']                                 |
| [Yelp](https://www.yelp.com/dataset)                                                                                              | The Yelp Dataset                                                                                                                             | ['Global']                              |
| [trustwallet/assets](https://github.com/trustwallet/assets)                                                                       | A comprehensive, up-to-date collection of information about several thousands (!) of crypto tokens.                                          | ['Global', 'Finance']                   |
| [geofabrik](https://www.geofabrik.de/)                                                                                            | we extract, select, and process free geodata for you. We create shape files, maps, map tiles and full-blown web mapping solutions.           | ['Global', 'Geo']                       |
| [celestrak](https://celestrak.org/)                                                                                               | understanding of our orbital environment and how to use it safely and responsibly.                                                           | ['Global', 'Geo']                       |
| [CrawlerNinja](https://crawler.ninja/)                                                                                            | Top 1 Million Sites Security Analysis                                                                                                        | ['Global', 'DNS', 'Code']               |
| [Ship Wreck Database 2](https://wrakkendatabank.afdelingkust.be/)                                                                 |                                                                                                                                              | ['Fun']                                 |
| [QuickWick/Music-AI-Voices](https://huggingface.co/QuickWick/Music-AI-Voices)                                                     | AI Voices                                                                                                                                    | ['Media']                               |
| [opentreeoflife](https://opentreeoflife.github.io/)                                                                               | comprehensive, dynamic and digitally-available tree of life                                                                                  | ['Geo']                                 |
| [Digitalisierte Sammlungen](https://digital.staatsbibliothek-berlin.de/)                                                          | Digitalisierte Sammlungen der Staatsbibliothek zu Berlin                                                                                     | ['Documents', 'Media']                  |
| [GraphHopper Traffic](https://github.com/graphhopper/open-traffic-collection)                                                     | GraphHopper Open Traffic Collection                                                                                                          | ['Outside India', 'Geo']                |
| [CreativeCommons](https://search.creativecommons.org/)                                                                            | CC stuff                                                                                                                                     | ['Documents', 'Media']                  |
| [sportsdatabase](https://sportsdatabase.com/)                                                                                     | peer-to-peer sports data with the SDQL API                                                                                                   | ['Global', 'Sports']                    |
| [Wikipedia Embeddings](https://txt.cohere.com/embedding-archives-wikipedia/)                                                      | Multilang Wikipedia Embeddings                                                                                                               | ['Documents']                           |
| [Airframe](https://app.airframes.io/)                                                                                             | Something airport data                                                                                                                       | ['Geo']                                 |
| [H1B salary DB](https://news.ycombinator.com/item?id=36277706)                                                                    | H1B salaray database , search and sort                                                                                                       | ['Outside India', 'Finance']            |
| [landconflictwatch](https://www.landconflictwatch.org/)                                                                           | Tracking natural resource disputes in India                                                                                                  | ['Geo', 'India']                        |
| [groundhogday](https://groundhog-day.com/)                                                                                        |                                                                                                                                              | ['Fun']                                 |
| [Encyclopedia of Life](https://eol.org/)                                                                                          | Encyclopedia of Life                                                                                                                         | ['Geo']                                 |
| [PublicDataMarket](https://publicdatamarket.com/datasets/)                                                                        | Random scraped datasets                                                                                                                      | ['Global']                              |
| [CF Radar](https://developers.cloudflare.com/radar/)                                                                              | CF Internet data                                                                                                                             | ['Geo', 'DNS', 'Code']                  |
| [Ship Wreck Database](https://www.wrecksite.eu/wrecksite.aspx)                                                                    |                                                                                                                                              | ['Fun']                                 |
| [gisgraphy](https://www.gisgraphy.com/index.php)                                                                                  | Open source geocoder and addresses / POIs databases                                                                                          | ['Geo', 'Global']                       |
| [naturalearthdata](https://www.naturalearthdata.com/)                                                                             | Natural Earth you can make a variety of visually pleasing, well-crafted maps with cartography or GIS software.                               | ['Global', 'Geo']                       |

</div>

</div>
