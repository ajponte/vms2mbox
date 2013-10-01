#!/usr/bin/env/python3

"""
vms2mbox.py
Created by Alan Ponte on 10/1/2013.
DESCRIPTION:  
	This script will convert vms mail format files to mbox files.
	The script will be run from the command line.  
	The user will input the desired vms file.  
	The resulting mbox file will be stored in the directory the script is run from.
"""

import inspect
import os
import re
import sys
import scanner

#####################################################
# Quick and dirty lambda functions to get user input
#####################################################
getFileName = lambda : input("Enter file name, inclusing extension")

def getInputFile(fileName):
    """Gets and returns the vms FILE the user wishes to convert."""
    file = None
    try:
        file = open(fileName)
    except IOError:
        print("Can not find ", fileName)
    return file
    

	
def convert():
    """Main convert function.  Will convert the file to mbx"""
    vmsFile = getInputFile(getFileName)
    #Still needs methods for conversion
    return None
def main():
	"""Main Function.  Will run the script."""
	if __name__ == "__main__":
		main()
	
