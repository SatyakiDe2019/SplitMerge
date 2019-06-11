# Split-Merge Package

Splitting a large CSV file into multiple small csv files for better processing using Split features at your local disk & Merge will merge back to small files into one large file. This is a first sample version. 

### Limitations

As of now, this will create splitted file with the extension known as "_splitted_". Make sure that your original file should not contain the same naming pattern.

> Your source file name for example - customer_addr_20180112.csv
> Your split file name will will be given below: 
> 	1__customer_addr_20180112__splitted_.csv
> 	2__customer_addr_20180112__splitted_.csv
> 	N__customer_addr_20180112__splitted_.csv
> Where N would be any number based on the size of the file.
> Bye default, each chunk will contain at least 30000 or less number of records.

This requires pandas & regular expression package installed in your python environment.

Sample Code to use this library. You can name it as -> 

--------------------------------------------------------------------------------------
                         callSplitMergeFiles.py
--------------------------------------------------------------------------------------

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
		
--------------------------------------------------------------------------------------
                 End Of Sample Code - callSplitMergeFiles.py
--------------------------------------------------------------------------------------

> Bug Fix: 1. Module loading issue fixed.
>          2. Source & Target directory as per developer's choice.
> Dependancy Package: You need to install followig packages in order to run this package -
>
>                     pip install pandas