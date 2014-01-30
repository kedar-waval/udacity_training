#!/usr/bin/python
import sys

#-----------------------------------------------------------#
# The reducer reads through all the records in the input.   #
# The input is of the format node_id\tType\tbody_length     #
#                                                           #
# If the record type is A, its a question; store its length #
# If the record type is B, its an answer; store its length  #
# in an array so that the array could later be used for     #
# calculating average.                                      #
#                                                           #
# The output is of the format                               #
# node_id\tquestion_length\taverage_answer_length           #
#-----------------------------------------------------------#

lastId = None
lastQuestLength = 0
answerLengths = []
avgAnsLength = 0

#This function helps with avarage length calculations
def calcAvg():
    global lastId
    global lastQuestLength
    global answerLengths
    global avgAnsLength

    if len(answerLengths) == 0:
       avgAnsLength = 0
    else:
       avgAnsLength = sum(answerLengths)/float(len(answerLengths))

    print lastId, "\t", lastQuestLength, "\t", avgAnsLength

    answerLengths[:] = []
    return

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        continue                 #Something has gone wrong. Skip this line.

    thisId, thisType, thisLength = data_mapped

    if lastId and lastId != thisId:   
       calcAvg()
 
    lastId = thisId
    if thisType == 'A':
       lastQuestLength = thisLength
    else:
       answerLengths.append(float(thisLength))
    
if lastId != None:                    #calculate and print result for last post
   calcAvg()
   
