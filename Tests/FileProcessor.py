import os
from shutil import copyfile

class FileProcessor:
    '''A File Processor class to list and copy files and folders'''
    
    def __init__(self, inputPath, destinationPath = None):
        self.Report = ''
        self.__CopyEnabled = False
        self.inputPath = self.__getAbsolutePath(inputPath) 
        self.__setDestinationPath(destinationPath)
        self.__InitializeReport()

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

            self.__ProcessDirectories(root, directories, destinationRoot)
            self.__ProcessFiles(files, root, destinationRoot)

    def __ProcessFiles(self, files, root, destinationRoot):
        for file in files:
            success = 'OK'
            if self.__CopyEnabled:
                src = os.path.join(root, file)
                dst = os.path.join(destinationRoot, file)
                try:
                    copyfile(src, dst)
                except:
                    success = 'ERROR'                 

            self.__ReportFile(root, file, success)

    def __ReportFile(self, root, file, success):

        textToAdd = '\n'
        if self.__CopyEnabled:
            textToAdd += success
            textToAdd += '\t'
        textToAdd += os.path.join(root, file)

        self.__AddToReport(textToAdd)        
    
    def __AddToReport(self, textToAdd):
        self.Report += textToAdd
        print(textToAdd)
        if self.__CopyEnabled:
            reportPath = os.path.join(self.destinationPath, "Report.txt")
            text_file = open(reportPath, "a+")
            text_file.write(textToAdd)
            text_file.close()

    def __InitializeReport(self):
        self.Report = ''
        if self.__CopyEnabled:
            reportPath = os.path.join(self.destinationPath, "Report.txt")
            text_file = open(reportPath, "w")
            text_file.write('')
            text_file.close()

    def __ProcessDirectories(self, root, directories, destinationRoot):
        for directory in directories:
            self.__ReportFile(root, directory, 'OK')

            if self.__CopyEnabled:        
                dst = os.path.join(destinationRoot, directory)
                self.__makeDir(dst)

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
            textToAdd = ''
            if self.__CopyEnabled:
                textToAdd += 'OK\t'
            textToAdd += self.inputPath
            self.__AddToReport(textToAdd)
            return True
        else:
            textToAdd = ''
            textToAdd += "[Error: Path does not exist] "
            textToAdd += self.inputPath
            self.__AddToReport(textToAdd)
            return False