import os
import sys
from subprocess import call
import datetime

HEADER = """---
layout: post
title: "{}"
---

"""

DRAFTSDIR = "_drafts"
POSTSDIR = "_posts"

if __name__ == '__main__':
  notebookfile = sys.argv[1]
  if len(sys.argv) > 2:
    title = sys.argv[2]
  else:
    title = None
  if len(sys.argv) > 3:
    make_post = sys.argv[3] == 'post'
  call(["ipython", "nbconvert", notebookfile, "--to", "markdown"])
  mdfile = notebookfile.replace(".ipynb", ".md")
  with open(mdfile, 'r') as md:
    inputmd = md.read()
  print "Removing {}".format(mdfile)
  os.remove(mdfile)

  today = datetime.datetime.today().strftime('%Y-%m-%d')
  outputmd = (HEADER.format(title or mdfile) +
              inputmd.replace("![png](", "![png]({{ site.baseurl }}/notebooks/"))
  dirname = POSTSDIR if make_post else DRAFTSDIR
  outputfile = os.path.join(dirname, today + '-' + os.path.basename(mdfile))

  print "Writing to {}".format(outputfile)
  with open(outputfile, 'w') as omd:
    omd.write(outputmd)
