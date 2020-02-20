# Lab 0 - Essential Linux Commands

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/00-Linux/lab0.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

This lab builds on the practice exercises in this module. Using this lab, we let you familiarize with common tasks using a combination of Linux commands. In this lab, we also introduce you to the `vi` editor. 

**Prerequisites**: please complete all the practices for this module.

## 1. Navigate the file system

- View your current directory
- list files and directories in the home directory, which ones are directories, files, and executable files?
- cd `training_materials`, find a folder name called `data_mgmt`
- cd `data_mgmt`, try the tab-completion technique
- copy one of the text files to your vagrant folder.
- verify that the text file is available from your windows host
- then delete the text file from vagrant folder
- create a new directory "data" in "data_ingest"
- copy all the text file from `$ADIR/data` to this directory
- then delete the directory

## 2. View/handle text files

- Go to the data folder for exercises `$ADIR/data`.
- Using a command to find out the size of the `ad_data1.txt` file
- display the file content interactively on screen
- take first 100 rows from `ad_data1.txt` and save it as `ad500.txt`
- from the file `ad_data1.txt`, find lines with "REVIEW" in the text, viewing results screen by screen
- find how many lines with REVIEW in `ad_data1.txt`

## 3. Basic use of `vi` (optional)

`vi` is a power text editor for Linux but it has a steep learning curve. Familiarize yourself with the following basic `vi` commands:

To use `vi`, type `vi` to open a blank file, `vi filename` to open an existing file (or create a new one with this name).

`vi` makes a distinction between *edit* mode and *command* mode. At first, you are in the command mode where your typing is interpreted as commands. Type `i` to enter the editing/insertion mode, where your type is interpreted as entering text. 

**Use ESC to exit the editing mode (remember this!)**

In the command mode, you can type `:q` to quit the editor, `:wq` to save and quit, **`:q!` to exit without saving changes**, `:w filename` to save text as a file. `dd` to delete the current line. `/text` to search for "text", `/` to search the next appearance of "text", `:%s/text1/text2/`  to search for "text1" and replace it with "text2".

- use `vi` to compile a new file with the following poem and save it as `poem.txt`. 
    ```
    you fit into me
    like a hook into an eye

    a fish hook
    an open eye
    ```
- Verify the content of `poem.txt`
- use `vi` to open `ad500.txt`, go up and down, and search for the first and second appearances of "linux" 
- replace the second `linux` to `unix` (hint: you need to enter and exit the edit mode).
- quit without saving

- Clean up ourselves by deleting `poem.txt` and `ad500.txt`

