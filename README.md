# SplitMerge
This project will provide you to split &amp; merge of any large CSV file using Python 3.7. Splitting a large CSV file into multiple small csv files for better processing using Split features at your local disk & Merge will merge back to small files into one large file. This is a first sample version. 
### Limitations
As of now, this will create splitted file with the extension known as "_splitted_". Make sure that your original file should not contain the same naming pattern.

> Your source file name for example - addr_det_20190101.csv
> Your split file name will will be given below: 
> 	1__addr_det_20180112__splitted_.csv
> 	2__addr_det_20180112__splitted_.csv
...
> 	N__addr_det_20180112__splitted_.csv
> Where N would be any number based on the size of the file.
> Bye default, each chunk will contain at least 30000 or less number of records.

