import os
import shelve
myFile = open(r'.\text.txt')
content = myFile.read() #open the file in read-only mode
writeFile = open(r'.\text2.txt','w')
writeFileAppend = open(r'.\text3.txt','a')


# shelfFile = shelve.open('mydata') #return shelffile object
# shelfFile['cat'] = ['Zophie','Pooka','Simon','Fat-tail','Cleo']
# shelfFile.close()
writeFile.write("['Zophie','Pooka','Simon','Fat-tail','Cleo']")