+++
title = "Snipes"
author = ["Hrishikesh Barman"]
draft = false
+++

I get nerdsniped by myself more often that i'd like, but i still want to keep the question in the back of my head. Other times I am just curious about things and to try it out myself even if the solution to the problem is known to the world. I'll dump my [questions](https://gwern.net/question) here.


## Computers and Programming {#computers-and-programming}


### Systems {#systems}


#### How different levels of computation will handle K-means {#how-different-levels-of-computation-will-handle-k-means}

Can experiment with this [blogpost](http://www.goldsborough.me/c++/python/cuda/2017/09/10/20-32-46-exploring_k-means_in_python,_c++_and_cuda/) also see [someshkar/colabcat](https://github.com/someshkar/colabcat)


#### How would I really sort a big file? {#how-would-i-really-sort-a-big-file}

Sort a 100GB file in 12GB memory. Various approaches.

```shell
cat main.cpp | tr a-z A-Z
# vs
tr a-z A-Z < main.cpp
```

-   What would `sort` do?
-   [External sorting - Wikipedia](https://en.wikipedia.org/wiki/External_sorting)
-   External sorting with concurrency
-   Loading it into a DB and sorting
-   [Reducing Pandas memory usage #3: Reading in chunks](https://pythonspeed.com/articles/chunking-pandas/)
-   [Fast subsets of large datasets with Pandas and SQLite](https://pythonspeed.com/articles/indexing-pandas-sqlite/)
-   [When your data doesn’t fit in memory: the basic techniques](https://pythonspeed.com/articles/data-doesnt-fit-in-memory/)
-   [Scaling to large datasets — pandas 2.0.0 documentation](https://pandas.pydata.org/docs/user_guide/scale.html)


#### Most efficient way to show last added file in the filesystem/dir {#most-efficient-way-to-show-last-added-file-in-the-filesystem-dir}

-   [shell - Get most recent file in a directory on Linux - Stack Overflow](https://stackoverflow.com/questions/1015678/get-most-recent-file-in-a-directory-on-linux)
-   [bash - How to recursively find the latest modified file in a directory? - Stack Overflow](https://stackoverflow.com/questions/4561895/how-to-recursively-find-the-latest-modified-file-in-a-directory)


#### Is IFS not Indian Forest Services? (Bash edition) {#is-ifs-not-indian-forest-services--bash-edition}

-   This stuff is pretty basic but I don't think I totally get it plus there is some "shell" specific behavior that's weird.
-   Also `man 1 read` (fish) and `man 1p read` (posix) are different, what about that idk. fish apparently does not document `-r` but still lets me use it.
-   [memory - Are files opened by processes loaded into RAM? - Unix &amp; Linux Stack Exchange](https://unix.stackexchange.com/questions/367982/are-files-opened-by-processes-loaded-into-ram)
-   [linux - What happens if you edit a script during execution? - Unix &amp; Linux Stack Exchange](https://unix.stackexchange.com/questions/88487/what-happens-if-you-edit-a-script-during-execution)
-   [bash - Understanding "IFS= read -r line" - Unix &amp; Linux Stack Exchange](https://unix.stackexchange.com/questions/209123/understanding-ifs-read-r-line)
-   [Why is using a shell loop to process text considered bad practice? - Unix &amp; Linux Stack Exchange](https://unix.stackexchange.com/questions/169716/why-is-using-a-shell-loop-to-process-text-considered-bad-practice)


#### How easy is for someone to steal my stdout stuff {#how-easy-is-for-someone-to-steal-my-stdout-stuff}

-   Example could be me logging my passwords in the cli.
-   [How to Handle Secrets on the Command Line](https://smallstep.com/blog/command-line-secrets/)


### Security {#security}


#### Does iframe+cors does not do what i think it does? {#does-iframe-plus-cors-does-not-do-what-i-think-it-does}

See SO answers here [signin inside iframe - Google Search](https://www.google.com/search?q=signin+inside+iframe)
