# Python version
I used this repository with python 3.6.7
Probably it works with other python 3.X versions. No standard libraries are used.

# upload.py
Move files to Leonardo file storage for Machine Learning

## parameters
### -b / --base_dir
file path moved from

### -tr / --training 
Number of files to be uploaded for training

### -v / --validation 
Number of files to be uploaded for validation

### -t / --test 
Number of files to be uploaded for test

### -u / --upload
Target path to upload in Leonardo
Just display cf commands and no run

# divide.py
Divide files into directories for uploading files

## parameters
### -b / --base_dir
file path moved from

### -d / --direcotry 
Number of directory to create/ save files

### -f / --file
Number of files to be saved

### -u / --upload
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