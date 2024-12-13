#!/usr/bin/env python3

import sys
import textwrap

saythis = sys.argv[1]

print(","+"-"*35+".")

for line in textwrap.wrap(saythis,width=33):
    print(f"| {line: <33} |")

for line in open("abe.txt"):
    print(line, end="")
