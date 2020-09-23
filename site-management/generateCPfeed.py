import pprint
import os, subprocess
import re
from fileutils import FileUtil

'''
    This script creates a chinesepod xml feed for beyondpod
'''

ROOT_DIR = "/home/steve/workspace/stevenc49.github.io/_cp/"



def main():

    print('> generating cp feed.xml')

    # generate markdown list content
    sb = """
        <test>
    """


    # write to solved list markdown page
    FileUtil.saveToFile(sb, ROOT_DIR + "cpfeed.xml")



if __name__ == '__main__':

    main()