import unittest

class FileProcessor:
    '''A File Processor class to detect files and folders.'''

    def __init__(self, path):
        self.path = path
        self.fileListReport = ''

    def Run(self):
        self.fileListReport = self.path

    def SimulateListFiles(self):
        self.fileListReport += "\n"
        self.fileListReport += "Text1.txt"

class FileProcessorTest(unittest.TestCase):

    def test_FileProcessorListFile_Run(self):
        fileLister = FileProcessor("/SD/Folder1")
        self.assertEqual(fileLister.fileListReport, "")

    def test_FileProcessorListFile_Constructor(self):
        fileLister = FileProcessor("/SD/Folder1")
        fileLister.Run()
        self.assertEqual(fileLister.fileListReport, "/SD/Folder1")

    def test_FileProcessorListFile_SimulateListFiles(self):
        fileLister = FileProcessor("/SD/Folder1")
        fileLister.Run()
        fileLister.SimulateListFiles()
        
        expectedReport = ['/SD/Folder1','Text1.txt']
        actualReport = fileLister.fileListReport.splitlines()
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

if __name__ == '__main__':
    unittest.main()