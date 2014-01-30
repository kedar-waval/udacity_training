#!/usr/bin/python
import sys
import csv

#-----------------------------------------------------------#
# The mapper reads through all the records in the input,    #
# skips the first record (which happens to be the header)   #
#                                                           #
# tagnames is the 3rd field in a record.                    #
# The mapper separates all the tags in tagnames and         #
# outputs one tag per line.                                 #
#-----------------------------------------------------------#

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
           print i
