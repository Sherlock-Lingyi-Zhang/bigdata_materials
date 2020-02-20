# Lab 0 - Essential Linux Commands (Solution)

## 1. Navigate the file system

```bash
# to show your current directory
pwd 
# show the content of the current directory, and tell their types
ls -l 
```
You can tell by color: green (executable), blue (directory), white (regular file).  If you use `ls -l`, you can tell by the first column file attributes: a directory start with `d`, a file starts with `-`, an executable file has attribute `x`. 

```bash
cd training_materials
# find data_mgmt
find . -name "data_mgmt"
# cd, using tab after the first few letters
cd training_materials/analyst/exercises/data_mgmt/
# to find what's in it
ls
# copy to vagrant
cp loyalty_data.txt /vagrant
# verify
ls /vagrant
# then verify from windows, look in c:/vagrant

# make a directory
mkdir data
# copy all files from  `~/training_materials/analyst/data` to this directory
cp $ADIR/data/*.txt data
# verify 
ls -l data
# delete dir
rm -r data
```

## 2. View/handle text files


```bash
cd $ADIR/data 
ls -lh 

# display the file interactively 
less ad_data1.txt  # space for next page, page up/down, and q to quit

# take first 100 rows from ad_data1.txt and save it as ad500.txt
head -n 500 ad_data1.txt > ad500.txt

# find lines with REVIEW from the text, view it screen by screen
grep "REVIEW" ad_data1.txt | less

# find how many lines with REVIEW in the text
grep "REVIEW" ad_data1.txt | wc -l
# 234 lines

```

## 3. Basic use of `vi` (optional)
```bash
vi ad500.txt
# use arrow keys or page up/down to go up/down.
:/linux  # to search linux
:/  # to search again
:i  # to enter edit mode
# delete linux at the cursor and replace it with unix
ESC  # to exit edit mode
:q!  # quit without saving

# first start vi
vi
:i # to insert
# type the poem
ESC
:w poem.txt # to write to a new file
:q # to quit vi

# verify
cat poem.txt
```