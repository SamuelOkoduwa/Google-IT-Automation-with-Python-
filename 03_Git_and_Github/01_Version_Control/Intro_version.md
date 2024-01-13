<h1>Version Control System</h1>

**Learnig Objectives**
- Describe the concept of version control and why it is important to use
- Utilize the diff and patch commands to automate differentiating and editing files
- Explain what Git is and its benefits of use
- Install Git on local machine
- Utilize Git to create and clone repositories, add code, check the status of code, and commit code

**Version Control System**
A version control system allows us to keep track of when and who did what changes to our files. Those can be code, configuration, images, or whatever else we need to track.

 **Comparing Different Files**
The diff tool shows all the differences between any type of file. By highlighting what’s changed, it helps us understand the changes and see how the files have been modified.

There are a lot of tools out there before version control to compare files. Diff is the most popular one, but not the only one available. For example, wdiff highlights the words that have changed in a file instead of working line by line like diff does. To help us even more, there are a bunch of graphical tools that display files side by side and highlight the differences by using color. Some examples of this include: meld, KDiff3, or vimdiff.

While diff is the command that generates the difference between two files, patch is the command that applies those differences to the original file.

The wdiff command highlights the words that changed in a file instead of working line by line.

**Git**
There are three sections: the Git directory, the working tree, and the staging area. 

**Git config command**
The Git config command is used to set the values to identify who made changes to Git repositories. To set the values of user.email and user.name to your email and name, type: 
:~$ git config  - -global user.email "me@example.com"

:~$ git config  - -global user.name "My name"

**Git init command**
:~/checks$ git int
The Git init command can create a new empty repository in a current directory or re-initialize an existing one. 

**Git ls -la command**
:~/checks$ ls -la
The Git ls - la command checks that an identified directory exists.  

:~/checks$ ls -l .git/
The ls-l.git command checks inside the directory to see the different things that it contains. This is called the Git directory. The Git directory is a database for your Git project that stores the changes and the change history.


**Git commit command**
:~/checks$ git commit
The .git commit command is run to remove changes made from the staging area to the .git directory. When this command is run, it tells Git to save changes. A text editor is opened that allows a commit message to be entered.


**Guidelines for writing commit messages**
A commit message is generally broken into two sections: a short summary and a description of the changes. When the git commit command is run, Git will open a text editor to write your commit message. A good commit message includes the following:
**Summary:** The first line contains the summary, formatted as a header, containing 50 characters or less. 
**Description:** The description is usually kept under 72 characters and provides detailed information about the change. It can include references to bugs or issues that will be fixed with the change. It also can include links to more information when relevant. 