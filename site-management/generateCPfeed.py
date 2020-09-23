import pprint
import os, subprocess
import re
from fileutils import FileUtil

'''
    This script creates a chinesepod xml feed for beyondpod
'''

ROOT_DIR = "/home/steve/workspace/stevenc49.github.io/"
SITE_DIR = ROOT_DIR + "_site/pages/lists"
LIST_DIR = ROOT_DIR + "pages/lists"



def main():

    print('> generating cp feed.xml')

    content = """
        <test/>

    """


    # write to solved list markdown page
    FileUtil.saveToFile(content, LIST_DIR + "/cpfeed.md")



if __name__ == '__main__':

    main()