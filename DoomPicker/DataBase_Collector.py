# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

import sys, os

def ripper(directory):
    DirectoryListing = sorted(os.listdir("G:\LEVELS\PWADS"))
    DirectoryListing = ["G:\LEVELS\PWADS" + s for s in DirectoryListing]
    return DirectoryListing
