# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 17:26:49 2016

@author: Manny
"""

# Assign initial variables
runVar = "Y"
base = (580966.028, 4275431.647, 214.00)
antennaHeight = 2.0
savePath = "C:\\Dropbox\\3dspatial_GPSpoints\\"

# Import modules 
import time
import os

# Create empty arrays to append data into 
targetList = []
targetPoint = []
point = ()
calcList = []

# use this array for testing while Piksi rover is offline, comment out when running live
#baseline_table = [(1,2),(3,4),(5,6),(7,8),(9,0),(11,12),(13,14),(15,16)]

# Define function to acquire a single point location on survey. 
# The user is prompted to enter a prefix and target to identify the point location
# User is also prompted to take 10 baseline positions (at least 0.5 sec apart)
# that are subsequently averaged to result in a single point position. A maximum variance can be 
# hard coded (rangeN and RangeE) to reject readings with too much movement in the targets
# targetList will contain a 2-item label and ten positions for each surveyed point.

def getTarget():
    targetNum = str(raw_input("Target: "))
    targetID = ("target " + targetNum)
    targetPoint = [(targetID)]
    northList = []
    eastList = []
    for i in range(10):
        try:
            press = raw_input("Press enter to continue...")
        except:
            press = ""
        north = baseline.table[3][1]
        east = baseline.table[4][1]
        northList.append(north)
        eastList.append(east)
        down = baseline.table[5][1]
        point = (north, east, down)
        targetPoint.append(point)
        time.sleep(0.5)
#    n = sum(a[0] for a in targetPoint / len(targetPoint))
#    e = sum(a[1] for a in targetPoint / len(targetPoint))
#    d = sum(a[2] for a in targetPoint / len(targetPoint))
#    calcPoint = (prefix, targetNum, n, e, d)
    #rangeN = max(northList) - min(northList)
    #rangeE = max(eastList) - min(eastList)
    #if rangeN < 0.15 and rangeE < 0.15:
    #    targetList.append(targetPoint)
    #else:
    #    print "Too much antenna movement. Point not taken."

    targetList.append(targetPoint)

# Points are collected until user ends the process. If user enters "Y"/"y" or presses enter, they
# will be continually prompted for the next prefix. If no additional point is desired, the prefix must still be entered 
# and a point collected, and then "N"/"n" selected when runVar is prompted for again.

while runVar == "Y" or runVar == "y":
    try:
        getTarget()
        try:
            runVar = str(raw_input("Take another point? Enter Y or N: "))
            if runVar != "N" and runVar != "n" and runVar != "Y" and runVar != "y":
                while runVar != "N" and runVar != "n" and runVar != "Y" and runVar != "y":
                    print "Invalid entry"
                    runVar = str(raw_input("Take another point? Enter Y or N"))
            if runVar == "N" or runVar == "n":
                pass
        except:
            runVar == ""
    except:
        pass

# each point in targetList is given a single position, by averaging the 10 positions collected with getTarget() and appending to calcList
for t in targetList:
    n = sum(a[0] for a in t[1:]) / float(len(t[1:]))
    e = sum(a[1] for a in t[1:]) / float(len(t[1:]))
    d = sum(a[2] for a in t[1:]) / float(len(t[1:]))
    calcPoint = (t[0], n, e, d)
    calcList.append(calcPoint)
    
# use calcList to calculate actual UTM position from base position

# enter new base position if necessary
#newBase = str(raw_input("Use default base position E/N/Elev " + str(base) + "? Y/N: "))
#if newBase == "Y" or newBase == "y":
#    pass
#if newBase == "N" or newBase == "n":
#    baseE = float(raw_input("Enter base Easting: "))
#    baseN = float(raw_input("Enter base Northing: "))
#    baseElev = float(raw_input("Enter base Elevation: "))
#    base = (baseE, baseN, baseElev)
#else:
#    #print "Default base selected!"        
#    pass

# enter new antenna height if necessary
#newAnt = str(raw_input("Use default antenna height (" + str(antennaHeight) + ")? Y/N: "))
#if newAnt == "Y" or newAnt == "y":
#   pass
#if newAnt == "N" or newAnt == "n":
#   antennaHeight = float(raw_input("Enter antenna height (m): "))
#else:
#    #print "Default antenna height selected!"
#    pass
# Calculate actual target point position
utmList = []

#for i in calcList:
#    targetName = i[0]
#    northing = i[1] + base[1]
#    easting = i[2] + base[0]
#    elev = i[3] + base[2]
#    utmPoint = (targetName, easting, northing, elev)
#    utmList.append(utmPoint)
        
# Assign a path for saving points .txt file if necessary
#newPath = str(raw_input("Use default path (" + str(savePath) + ")? Y/N: "))
#if newPath == "N":
#    savePath = str(raw_input("Enter new path (use \\ instead of \): "))
#if newPath == "Y":
#    pass

# Assign a file name for .txt file
fileName = str(raw_input("Enter file name: "))

# Create full save path and file name
fullFile = savePath + fileName + ".txt"

# Create, open, and write to file
fileGPS = open(fullFile, "w")
for line in calcList:
    fileGPS.write(str(line[0]) + "," + str(line[1]) + "," + str(line[2]) + "," + str(line[3]) + "\n")
fileGPS.close()
print "File saved as: " + fileName + ".txt"



    



