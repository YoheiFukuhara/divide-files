# Purpose
Move files to sub directories for smaller chunk to upload Leonardo.


# divide-files
Divide files into directories for uploading files


# parameters
## -b / --base_dir
file path moved from

## -d / --direcotry 
Number of directory to create/ save files

## -f / --file
Number of files to be saved


## -u / --upload
Target path to upload in Leonardo
Just display cf commands and no run


```bash
# sample command
# only set "cf sapml fs push" target direcotry 
python divide.py -u fax/test/f1/
python divide.py -u fax/validation/f1/

# number of directory to create and save file in
python divide.py -u fax/training/f1/ -d 40
```