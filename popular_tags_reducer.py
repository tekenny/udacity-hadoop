#!/usr/bin/python

import csv
import sys 

def reducer():
    # Using CSV reader and writer to simplify input/output 
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    count   = 0
    lastKey = None
    theList = []
    for line in reader:
        if len(line) != 2: # skip bad data
            continue
    
        theKey  = line[0]
        if theKey == '': # skip if no tag exists
            continue
    
        if lastKey and theKey != lastKey:
            # Append the count for this tag to theList
            theList.append([count, lastKey])
            count = 0 
            
        # Increment count for this tag
        # Don't assume value is 1 in case a combiner is used
        count  += int(line[1])
        lastKey = theKey 

    # Must ensure the last tag record is in theList
    if lastKey != None:
        theList.append([count, lastKey])

    # Sort the list containing the counts in descending order
    theList.sort(reverse=True)
    # Write a row for each tag that is in the top ten from theList
    for count, tag in theList[:10]:
        writer.writerow([tag, count])

# The following is to be able to test outside of hadoop
def main():
    reducer()

main()
