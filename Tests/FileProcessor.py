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
    
    def __ListFiles(self):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.inputPath):
            for directory in d:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, directory)

            for file in f:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, file)

                if self.destinationPath is not None:
                    src = os.path.join(r, file)
                    directoryName = os.path.split(r)[1]
                    dst = os.path.join(self.destinationPath, directoryName, file)
                    copyfile(src, dst)

    def CheckPath(self):
        if(os.path.isdir(self.inputPath)):
            self.fileListReport = self.inputPath

            if self.destinationPath is not None:             
                # create the directory in the destination folder
                directoryName = os.path.split(self.inputPath)[1]
                copiedDirectory = os.path.join(self.destinationPath, directoryName)
                os.mkdir(copiedDirectory)

            return True
        else:
            self.fileListReport += "[Error: Path does not exist] "
            self.fileListReport += self.inputPath
            return False