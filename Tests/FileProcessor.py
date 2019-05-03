import os
from shutil import copyfile

class FileProcessor:
    '''A File Processor class to list and copy files and folders'''

    def __init__(self, inputPath, destinationPath = None):
        self.Report = ''
        self.__CopyEnabled = False
        self.inputPath = self.__getAbsolutePath(inputPath) 
        self.__setDestinationPath(destinationPath)

    def __setDestinationPath(self, destinationPath):
        if destinationPath is not None:
            self.__CopyEnabled = True
            self.destinationPath = self.__getAbsolutePath(destinationPath)                
        else:
            self.destinationPath = None

    def __getAbsolutePath(self, path):
        escapedBackslash = "\\"
        if path.startswith(escapedBackslash):
            return os.getcwd() + path
        else:
            return path

    def Run(self):
        if(self.__ValidateInputPath()):
            self.__Run()
    
    def __makeDir(self, path):
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    def __Run(self):
        destinationRoot = self.destinationPath
        for root, directories, files in os.walk(self.inputPath):   

            if self.__CopyEnabled:                
                destinationRoot = self.__GetDestinationRoot(root)                
                self.__makeDir(destinationRoot)             

            for directory in directories:
                self.Report += '\n'
                self.Report += os.path.join(root, directory)

                if self.__CopyEnabled:        
                    dst = os.path.join(destinationRoot, directory)
                    self.__makeDir(dst)

            for file in files:
                self.Report += '\n'
                self.Report += os.path.join(root, file)

                if self.__CopyEnabled:
                    src = os.path.join(root, file)
                    dst = os.path.join(destinationRoot, file)
                    copyfile(src, dst)

    def __GetDestinationRoot(self, inputRoot):
        relativeRoot = inputRoot.replace(os.path.split(self.inputPath)[0], '')
        if relativeRoot is '':
            destinationRoot = os.path.join(self.destinationPath, os.path.split(inputRoot)[1])
        else:
            escapedBackslash = "\\"
            destinationRoot = os.path.join(self.destinationPath, relativeRoot.strip(escapedBackslash))
        return destinationRoot

    def __ValidateInputPath(self):
        if(os.path.isdir(self.inputPath)):
            self.Report = self.inputPath
            return True
        else:
            self.Report += "[Error: Path does not exist] "
            self.Report += self.inputPath
            return False