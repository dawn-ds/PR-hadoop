#!/usr/bin/python

# PageRank reducer function

import sys

prev_key    = -1;
pr          = 0; # page rank variable
decay_f     = 0.85; # decay factor parameter
N           = 925783; # total number of valid pages
string      = ""; # string containing list of outgoing links

for line in sys.stdin:
    line        = line.replace("\n", ""); # removing the end of line character
    key, val    = line.split(","); # splitting  the line into (key, value) pairs
    key         = int(key); # converting key from string to int

    # condition to check if all the information regarding
    # a specific key (the key from previous iteration) has been obtained
    if (prev_key != key) and (prev_key != -1):
        pr = decay_f/N + (1-decay_f)*pr;
        print str(prev_key) + "," + str(pr) + string;

        # if the following condition is ever true, we cannot proceed with
        # the next iteration and we have to solve the issue first!
        if string.find("|") == -1:
            print "ERROR!! line = ", line, ", prev_key = ", prev_key, ", key = ", key

        # reset the variables
        pr = 0;
        string = "";

    # differentiate between a list of outgoing links and PageRank value
    links = val.split("|");
    if len(links) == 1:
        pr += float(val);
    else:
        M = links[1:];
        for i in M:
            string += "|"+str(i);

    # substitute the current key value with the prev_key value for next iteration
    prev_key = key;

# print the information for last step
if key == prev_key:
    print str(prev_key) + "," + str(pr) + string;
