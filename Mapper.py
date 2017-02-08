#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip('')
    descs = line.split(',')
    for desc in descs:
        print '%s\t%s' % (descs[4],1)

