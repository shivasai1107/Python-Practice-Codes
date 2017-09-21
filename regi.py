import re

def Main():
    line= "I think I understand regular expressions"

    matchResult= re.match(r"think", line, re.M|re.I)

    if matchResult:
        print "Found a match for"+ matchResult.group()
    else:
        print "Sorry Dude!"

    searchResult= re.search(r"think", line, re.M|re.I)

    if searchResult:
        print "Found it"+ searchResult.group()
    else:
        print "Sorry dude nothing found in seach"


if __name__=="__main__":
    Main()

