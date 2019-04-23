import unittest
import os
import sys
from FileProcessor import FileProcessor

class FileProcessorTest(unittest.TestCase):

    def test_FileProcessorListFile_Constructor(self):
        fileLister = FileProcessor(r"\SD\Folder1")
        self.assertEqual(fileLister.fileListReport, "")

    def test_FileProcessorListFile_PathNotExist(self):
        fileLister = FileProcessor(r"\SD\DoesNotExist")
        fileLister.Run()
        print(fileLister.fileListReport)

        self.assertEqual(fileLister.fileListReport, "[Error: Path does not exist] " + os.getcwd() + r"\SD\DoesNotExist", "Incorrect Report generated.")

    def test_FileProcessorListFile_Run_FolderWithFile(self):
        fileLister = FileProcessor(r"\Tests\SD\FolderWithFile")
        fileLister.Run()
        print(fileLister.fileListReport)

        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFile',
            os.getcwd() + r'\Tests\SD\FolderWithFile\Text1.txt']
        actualReport = fileLister.fileListReport.splitlines()
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

    def test_FileProcessorListFile_Run_FolderWithFileAndEmptyFolder(self):
        fileLister = FileProcessor(r"\Tests\SD\FolderWithFileAndEmptyFolder")
        fileLister.Run()
        print(fileLister.fileListReport)

        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\EmptyFolder',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\Text1.txt']
        actualReport = fileLister.fileListReport.splitlines()
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

    def test_FileProcessorListFile_Run_FolderWithFileAndSubFolderUntileLevel3(self):
        fileLister = FileProcessor(r"\Tests\SD\FolderWithFileAndSubFolderUntileLevel3")
        fileLister.Run()
        print(fileLister.fileListReport)

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