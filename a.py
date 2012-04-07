#!/usr/bin/env python

import cgitb

print "Content-Type: text/html"
print

try:
   f = open('non-existent-file.txt', 'r')
except:
   cgitb.handler()
