'''
    This file will be the entry point of the application.
    The input check will be performed and then if everything is
    ok the internal execution will be initiated.
'''

import os, sys, getopt, glob, time
from core.hashtagAppExecution import Hashtager

# Check if the path exist
def verify_path(folder_path):

    if not os.path.exists(folder_path):
        raise Exception('The path: {} does not exist'.format(folder_path))
    
    if not glob.glob(os.path.join(folder_path, '*.txt')) :
        raise Exception('The given directory has no text files')
    
    return folder_path
        

# Check the structure of the input
def input_check(argv):
    
    try:
        opts, _ = getopt.getopt(argv,"d:")
    except getopt.GetoptError:
        print("hashtagApp.py -d <folder_path>")
        sys.exit(2)
    
    _, folder_path = opts[0]

    return folder_path

# Application entry point
if __name__ == "__main__":

    folder_path = input_check(sys.argv[1:])
    folder_path = verify_path(folder_path)

    hashtager = Hashtager()
    hashtager.find_hastags(folder_path)