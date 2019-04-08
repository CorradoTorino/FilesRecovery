import unittest
import os

class FileProcessor:
    '''A File Processor class to detect files and folders.'''

    def __init__(self, path):
        self.path = path
        self.fileListReport = ''

    def Run(self):
        self.fileListReport = self.path
        self.ListFiles()

    def SimulateListFiles(self):
        self.fileListReport += "\n"
        self.fileListReport += "/SD/Folder1/Text1.txt"
        
    def ListFiles(self):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                self.fileListReport += '\n'
                self.fileListReport += os.path.join(r, file)

class FileProcessorTest(unittest.TestCase):

    def test_FileProcessorListFile_Constructor(self):
        fileLister = FileProcessor("/SD/Folder1")
        self.assertEqual(fileLister.fileListReport, "")

    def test_FileProcessorListFile_PathNotExist(self):
        fileLister = FileProcessor("/SD/DoesNotExist")
        fileLister.Run()
        self.assertEqual(fileLister.fileListReport, "[Error: Path does not exist] /SD/DoesNotExist", "Incorrect Report generated.")

    def test_FileProcessorListFile_Run(self):
        fileLister = FileProcessor("/SD/Folder1")
        fileLister.Run()
        self.assertEqual(fileLister.fileListReport, "/SD/Folder1")

    def test_FileProcessorListFile_SimulateListFiles(self):
        fileLister = FileProcessor("/SD/Folder1")
        fileLister.Run()
        fileLister.SimulateListFiles()
        
        expectedReport = ['/SD/Folder1','/SD/Folder1/Text1.txt']
        actualReport = fileLister.fileListReport.splitlines()
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

if __name__ == '__main__':
    unittest.main()