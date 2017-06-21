#!/usr/bin/env python3
import os
import shutil
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("skeltype", help="The file type of the skeleton")
ap.add_argument("skelname", help="The name of the skeleton file", nargs="?")
opts = ap.parse_args()
skelDir = os.path.dirname(__file__) + "/skeletons"
curDir = os.getcwd()
skelType = opts.skeltype
if opts.skelname is not None:
    skelName = opts.skelname
else:
    skelName = ""
skelFile = ".".join([skelName, skelType])
finalPath = "/".join([skelDir, skelFile])
try:
    shutil.copy(finalPath, curDir)
except:
    print("Could not find the skeleton file specified.")
