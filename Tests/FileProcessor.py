import os
from shutil import copyfile

class FileProcessor:
    '''A File Processor class to detect files and folders.'''

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
            self.__ListFiles()
    
    def __makeDir(self, path):
        try:
            os.mkdir(path)
        except FileExistsError:
            pass

    def __ListFiles(self):
        destinationRoot = self.destinationPath
        for roots, directories, files in os.walk(self.inputPath):
            
            if self.__CopyEnabled:
                
                relativeRoot = roots.replace(os.path.split(self.inputPath)[0], '')

                if relativeRoot is '':
                    destinationRoot = os.path.join(self.destinationPath, os.path.split(roots)[1])
                else:
                    escapedBackslash = "\\"
                    destinationRoot = os.path.join(self.destinationPath, relativeRoot.strip(escapedBackslash))
                
                self.__makeDir(destinationRoot)             

            for directory in directories:
                self.Report += '\n'
                self.Report += os.path.join(roots, directory)

                if self.destinationPath is not None:        
                    dst = os.path.join(destinationRoot, directory)
                    self.__makeDir(dst)

            for file in files:
                self.Report += '\n'
                self.Report += os.path.join(roots, file)

                if self.destinationPath is not None:
                    src = os.path.join(roots, file)
                    dst = os.path.join(destinationRoot, file)
                    copyfile(src, dst)

    def __ValidateInputPath(self):
        if(os.path.isdir(self.inputPath)):
            self.Report = self.inputPath
            return True
        else:
            self.Report += "[Error: Path does not exist] "
            self.Report += self.inputPath
            return False