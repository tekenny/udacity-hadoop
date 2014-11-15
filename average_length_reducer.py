#!/usr/bin/python

import csv
import sys 

def reducer():
    # Using CSV reader and writer to simplify input/output 
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    averageAnswerLength = 0
    questionLength      = 0
    totalAnswers        = 0
    totalLength         = 0
    lastKey = None
    for line in reader:
        if len(line) != 3: # skip bad data
            continue
    
        theKey     = line[0] 
        nodeType   = line[1]
        bodyLength = line[2]
        if lastKey and theKey != lastKey:
            # Write records for lastKey if theKey has changed
            if totalAnswers != 0:
                 averageAnswerLength = 1.0 * totalLength / totalAnswers
            writer.writerow([lastKey, questionLength, averageAnswerLength])
            averageAnswerLength = 0
            questionLength      = 0
            totalAnswers        = 0
            totalLength         = 0

        if nodeType == 'answer':
            # Tally answers
            totalAnswers += 1
            totalLength  += int(bodyLength)
        elif nodeType == 'question':
            # Store (parent) question length
            questionLength = int(bodyLength)
        lastKey = theKey

    # Must ensure the last record is written
    if lastKey != None:
        if totalAnswers != 0:
            averageAnswerLength = 1.0 * totalLength / totalAnswers
        writer.writerow([lastKey, questionLength, averageAnswerLength])
        
# The following is to be able to test outside of hadoop
def main():
    reducer()

main()
