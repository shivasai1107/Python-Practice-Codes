import sys
import re

word=re.compile(r'\bproblem.*\b',flags= re.I)
for line in sys.stdin.readlines():
    match=re.search(word, line)
    if match is not None:
	print "yes"
    else:
	print "No"
