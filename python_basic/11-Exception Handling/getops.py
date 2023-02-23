import sys                                                   
# importing getopt module                           
import getopt, os    

def usage():
    print('\ngetops.py -f first_name | -d second_name | -h help')

def full_name():   
    first_name = None  
    last_name = None  
    
    argv = sys.argv[1:]   
    try:   
        options, remainder = getopt.getopt(argv, "f:l:h",[ " first_name = " , " last_name = ", "help=" ] )   
    
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in options:  
        if opt in [ '-f' , '--first_name']:   
            first_name = arg   
        elif opt in [ '-l' ,'--last_name'] :   
            last_name = arg   
        elif opt in ['-h', '--last_name']:
            usage()
full_name()
