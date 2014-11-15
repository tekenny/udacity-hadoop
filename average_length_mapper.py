#!/usr/bin/python
"""
"id"    "title" "tagnames"      "author_id"     "body"  "node_type"     "parent_id"     "abs_parent_id" "added_at"      "score" "state_string"  "last_edited_id"        "last_activity_by_id"   "last_activity_at"      "active_revision_id"    "extra" "extra_ref_id"  "extra_count"   "marked"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1"
"""

import csv
import sys

def mapper():
    # Using CSV reader and writer to simplify input/output
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        # Only process lines that have the expected number of fields
        if len(line) == 19:
            body          = line[4]
            node_type     = line[5]
            if node_type == 'question':
                id        = line[0] # id
            elif node_type == 'answer':
                id        = line[7] # abs_parent_id
            else:
                continue
            writer.writerow([id, node_type, len(body)])

# The following is to be able to test outside of hadoop
def main():
    mapper()

main()
