import os,sys

f = sys.argv[1]

if os.path.exists(f):
    os.system(f)
    input("Press enter to return")