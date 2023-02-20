import sys
import getopt


argv = sys.argv[1:]

print(argv)  
opts, args = getopt.getopt(argv, "f:l:")
print(opts,args)