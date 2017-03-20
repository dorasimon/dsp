# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > pwd: show current working directory path  
mkdir directory name: creating a directory  
rm -rf directory name: deleting a directory  
touch file name: creating a file  
rm <file name>: deleting a file  
mv file name: renaming a file  
ls -a: listing hidden files
cp file name directory name: copying a file  
pushd directory name, popd directory name: switching to another directory back and forth  
find directory name -name "file name" -print: looking for a file in a directory  
grep "something" file name: looking for something in a file  
cat file name: streaming a file to the screen

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls: listing out the contents of the directory  
ls -a: listing out all the contents including hidden files  
ls -l: listing in long format  
ls -lh: listing in long format and showing sizes in human readable format  
ls -lah: listing all including hidden files in long format and showing sizes in human readable format  
ls -t: listing by modification time, newest first  
ls -Glp: listing with "/" appended to directories in long format, don't print group names

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -r, ls -t, ls -1, ls -R, ls -x

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs builds and executes command lines from standard input.  
find . -name "*.md" | xargs grep Python