import shutil
import os
# os.mkdir('folderToMoveTo')
shutil.copy('text.txt',r'folderToMoveTo\text2.txt') #copy file
shutil.copytree #copy folder
shutil.move #cut instead of copy, also used to rename the file

os.unlink('text.txt') #deleting file
os.rmdir() #deleting folder, folder has te be empty
shutil.rmtree('folderToBeDeleted') #deleting folder, it doesnt have to be empty