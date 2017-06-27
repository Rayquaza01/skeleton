#!/usr/bin/env python3
import os
import shutil
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("skeltype", help="The file type of the skeleton")
ap.add_argument("skelname", help="The name of the skeleton file", nargs="?")
ap.add_argument("-n", "--name", help="The file name of the destination "
                "file", nargs="?")
opts = ap.parse_args()
skelDir = os.path.dirname(__file__) + "/skeletons"
curDir = os.getcwd()
skelType = opts.skeltype
if opts.skelname is not None:
    skelName = opts.skelname
else:
    skelName = ""
skelFile = ".".join([skelName, skelType])
skelPath = "/".join([skelDir, skelFile])
if os.path.isfile(skelPath):
    shutil.copy(skelPath, curDir)
else:
    print("Could not find the skeleton file specified.")
if opts.name is not None:
    destPath = "/".join([curDir, skelFile])
    destName = ".".join([opts.name, skelType])
    os.rename(destPath, destName)
