#!/usr/bin/python
import sys
import csv
from datetime import datetime

#-----------------------------------------------------------#
# The mapper reads through all the records in the input,    #
# skips the first record (which happens to be the header)   #
# and outputs author_id and hour part of the added_at date. #
#                                                           #
# author_id is the 4th field in a record.                   #
# added_at is the 9th field in a record.                    #
#-----------------------------------------------------------#

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
headerSkipped = False

for line in reader:

    #skip the first (Header) line
    if not headerSkipped:
       headerSkipped = True
       continue

    author_id = line[3].strip('"')
    added_at_hour = datetime.strptime(line[8].strip('"').split('.')[0], '%Y-%m-%d %H:%M:%S').hour

    print "{0}\t{1}".format(author_id, added_at_hour)
