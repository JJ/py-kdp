#!/usr/bin/env python

import pyexcel as p
import os
import sys

dir = "."
if len(sys.argv) == 2:
    dir = sys.argv[1]

for filename in os.listdir(dir):
    if filename.startswith("KDP ") or filename.startswith("Sales "):
        print( filename )
        sheet = p.get_sheet(file_name=dir+filename)
        print(sheet)
