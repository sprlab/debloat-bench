# load args from command line
import sys


l = len(sys.argv)

if l == 3:
    print("Test Passed")
else:
    print("The number of arguments is incorrect")

