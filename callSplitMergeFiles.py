###############################################
#### Written By: SATYAKI DE                ####
#### Written On: 10-Feb-2019               ####
#### Pandas, Regular Expression, gc        ####
#### needs to install in order to run      ####
#### this script.                          ####
####                                       ####
#### Objective: This script will           ####
#### call both the split & merge libraries ####
#### to simulate both the cases using      ####
#### large csv files.                      ####
###############################################

from SplitMerge.clsSplitFiles import clsSplitFiles
from SplitMerge.clsMergeFiles import clsMergeFiles
import re
import platform as pl
import os

def main():
    print("Calling the custom Package for large file splitting..")
    os_det = pl.system()

    print("Running on :", os_det)

    ###############################################################
    ###### User Input based on Windows OS                  ########
    ###############################################################

    srcF = str(input("Please enter the file name with extension:"))
    base_name = re.sub(r'[0-9]','', srcF)
    srcFileInit = base_name[:-5]

    if os_det == "Windows":
        subdir = "\\temp\\"
        path = os.path.dirname(os.path.realpath(__file__)) + "\\"
    else:
        subdir = "/temp/"
        path = os.path.dirname(os.path.realpath(__file__)) + '/'

    ###############################################################
    ###### End Of User Input                                 ######
    ###############################################################
    t = clsSplitFiles(srcF, path, subdir)
    ret_val = t.split_files()

    if ret_val == 0:
        print("Splitting Successful!")
    else:
        print("Splitting Failure!")

    print("-"*30)

    print("Finally, Merging small splitted files to make the same big file!")

    y = clsMergeFiles(srcFileInit, path)
    ret_val1 = y.merge_file()

    if ret_val1 == 0:
        print("Merge Successful!")
    else:
        print("Merge Failure!")

    print("-"*30)



if __name__ == "__main__":
    main()