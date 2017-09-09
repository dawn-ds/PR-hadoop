#!/usr/bin/python

# PageRank mapper function

import sys
import string

N = 925783; # total number of valid pages
VN = N; # label of the virtual node (pages are indexed from 0 to N-1)

for line in sys.stdin:
    # read each line from the input
    line = line.split("\n")[0];

    # pass along graph structure
    print line;

    key, val = line.split(","); # separate (key, value) pairs
    out_links = val.split("|"); # separate outgoing links with | as the delimiter

    # pass PageRank mass to neighbors
    p = float(out_links[0])/(len(out_links)-1); # first value in the list is the current PR
    for i in out_links[1:]:
        if int(i) == VN:
            continue; # ignore the VN
        print i + "," + str(p);
