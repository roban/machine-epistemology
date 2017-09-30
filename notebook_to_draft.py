import os
import sys
from subprocess import call

HEADER = """---
layout: post
title: "{}"
---

"""

DRAFTSDIR = "_drafts"

if __name__ == '__main__':
  notebookfile = sys.argv[1]
  if len(sys.argv) > 2:
    title = sys.argv[2]
  else:
    title = None
  call(["ipython", "nbconvert", notebookfile, "--to", "markdown"])
  mdfile = notebookfile.replace(".ipynb", ".md")
  with open(mdfile, 'r') as md:
    inputmd = md.read()

  outputmd = (HEADER.format(title or mdfile) +
              inputmd.replace("![png](", "![png]({{ site.baseurl }}/notebooks/"))
  outputfile = os.path.join(DRAFTSDIR, os.path.basename(mdfile))

  with open(outputfile, 'w') as omd:
    omd.write(outputmd)
