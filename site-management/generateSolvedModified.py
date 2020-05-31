import pprint
import os, subprocess
import re
from fileutils import FileUtil


ROOT_DIR = "/home/steve/workspace/stevenc49.github.io/"
PROBLEMS_DIR = ROOT_DIR + "_problems"
LIST_DIR = ROOT_DIR + "pages/lists"

def getAttribute(filename, attribute):
    content = FileUtil.readFromFile( PROBLEMS_DIR + "/" + filename )
    attributeLen = len(attribute)+1
    return list( filter( lambda x: attribute + ": " in x, content.split('\n') ) )[0][attributeLen:].strip()

def main():

    os.chdir( PROBLEMS_DIR )

    ll_result = os.popen('ls -lt --time-style=long-iso').read()
    ll_result =  ll_result.split('\n')
    ll_result = filter(None, ll_result)		# remove empty element

    # got list of filenames/dates
    list_filenames_dates = []
    for line in ll_result:
        filename, last_modified = line[47:], line[30:40]
        list_filenames_dates.append( (filename, last_modified) )


    # generate markdown list content
    sb = """
---
layout: page
title:  Solved - Last Modified
---
    """.strip() + "\n\n\n"

    # generate table header
    sb += "Problem | Last Modified\n"
    sb += "-----------|-----------\n"

    # generate table rows
    for prob in list_filenames_dates:
        filename = prob[0]

        if filename and filename!="1template.md":
            sb += "[%s](%s) | %s \n" % (getAttribute(filename, "title"), "/problems/"+filename[:-3], prob[1])


    # write to solved list markdown page
    FileUtil.saveToFile(sb, LIST_DIR + "/solvedLastModified.md")



if __name__ == '__main__':

    # print( getAttribute("waterWithMostWater.md", "category") )
    main()