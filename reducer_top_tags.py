#!/usr/bin/python

import sys

#-----------------------------------------------------------#
# The reducer reads through all the records in the input.   #
# The input has only one field - tagname - per line.        #
#                                                           #
# It keeps track of the top-N tags using a tuple-list       #
#-----------------------------------------------------------#

n = 10
lastTag = None
occurence = 0
topN = [(0, 'a')] * n
minOcc = min(topN)[0] 

#This function helps with the recording of top-N tags
def calcTopN():
    global n
    global lastTag
    global occurence
    global topN
    global minOcc

    if occurence > minOcc:
       topN.append((occurence, lastTag))
       topN = sorted(topN, reverse=False)
       topN = topN[1:]
       minOcc = min(topN)[0]

    return

for line in sys.stdin:
    thisTag = line.strip() 
    if lastTag and lastTag != thisTag:
       calcTopN()
       occurence = 0

    lastTag = thisTag
    occurence += 1 

calcTopN()

topN = sorted(topN, reverse=True)
for i in topN:
    print "{0}\t{1}".format(i[1], i[0])
