#!/usr/bin/python

import sys
from datetime import datetime

#-----------------------------------------------------------#
# The reducer reads through all the records in the input.   #
# The input is of the format author_id\tadded_at_hour.      #
#                                                           #
# It counts the number of lines in the input that have the  #
# same author_id and added_at_hour; remembers the hour for  #
# for which highest activity is found so far and  outputs   #
# the highest activity hour for an author.                  #
#                                                           #
# It also considers the possibility of an author having the #
# same highest activity in more than one hours by recording #
# then in an array.                                         #
#-----------------------------------------------------------#

lastId = None
lastHour = None
activityCount = 1
activityCountMax = 1
highestActivityHours = []

#This function helps with the recording of highest activity.
#It optionally prints the results depending on the input flag.
def calcMax(printResult):
    global lastId
    global lastHour
    global activityCount
    global activityCountMax

    if activityCount > activityCountMax:
       activityCountMax = activityCount
       highestActivityHours[:] = []
       highestActivityHours.append(lastHour)
    elif activityCount == activityCountMax:
       highestActivityHours.append(lastHour)

    if printResult == 1:
       print lastId, "\t", ', '.join(highestActivityHours)
    return

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue                 #Something has gone wrong. Skip this line.

    thisId, thisHour = data_mapped

    if lastId and lastId == thisId and lastHour and lastHour == thisHour:  #same author same hour
       activityCount += 1 

    if lastId and lastId == thisId and lastHour and lastHour != thisHour:  #Same author different hour,
       calcMax(0)                                                          #record activity counts and reset the counter
       activityCount = 1                            
       
    if lastId and lastId != thisId:   #Different author,
       calcMax(1)                     #record activity counts and print the highest activity hours
       activityCount = 1                            
       activityCountMax = 1                         
       highestActivityHours[:] = []

    lastId = thisId
    lastHour = thisHour
 
if lastId != None:                    #calculate and print result for last author_id in the input
   calcMax(1)
    
