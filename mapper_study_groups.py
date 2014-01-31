#!/usr/bin/python
import sys
import csv

#-----------------------------------------------------------#
# The mapper reads through all the records in the input,    #
# skips the first record (which happens to be the header)   #
# For nodes of type "question" it outputs                   #
# node_id\tauthor_id                                        #
#                                                           #
# For nodes of type "answer" or "comment" it outputs        #
# abs_parent_id\tauthor_id                                  #
#                                                           #
# node_id is the 1st field in a record.                     #
# node_type is the 6th field in a record.                   #
# author_id is the 4th field in a record.                   #
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
    author_id = line[3].strip('"')
    abs_parent_id = line[7].strip('"')
    
    if node_type == "question":
       print "{0}\t{1}".format(node_id, author_id)
    else:
       print "{0}\t{1}".format(abs_parent_id, author_id)
