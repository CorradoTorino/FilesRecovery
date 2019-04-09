import unittest
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

class FileProcessorTest(unittest.TestCase):

    def test_FileProcessorListFile_Constructor(self):
        fileLister = FileProcessor(r"\SD\Folder1")
        self.assertEqual(fileLister.fileListReport, "")

    def test_FileProcessorListFile_PathNotExist(self):
        fileLister = FileProcessor(r"\SD\DoesNotExist")
        fileLister.Run()
        self.assertEqual(fileLister.fileListReport, "[Error: Path does not exist] " + os.getcwd() + r"\SD\DoesNotExist", "Incorrect Report generated.")

    def test_FileProcessorListFile_Run(self):
        fileLister = FileProcessor(r"\Tests\SD\Folder1")
        fileLister.Run()
        expectedReport = [
            os.getcwd() + r'\Tests\SD\Folder1',
            os.getcwd() + r'\Tests\SD\Folder1\Text1.txt']
        actualReport = fileLister.fileListReport.splitlines()
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

    def test_FileProcessorListFile_Run_FolderWithFileAndEmptyFolder(self):
        fileLister = FileProcessor(r"\Tests\SD\FolderWithFileAndEmptyFolder")
        fileLister.Run()

        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\EmptyFolder',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\Text1.txt']
        actualReport = fileLister.fileListReport.splitlines()
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

    def test_FileProcessorListFile_Run_FolderWithFileAndSubFolderUntileLevel3(self):
        fileLister = FileProcessor(r"\Tests\SD\FolderWithFileAndSubFolderUntileLevel3")
        fileLister.Run()

        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\Level1.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\SubFolderLevel2',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\Level2a.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\Level2b.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\SubFolderLevel2\Level3a.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\SubFolderLevel2\Level3b.txt',]
        actualReport = fileLister.fileListReport.splitlines()
        self.assertEqual(len(expectedReport), len(actualReport), "fileListReport does not contain the expected number of entries.")
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

if __name__ == '__main__':
    unittest.main()