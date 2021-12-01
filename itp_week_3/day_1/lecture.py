# ITP Week 2 Day 4 Lecture

#-------DATA STRUCTURES---------
# - Tuple: Ordered, unchangeable, and INDEXED Allows duplicate members.
#SYNTAX:
gardenPlants = ("lettuce", "raspberry", "cauliflower")

#Access item:
print(gardenPlants[1])

# - Set: Sets are used to store multiple items in a single variable.  Unordered and unindexed. No duplicate members.  
#SYNTAX:

myImmediateFamily = {"Karen", "Jeff", "Kyle", "Myles"}

#You must use a for-in loop to access items.
for member in myImmediateFamily:
    print(member)

#You CAN add values to a set using the add() method
myImmediateFamily.add("Adopted")

print(myImmediateFamily)

#----------MODULES------------
# The modules that come with Python are called the standard library, but you can also install third-party modules using the pip tool.

#You can import modules and get access to new functions.

#---------USING PATHS TO CONNECT THINGS----------
#Absolute Path: Absolute path specifies the location from the root directory.

#This is the ABSOLUTE path to this file on my computer:
#  /Users/tylerpritchard/Desktop/VIT/day_3/lecture.py

#Relative Path: A relative path is related to the current directory

#This is the RELATIVE path to this file on my computer:
#  day_3/lecture.py


#--------------IMPORTING MODULES---------
#Use the "import" keyword to bring outside functions/programs into the file you are currently working on.  For example, to add additional math functionality to your file, import the "math" module.
import math

#Now you can use math functions that were not previously available, like:

num1 = math.sqrt(16)
print("num1 is ", num1)

num2 = math.pi
print("num2 is ", num2)

tip = math.sinh(num2)
print(tip)

#-----------GIT & GITHUB-------------

#     GIT IS NOT THE SAME AS GITHUB!!!!!!!!!

#A .git file is created in your folder when git is initialized (the command to do a simple git intializtion is "git init", but we're not using that today).

#GitHUB is an online service which hosts code IN TEXT FORM.  It does NOT run any programs.  It is used by individuals to save their code to the cloud, and teams use it to work on large applications where individuals are responsible for different parts.

#Your computer has a lot of files.  You don't want to upload ALL of them, so you use the "git add ." from within the folder you would like Git to track. (The "." indicates "all of the files in the folder")

#After you have told your computer which files to keep track of, you will need to commit your files in order to prepare them to be sent to github.  This is also the point that you can think of as "saving your game".  You will need to add a message describing the changes you've made, so the syntax will look like:
#git commit -m "I just changed some stuff"

#After your changes have been saved, you may now push it to github using the "git push" command 

#---------HOW TO USE OTHER CODE---------
#Go to the repository on github that you would like to copy.  In our case it will be:
# https://github.com/Vets-In-Tech/itp_week_2

# In the top right corner, select the "fork" button.
# Once the repository has been copied to your account, go to it and click on the green "Code" button.  A dropdown menu will appear.  Select the clipboard.

#Back in your terminal, open the directory you would like to clone the repository to.  Enter:
#git clone https://github.com/Vets-In-Tech/itp_week_2

#This should clone the repository.  Now you know how to fork, clone, add, commit, and push.  But what about updating your local files with the changes from github?  The command is:
#git pull

#You can also use the git tools in the lefthand toolbar (it's the icon with the three circles and two lines)