import unittest
import os
import sys
import shutil

from FileProcessor import FileProcessor

class FileProcessorListFileTest(unittest.TestCase):

    def test_FileProcessorListFile_PathNotExist(self):
        inputFolder = r"\SD\DoesNotExist"

        expectedReport = ["[Error: Path does not exist] " + os.getcwd() + r"\SD\DoesNotExist"]

        self.__testFileProcessorListing(inputFolder, expectedReport)

    def test_FileProcessorListFile_Run_EmptyFolder(self):

        inputFolder = r"\Tests\SD\EmptyFolder"
        
        expectedReport = [
            os.getcwd() + r'\Tests\SD\EmptyFolder',]
        
        self.__testFileProcessorListing(inputFolder, expectedReport)

    def test_FileProcessorListFile_Run_FolderWithFile(self):

        inputFolder = r"\Tests\SD\FolderWithFile"
        
        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFile',
            os.getcwd() + r'\Tests\SD\FolderWithFile\Text1.txt']
        
        self.__testFileProcessorListing(inputFolder, expectedReport)

    def test_FileProcessorListFile_Run_FolderWithFileAndEmptyFolder(self):

        inputFolder = r"\Tests\SD\FolderWithFileAndEmptyFolder"

        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\EmptyFolder',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\Text1.txt']
        
        self.__testFileProcessorListing(inputFolder, expectedReport)

    def test_FileProcessorListFile_Run_FolderWithFileAndSubFolderUntileLevel3(self):

        inputFolder = r"\Tests\SD\FolderWithFileAndSubFolderUntileLevel3"

        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\Level1.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\SubFolderLevel2',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\Level2a.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\Level2b.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\SubFolderLevel2\Level3a.txt',
            os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderUntileLevel3\SubFolderLevel1\SubFolderLevel2\Level3b.txt',]
        
        self.__testFileProcessorListing(inputFolder, expectedReport)

    def __testFileProcessorListing(self, inputFolder, expectedReport):
        fileLister = FileProcessor(inputFolder)
        fileLister.Run()
        print(fileLister.fileListReport)
        
        actualReport = fileLister.fileListReport.splitlines()
        self.assertEqual(len(expectedReport), len(actualReport), "fileListReport does not contain the expected number of entries.")
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")

if __name__ == '__main__':
    unittest.main()