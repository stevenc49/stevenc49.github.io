import pprint
import os, subprocess
import re
from fileutils import FileUtil

'''
    This script creates a chinesepod xml feed for beyondpod
'''

ROOT_DIR = "/home/steve/workspace/stevenc49.github.io/"
SITE_DIR = ROOT_DIR + "_site/pages/lists"



def main():

    print('> generating cp feed.xml')

    content = """
{% raw %}
your code block
{% endraw %}

    """

    # write to site dir
    FileUtil.saveToFile(content, SITE_DIR + "/cpfeed.xml")






if __name__ == '__main__':

    main()