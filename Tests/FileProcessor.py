import os
from shutil import copyfile

class FileProcessor:
    '''A File Processor class to detect files and folders.'''

    def __init__(self, inputPath, destinationPath = None):
        self.__setInputPath(inputPath) 
        self.__setDestinationPath(destinationPath)

        self.fileListReport = ''

    def __setInputPath(self, inputPath):
        escapedBackslash = "\\"
        if(inputPath.startswith(escapedBackslash)):
            self.inputPath = os.getcwd() + inputPath
        else:
            self.inputPath = inputPath

    def __setDestinationPath(self, destinationPath):
        escapedBackslash = "\\"
        if destinationPath is None or destinationPath.startswith(escapedBackslash) is False:
            self.destinationPath = destinationPath
        else:
            self.destinationPath = os.getcwd() + destinationPath

    def Run(self):
        if(self.CheckPath()):
            self.__ListFiles()
    
    def __makeDirIfDoNotExist(self, path):
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    def __ListFiles(self):

        destinationRoot = self.destinationPath
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.inputPath):
            
            if self.destinationPath is not None:
                #relativeRoot = r.replace(self.inputPath, '')
                
                relativeRoot = r.replace(os.path.split(self.inputPath)[0], '')
                #relativeRoot = os.path.join(os.path.split(os.path.split(r)[0])[1],os.path.split(r)[1])
                if relativeRoot is '':
                    destinationRoot = os.path.join(self.destinationPath, os.path.split(r)[1])
                else:
                    escapedBackslash = "\\"
                    destinationRoot = os.path.join(self.destinationPath, relativeRoot.strip(escapedBackslash))
                
                self.__makeDirIfDoNotExist(destinationRoot)                

            for directory in d:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, directory)

                if self.destinationPath is not None:        
                    dst = os.path.join(destinationRoot, directory)
                    self.__makeDirIfDoNotExist(dst)

            for file in f:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, file)

                if self.destinationPath is not None:
                    src = os.path.join(r, file)
                    dst = os.path.join(destinationRoot, file)
                    copyfile(src, dst)

    def CheckPath(self):
        if(os.path.isdir(self.inputPath)):
            self.fileListReport = self.inputPath

            return True
        else:
            self.fileListReport += "[Error: Path does not exist] "
            self.fileListReport += self.inputPath
            return False