#!/usr/bin/python

import csv
import sys

def reducer():
    # Using CSV reader and writer to simplify input/output
    reader = csv.reader(sys.stdin, delimiter='\t')    
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    highCount    = -1
    lastKey      = None
    hourlyCounts = {} # create a dictionary for hourly counts
    for line in reader:
        if len(line) != 2: # skip bad data
            continue

        theKey  = line[0]
        theHour = line[1]
        if lastKey and theKey != lastKey:
            # Write records for lastKey if theKey has changed
            write_row(writer, lastKey, highCount, hourlyCounts)
            # Reset highCount and hourlyCounts
            highCount    = -1
            hourlyCounts = {}
            
        # Determine if the current key exists in the dictionary
        if theHour in hourlyCounts:
            # Increment the hourlyCount for theHour if it is in the dictionary
            hourlyCounts[theHour] += 1
        else:
            # Set the hourlyCount to 1 if theHour is not in the dictionary
            hourlyCounts[theHour] = 1
        # Determine if the highCount needs to be set to current count value
        if hourlyCounts[theHour] > highCount:
            highCount = hourlyCounts[theHour]
        lastKey = theKey

    # Must ensure the last record is written
    if lastKey != None:
        write_row(writer, lastKey, highCount, hourlyCounts)
        
# This function will write the record(s) with the highest hourly count
def write_row(writer, lastKey, highCount, hourlyCounts):
    # Loop through the dictionary and write records that match the high count
    for hour, count in hourlyCounts.iteritems():
        if hourlyCounts[hour] == highCount:
            writer.writerow([lastKey, hour])

# The following is to be able to test outside of hadoop
def main():
    reducer()

main()
