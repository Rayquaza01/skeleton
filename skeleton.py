#!/usr/bin/env python3
import os
import sys
import shutil
import argparse


def options():
    ap = argparse.ArgumentParser()
    ap.add_argument("skeltype", help="The file type of the skeleton", nargs=1)
    ap.add_argument("skelname", help="The name of the skeleton file", nargs="?")
    ap.add_argument("-n", "--name", help="The file name of the destination "
                    "file", nargs="?")
    return ap.parse_args()


def main():
    opts = options()
    skelDir = os.path.join(os.path.dirname(sys.argv[0]) + "skeletons")
    curDir = os.getcwd()
    skelType = opts.skeltype
    if opts.skelname is not None:
        skelName = opts.skelname
    else:
        skelName = ""
    skelFile = ".".join([skelName, skelType])
    skelPath = os.path.join([skelDir, skelFile])
    if os.path.isfile(skelPath):
        shutil.copy(skelPath, curDir)
    else:
        print("Could not find the skeleton file specified.")
    if opts.name is not None:
        destPath = os.path.join([curDir, skelFile])
        destName = ".".join([opts.name, skelType])
        os.rename(destPath, destName)


if __name__ == "__main__":
    main()
