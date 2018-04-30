# Assignment 4
# Christopher Rico
# CS325
# OSU ID: 933239746

import math
from collections import namedtuple
from operator import attrgetter

class Activity:
    def __init__(self, activityNum, start, end):
        self.activityNum = activityNum
        self.start = start
        self.end = end



def lastToStart(activityList):
    #sorts the jobs by the starting time, with largest last
    activityList.sort(key = attrgetter('start'), reverse = True)


    chosenActivites = []
    #get the activity that starts last
    chosenActivites.append(listOfActivities[0])
    lastAddedActivity = listOfActivities[0]

    #iterate through all the activities
    for j in range(1, len(listOfActivities)):
        potentialActivity = listOfActivities[j]

        #if an activity ends earlier than the last one chosen starts
        if potentialActivity.end <= lastAddedActivity.start:
            #choose it to do
            chosenActivites.push(listOfActivities[j])
            lastAddedActivity = listOfActivities[j]

    return chosenActivites



def main():
    dataFile = open("act.txt", "r")

    #split the file into an array of values
    for line in dataFile:
        multiLineArray = list(map(int, line.split()))

    #get the number of activities of the first set
    numActivities = multiLineArray[0]
    activityArr = []
    setNum = 0


    #split multiLineArray by spaces - get start and stop values to individual indexes
    for j in range(1, len(multiLineArray)):
        lineArray = multiLineArray[j].split(" ")

        #get start and stop values into int values
        for i in range(0, len(lineArray)):
            lineArray[i] = int(lineArray[i])

        #push
        if len(lineArray) != 1:
            activityNum = lineArray[0]
            start = lineArray[1]
            end = lineArray[2]
            activityArr.append(Activity.(activityNum, start, end))

        else:
            setNum++
            print("Set " + str(setNum))
            chosenActivites = lastToStart(activityArray)
            numChosen = len(chosenActivites)
            print("Number of activites selected = " + str(numChosen))
            print("Activities: ")
            chosenActivites.reverse()

            for act in chosenActivites:
                print(str(act.activityNum) + " ")

            print("\n")
            activityArr = []


if __name__ == '__main__':
    main()
