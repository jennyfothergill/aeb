#!/usr/bin/env python3

from collections import defaultdict
import random
import sys
import textwrap

acronym = sys.argv[1]

words = defaultdict(list)
for line in open("dictionary.txt"):
    words[line[0].lower()] += [line]


expanded = "".join([random.choice(words[i.lower()]) for i in acronym])
abesaying = [
    f"Back in my day {acronym} stood for {expanded}",
    f"You kids and your {expanded}",
    f"{acronym}? What would I do with a {expanded}?",
]

saythis = random.choice(abesaying)

print(","+"-"*35+".")

for line in textwrap.wrap(saythis,width=33):
    print(f"| {line: <33} |")

for line in open("abe.txt"):
    print(line, end="")
