import os
from datetime import datetime

#create folder
if os.path.exists('test'):
    print("test folder exists")
else:
    os.mkdir('test')
    print("test folder created")


#create a folder path
folder = 'a/b/c/d/e/f/g'
if os.path.exists(folder):
    print('path exists')
else:
    os.makedirs(folder)
    print('path created')


#delete file
if os.path.exists('faltu.txt'):
    os.unlink("faltu.txt")
    print("faltu.txt deleted")
else:
    print("faltu.txt does not exist")

#delete folder.....(folder must be empty)
if os.path.exists('test'):
    os.rmdir("test")
    print('folder deleted')
else:
    print("test folder DNE")

#display file details
if os.path.exists('basics/hello.py'):
    size = os.path.getsize('basics/hello.py')
    ctime = os.path.getctime('basics/hello.py')
    mtime = os.path.getmtime('basics/hello.py')
    isfile = os.path.isfile('basics/hello.py')
    isdir = os.path.isdir('basics/hello.py')
    print('filname = basics/hello.py')
    print('size = ',size, 'bytes')
    print('ctime = ',datetime.fromtimestamp(ctime))
    print('mtime = ',datetime.fromtimestamp(mtime))
    print('file hai ye?? = ',isfile)     #check for file
    print('folder hai ye?? = ',isdir)       #check for folder


#recursive display file tree

print("recursive display file tree")
for root, dirs, files in os.walk('.'):    # '.' used for current location
    print(f"folder is {root.upper()}")
    print('total folders are = ',len(dirs))
    print('files in this folder are = ',files)