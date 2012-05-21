"""
This script replaces underscores with blank spaces
in filenames.

It takes an input directory path in the command line,
the directory and its subdirectories are scanned,
and filetypes of pdf, djvu, txt, epub, chm or mp3
can have their underscores replaced.

The user may verify the look of the filenames
before renaming them. The user may also modify
this script to include additional file types.

To use the script in Windows:

    *run the command prompt
    *type the name of the script and the desired directory

    e.g.:

        cmd >> script.py c:\ebooks
    

Original Date:   12 / 28 / 2011
"""

import sys, os

# function returns string
# with underscore replaced
# with a blank space
def replaceUnderscore(string):
    return string.replace('_', ' ')

# function prints a list
def printList(aList):
    for each in aList:
        print each
    print "\n"

# check input arg count
if len(sys.argv) != 2:
    print "Windows Usage: [cmd >> script.py directory\path], terminating..."
    sys.exit()

# get input dir path
dirpath = sys.argv[1]

# check input dir path
if not os.path.isdir(dirpath):
    print "Entered directory path does not exist, terminating..."
    sys.exit()
    


# create lists of valid files and
# their paths in given dir and subdirs
fileList = []
pathList = []

for root, dirs, files in os.walk(dirpath):
    for name in files:

        # filename must have underscore and following extensions
        # splitext() returns a tuple, [-1] captures the second
        # entry of the tuple being the extension
        if '_' in name and os.path.splitext(name)[-1] in ('.pdf', '.txt', '.epub',  # user may add additional file
                                                          '.chm', '.djvu', '.mp3'): # extensions within parenthesises

                # save the filename
                fileList.append(name)

                # save the path
                pathList.append(root)
                                
# count and show files to be changed to user              
print "\nThere are ", len(fileList), " files that meet the conditions.\n"
print "List of files to change:\n"
printList(fileList)

# show the paths
print "List of paths:\n"
printList(pathList)
 
# remove underscores, save the names to a new list, and print
print "Replacing underscores, verify this is how the filenames should look: \n"
modifiedFileList = map(replaceUnderscore, fileList)   
printList(modifiedFileList)

# ask user to rename files
userInput = raw_input("Would you like to rename these files? Enter 'y' or 'n': \n")

# check user input and perform the appropriate action
if len(userInput) != 1:
    
    print "Enter only one letter next time, terminating..."
    sys.exit()

# user wants to rename    
elif userInput == "y":

    # create oldpath and newpath from saved information
    for p, f, m in zip(pathList, fileList, modifiedFileList):
        oldpath = os.path.join(p, f)
        newpath = os.path.join(p, m)

        # attempt to rename
        try:
            os.rename(oldpath, newpath)
        except OSError as e:
            print >> sys.stderr, "Error renaming '%s' : %s" %(oldpath, e.strerror)
                    

    print "**File names have had underscores replaced with spaces**"
    sys.exit()

# user does not want to rename
elif userInput == "n":
    
    print "File names remained unchanged, terminating..."
    sys.exit()

# user entered invalid input
else:
    
    print "Invalid input, terminating..."
    sys.exit()
