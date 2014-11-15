#!/usr/bin/python

import csv
import sys 

def reducer():
    # Using CSV reader and writer to simplify input/output 
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
            
    lastKey = None
    theList = []
    for line in reader:
        if len(line) != 2: # skip bad data
            continue
    
        theKey  = line[0]
        if lastKey and theKey != lastKey:
            writer.writerow([lastKey, theList])
            theList = []
        
        # Append the author_id to theList
        theList.append(line[1])
        lastKey = theKey 
                
    # Must ensure the last tag record is in theList
    if lastKey != None:   
        writer.writerow([lastKey, theList])
                
# The following is to be able to test outside of hadoop
def main():
    reducer()

main()
