import pprint
import os, subprocess
import re
from fileutils import FileUtil

'''
    This script creates a chinesepod xml feed for beyondpod
'''

ROOT_DIR = "/home/steve/workspace/stevenc49.github.io/cp/"



def main():

    print('> generating cp feed.xml')

    # generate markdown list content
    sb = """
---
layout: page
title:  CP Feed
---
    """.strip() + "\n\n\n"


    # write to solved list markdown page
    FileUtil.saveToFile(sb, ROOT_DIR + "cpfeed.md")



if __name__ == '__main__':

    main()