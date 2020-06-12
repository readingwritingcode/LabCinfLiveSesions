#!/usr/bin/python3

import os
import sys

for i, j, k in os.walk(sys.argv[1]):
    for l in k:
       with open(os.path.join(i,l), "r") as h:
            print(h.read())
