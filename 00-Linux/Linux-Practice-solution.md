
# Linux Command Line Practice Problems - Solution

## 1. Navigate the file structure

<iframe width="560" height="315" src="https://www.youtube.com/embed/UzcZ0ph9dsA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

```bash
# view present working directory
pwd

# list file in the current directory
ls 

# list files in the root directory
ls /

# list files in the vagrant folder
ls /vagrant

# cd vagrant folder
cd /vagrant

# cd the home directory
cd ~

# list files in the current directory
ls

# in the long form
ls -l

# cd the data directory: training_materials/analyst/data (use tab and double tab for auto-completion)
cd training_materials/analyst/data

# list files recurrsively in the long form
ls -lR

# cd your home directory
cd ~
```

##  2. Copy/paste/edit commands

<iframe width="560" height="315" src="https://www.youtube.com/embed/_DQxVuCMSpw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

```bash
# Clear the screen 
clear

# re-enter the data directory (re-use a previouse command)
# up arrow three times.

# copy the command and past it to notepad++
# use mouse to select the command to copy

# copy the command and paste it here in the prompt
# hit: Shift+insert  or right click

# add ~/ before the path
# Ctrl+A (Home) to the beging, arrow twice, and type

# delete the current command 
# Ctrl+e (End) to move to the end.
# Ctrl+u to delete
```


### 3. File Operations

<iframe width="560" height="315" src="https://www.youtube.com/embed/kyDI8bgUD6s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


```bash
# navigate to $ADIR/data and view its content
cd $ADIR/data
ls -l

# make a copy of README as readme2
cp README readme2

# make a new directory called dir1
mkdir dir1

# copy README to the newly created directory as readme2
cp README dir1/readme2

# repeat the previous command
# if the cp finds an existing file, it will ask
cp README dir1/readme2

# rename the readme2 to readme3
mv readme2 readme3

# move readme3 to home directory
mv readme3 dir1

# remove the readme2 from this directory
rm readme2

# remove the dir1 directory
rmdir dir1 # this will fail because it is not empty
rm -r dir1 
# or
rm dir1/*
rmdir dir

# find all ".txt" files in the current directory
find . -name "*.txt"
```

### 4. Handle large text files

<iframe width="560" height="315" src="https://www.youtube.com/embed/ygj3mzfRrMw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


```bash
# navigate to $ADIR/data and view file sizes
cd $ADIR/data

# display the content of fratings_2013.txt on screen
cat ratings_2013.txt

# repeat the previous but in a page-by-page fashion, and quit with q
less, # f/b, up/down to move up/down, q to quit
more # space to advance, q to quite

# display the first 10 rows of the file
head ratings_2013.txt

# display the last 20 rows of the file
tail -n 20 ratings_2013.txt

# find rows that contain the word "the" 
grep "the" ratings_2013.txt

# find rows that does not contain the word "the" - hint: use option -v
grep -v "the" ratings_2013.txt

# find rows that does not contain the word "the" (case insensitive)
grep -vi "the" ratings_2013.txt
```


### Practice 5: line count, grep


<iframe width="560" height="315" src="https://www.youtube.com/embed/yVTWT2K9yBo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

```bash
# enter 
cd $ADIR/exercises/data_mgmt 
ls -l 
# to get how many lines in the file.
wc -l loyalty_data.txt 
# 311 rows
less loyalty_data.txt 
# or
cat loyalty_data.txt | more 
```
to search the records with "GOLD" (any case),

```bash
# list records
grep -i 'GOLD' loyalty_data.txt  
# count the records
grep -i 'GOLD' loyalty_data.txt | wc -l
# 52 rows
```

### Practice 6: redirection, sed, and vi

<iframe width="560" height="315" src="https://www.youtube.com/embed/14TuKQZG7rA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

```bash
cd $ADIR/data
# make a samples directory
mkdir samples
# take a 100 records as a sample
head -n 100 latlon.tsv > samples/latlon100.tsv
cd samples
# search \t and replace it with |, use g to replace all \t in the row.
sed "s/\t/|/g" latlon100.tsv > latlon100.txt
# verify it 
head latlon100.txt
#an alternative way of replacing is 
vi latlon100.tsv 
#then type 
:%s/\t/|/g  #to do a global search and replace. %s for replacing all lines, 
# and g for replacing all instance in the current line.
:w latlon100.txt # to save it as a new file.
:q! #to exit
# view a small sample
head latlon100.txtc
cd ..
ls -R
# save the result of ls -R to a file.
ls -R > samples/files.txt 
cd samples
# to view content of files.txt. there are many other ways to do so
less files.txt  
rm files.txt
cd ..
# recursively remove the samples folder and all of its content
rm -r samples
```