import re

file = open("test.txt", "r")
doclist = [ line for line in file ]
docstr = '' . join(doclist)
sentences = re.split(r'[.!?]', docstr)