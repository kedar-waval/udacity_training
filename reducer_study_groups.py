#!/usr/bin/python
import sys

#-----------------------------------------------------------#
# The reducer reads through all the records in the input.   #
# The input is of the format node_id\tauthor_id             #
#                                                           #
# The output is of the format                               #
# node_id\t<comma separeted list of author_ids>             #
#-----------------------------------------------------------#

lastId = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue                 #Something has gone wrong. Skip this line.

    thisId, thisAuthor = data_mapped

    if lastId == None:
       print thisId + "\t",
       print thisAuthor,
    elif lastId and lastId != thisId:   
       print " "
       print thisId + "\t",
       print thisAuthor,
    else:
      print ", " + thisAuthor,

    lastId = thisId
    lastAuthor = thisAuthor
    
print ", " + thisAuthor,
