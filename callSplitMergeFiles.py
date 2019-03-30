import clsSplitFiles as t
import clsMergeFiles as cm
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

    x = t.clsSplitFiles(srcF, path, subdir)

    ret_val = x.split_files()

    if ret_val == 0:
        print("Splitting Successful!")
    else:
        print("Splitting Failure!")

    print("-"*30)

    print("Finally, Merging small splitted files to make the same big file!")

    y = cm.clsMergeFiles(srcFileInit)

    ret_val1 = y.merge_file()

    if ret_val1 == 0:
        print("Merge Successful!")
    else:
        print("Merge Failure!")

    print("-"*30)



if __name__ == "__main__":
    main()