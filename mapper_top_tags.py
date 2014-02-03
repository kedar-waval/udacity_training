#!/usr/bin/python
import sys
import csv
import operator

#-----------------------------------------------------------#
# The mapper reads through all the records in the input,    #
# skips the first record (which happens to be the header)   #
#                                                           #
# tagnames is the 3rd field in a record.                    #
# The mapper separates all the tags in tagnames and         #
# outputs topN tags.                                        #
#-----------------------------------------------------------#
n = 10

tagOccurence = {}
reader = csv.reader(sys.stdin, delimiter='\t')
headerSkipped = False

for line in reader:

    if len(line) != 19:
       continue

    if not headerSkipped:      
       headerSkipped = True    
       continue                

    for i in line[2].split(" "):
        if i != '':
           if i not in tagOccurence:
              tagOccurence[i] = 1
           else:
              tagOccurence[i] = tagOccurence[i]+1

tagOccurence1 = [(v, k) for k, v in tagOccurence.items()]
tagOccurence1 = sorted(tagOccurence1, reverse=True, key=lambda x: int(x[0]))[:n]

for i in tagOccurence1:
    print "{0}\t{1}".format(i[1], i[0])
