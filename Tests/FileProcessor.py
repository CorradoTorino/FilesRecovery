import os

class FileProcessor:
    '''A File Processor class to detect files and folders.'''

    def __init__(self, path):
        start = "\\"
        if(path.startswith(start)):
            self.path = os.getcwd() + path
        else:
            self.path = path
        
        self.fileListReport = ''

    def Run(self):
        if(self.CheckPath()):
            self.__ListFiles()
    
    def __ListFiles(self):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for directory in d:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, directory)

            for file in f:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, file)

    def CheckPath(self):
        if(os.path.isdir(self.path)):
            self.fileListReport = self.path
            return True
        else:
            self.fileListReport += "[Error: Path does not exist] "
            self.fileListReport += self.path
            return False