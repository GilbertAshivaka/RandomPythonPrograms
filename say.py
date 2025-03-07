import cowsay 
import sys


if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
else:
    sys.exit("Type in a name.")



import cowsay
import sys
if len(sys.argv) ==2:
    cowsay.trex("Hello,"+sys.argv[1])
else:
    sys.exit("Type in something.")