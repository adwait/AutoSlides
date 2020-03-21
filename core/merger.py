# TODO: add methods for
#       merger to single file by reolving 'input'
#       generate content tree for non-text content


import sys
import re

class Merger:

    mainpath = None
    mainfiletext = None
    
    def __init__(self):
        pass

    def loadfromstring(self, input, asl):
        self.mainpath = input
        mainfile = open(input)
        mainfiletext = mainfile.read()
        
    def getoutput(self):
        maindirpath = '/'.join(self.mainpath.split('/')[:-1])
        mainfilename = self.mainpath.split('/')[-1]
        return self.getlinkedfiles(maindirpath, mainfilename)

    def getlinkedfiles(self, dirpath, filename):
        
        # print(dirpath+filename)

        def cleaninput(file):
            file = file[7:-1].strip()
            if file.endswith('.tex'):
                pass
            else:
                file = file + '.tex'
            return file
        
        def cleaninclude(file):
            file = file[9:-1].strip()
            if file.endswith('.tex'):
                pass
            else:
                file = file + '.tex'
            return file
        

        relpath = dirpath + '/' + filename

        newdirpath = '/'.join(relpath.split('/')[:-1])
        newfilename = relpath.split('/')[-1]
        
        f = open(newdirpath + '/' + newfilename)
        ftext = f.read()

        inputreg = re.compile(r'\\input{[^{}]*}')
        includereg = re.compile(r'\\include{[^{}]*}')
        

        ftext = re.sub(inputreg, lambda x: self.getlinkedfiles(newdirpath, cleaninput(x.group())), ftext)
        ftext = re.sub(includereg, lambda x: self.getlinkedfiles(newdirpath, cleaninclude(x.group())), ftext)

        return ftext
