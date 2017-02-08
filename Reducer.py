#!/usr/bin/env python
import sys

current_desc = None
current_count = 0
desc = None

for line in sys.stdin:
    line = line.strip()
    desc, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    if current_desc == desc:
        current_count += count
    else:
        if current_desc:
            # write result to STDOUT
            print '%s\t%s' % (current_desc, current_count)
        current_count = count
        current_desc = desc

if current_desc == desc:
    print '%s\t%s' % (current_desc, current_count)

