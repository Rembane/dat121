dat121
======

This repository keeps the latest version of the org-files of the Programming Paradigms site, so we can see the changes with git diff.

The site: http://www.cse.chalmers.se/~bernardy/pp/

Usage
-----

Use the files on github instead of the original site: https://github.com/Rembane/dat121/tree/master/site

Or if you want your own hosting, fork this repo and add the following line to your crontab:

```
0 * * * * cd /path/to/script && python update.py 
```
