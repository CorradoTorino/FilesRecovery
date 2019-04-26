import unittest
import os
import sys
import shutil

from FileProcessor import FileProcessor

class FileProcessorCopyFilesTest(unittest.TestCase):

    def test_FileProcessorCopyFilesTest_Run_EmptyFolder(self):

        inputFolder = r"\Tests\SD\EmptyFolder"
        outputFolder = r"\Tests\TestOuput"

        expectedReport = [
            os.getcwd() + r'\Tests\SD\EmptyFolder',]
        expectedReportForDestination = [
            os.getcwd() + r'\Tests\TestOuput',
            os.getcwd() + r'\Tests\TestOuput\EmptyFolder',]
        
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport, expectedReportForDestination)

    def test_FileProcessorCopyFilesTest_Run_FolderWithFile(self):
        
        inputFolder = r"\Tests\SD\FolderWithFile"
        outputFolder = r"\Tests\TestOuput"
        
        expectedReport = [
            os.getcwd() + r'\Tests\SD\FolderWithFile',
            os.getcwd() + r'\Tests\SD\FolderWithFile\Text1.txt']
        
        expectedReportForDestination = [
            os.getcwd() + r'\Tests\TestOuput',
            os.getcwd() + r'\Tests\TestOuput\FolderWithFile',
            os.getcwd() + r'\Tests\TestOuput\FolderWithFile\Text1.txt']
        
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport, expectedReportForDestination)

    def __cleanTestOuput(self):     
        testOuputDirectory = os.getcwd() + r"\Tests\TestOuput" 
        try:
            shutil.rmtree(testOuputDirectory)
        except FileNotFoundError:
            pass
        os.mkdir(testOuputDirectory)

    def __testFileProcessorCopying(self, inputFolder, outputFolder, expectedReport, expectedReportForDestination):
            self.__cleanTestOuput()

            fileCopier = FileProcessor(inputFolder, outputFolder)
            fileCopier.Run()
            print(fileCopier.fileListReport)
            
            actualReport = fileCopier.fileListReport.splitlines()
            self.assertEqual(len(expectedReport), len(actualReport), "fileListReport does not contain the expected number of entries.")
            self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")   

            self.__checkDirectoryTreeCopied(outputFolder, expectedReportForDestination)

    def __checkDirectoryTreeCopied(self, destinationFolder, expectedReport):
        fileLister = FileProcessor(destinationFolder)
        fileLister.Run()
        print(fileLister.fileListReport)
        
        actualReport = fileLister.fileListReport.splitlines()
        self.assertEqual(len(expectedReport), len(actualReport), "fileListReport does not contain the expected number of entries.")
        self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")   

if __name__ == '__main__':
    unittest.main()