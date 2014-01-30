#!/usr/bin/python
import sys
import csv

#-----------------------------------------------------------#
# The mapper reads through all the records in the input,    #
# skips the first record (which happens to be the header)   #
# For nodes of type "question" it outputs                   #
# node_id\tA\tbody_length                                   #
#                                                           #
# For nodes of type "answer" it outputs                     #
# abs_parent_id\tB\tbody_length                             #
#                                                           #
# The A or B written to the output help sort the record     #
# before they are consumed by the reducer.                  #
# They make sure that question comes first followed by all  #
# the answers.                                              #
#                                                           #
# node_id is the 1st field in a record.                     #
# node_type is the 6th field in a record.                   #
# body is the 5th field in a record.                        #
# abs_parent_id is the 8th field in a record.               #
#-----------------------------------------------------------#

reader = csv.reader(sys.stdin, delimiter='\t')
headerSkipped = False

for line in reader:

    if len(line) != 19:
       continue

    if not headerSkipped:      
       headerSkipped = True    
       continue                

    node_id = line[0].strip('"')
    node_type = line[5].strip('"')
    body = line[4].strip('"')
    abs_parent_id = line[7].strip('"')
    
    if node_type == "question":
       print "{0}\t{1}\t{2}".format(node_id, "A", len(body))

    if node_type == "answer":
       print "{0}\t{1}\t{2}".format(abs_parent_id, "B", len(body))
