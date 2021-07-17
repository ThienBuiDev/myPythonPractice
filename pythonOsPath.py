import os
# os.chdir('c:\\')
print(os.getcwd())
print(os.path.abspath(r'newPython.py'))
print(os.path.relpath(r'C:\Users\Nhat Bui\Downloads\Visual Studio Code\python\me.py',r'c:\Users\NhatBui\asd'))
print(os.path.dirname(r'C:\Users\Nhat Bui\Downloads\Visual Studio Code\python\me.py'))
print(os.path.basename(r'C:\Users\Nhat Bui\Downloads\Visual Studio Code\python\me.py'))
for filename in os.listdir():
    if filename.endswith('.txt') # check file with the desired extension
os.makedirs(r'newpo')