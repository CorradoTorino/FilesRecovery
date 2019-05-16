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
            'OK\t' + os.getcwd() + r'\Tests\SD\EmptyFolder']
                          
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport)

    def test_FileProcessorCopyFilesTest_Run_FolderWithFile(self):
        
        inputFolder = r"\Tests\SD\FolderWithFile"
        outputFolder = r"\Tests\TestOuput"
        
        expectedReport = [
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFile',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFile\Text1.txt']
        
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport)

    def test_FileProcessorCopyFilesTest_Run_FolderWithFileAndEmptyFolder(self):

        inputFolder = r"\Tests\SD\FolderWithFileAndEmptyFolder"
        outputFolder = r"\Tests\TestOuput"
        
        expectedReport = [
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\EmptyFolder',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndEmptyFolder\Text1.txt']
        
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport)

    def test_FileProcessorListFile_Run_FolderWithFileAndSubFolderLevel3(self):

        inputFolder = r"\Tests\SD\FolderWithFileAndSubFolderLevel3"
        outputFolder = r"\Tests\TestOuput"

        expectedReport = [
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\SubFolderLevel1',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\Level1.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\SubFolderLevel1\SubFolderLevel2',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\SubFolderLevel1\Level2a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\SubFolderLevel1\Level2b.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\SubFolderLevel1\SubFolderLevel2\Level3a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSubFolderLevel3\SubFolderLevel1\SubFolderLevel2\Level3b.txt',]
        
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport)

    def test_FileProcessorListFile_Run_FolderWithFileAndSeveralSubFolderLevel3(self):

        inputFolder = r"\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3"
        outputFolder = r"\Tests\TestOuput"

        expectedReport = [
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\Level1.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1\SubFolderLevel2',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1\Level2a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1\Level2b.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1\SubFolderLevel2\Level3a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1\SubFolderLevel2\Level3b.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2a',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2b',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2c',                
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\Level2a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\Level2b.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2a\Level3a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2a\Level3b.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2a\Level3c.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2a\Level3d.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2b\Level3a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2b\Level3b.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2c\Level3a.txt',
            'OK\t' + os.getcwd() + r'\Tests\SD\FolderWithFileAndSeveralSubFolderLevel3\SubFolderLevel1bis\SubFolderLevel2c\Level3b.txt',   
            ]
        
        self.__testFileProcessorCopying(inputFolder, outputFolder, expectedReport)

    def __cleanTestOuput(self):     
        testOuputDirectory = os.getcwd() + r"\Tests\TestOuput" 
        try:
            shutil.rmtree(testOuputDirectory)
        except FileNotFoundError:
            pass
        os.mkdir(testOuputDirectory)

    def __testFileProcessorCopying(self, inputFolder, outputFolder, expectedReport):
            self.__cleanTestOuput()

            fileCopier = FileProcessor(inputFolder, outputFolder)
            fileCopier.Run()
            print(fileCopier.Report)
            
            actualReport = fileCopier.Report.splitlines()
            self.assertEqual(len(expectedReport), len(actualReport), "fileListReport does not contain the expected number of entries.")
            self.assertListEqual(expectedReport, actualReport, "fileListReport does not contain the expected values.")   
            
            expectedReportForDestination = [ os.getcwd() + r'\Tests\TestOuput',]
            expectedReportForDestination.extend(expectedReport)
            for i, s in enumerate(expectedReportForDestination):
                outputFolderInReport = outputFolder + "\\"
                outputFolderInReport = outputFolderInReport + os.path.split(inputFolder)[1]
                expectedReportForDestination[i] = s.replace(inputFolder, outputFolderInReport)
            expectedReportForDestination.append( os.getcwd() + r'\Tests\TestOuput\Report.txt')

            for i, s in enumerate(expectedReportForDestination):
                expectedReportForDestination[i] = s.replace('OK\t', '')

            self.__checkDirectoryTreeCopied(outputFolder, expectedReportForDestination)

    def __checkDirectoryTreeCopied(self, destinationFolder, expectedReportForDestination):       
        fileLister = FileProcessor(destinationFolder)
        fileLister.Run()
        print(fileLister.Report)
        
        actualReport = fileLister.Report.splitlines()
        actualReport.sort()
        expectedReportForDestination.sort()
        
        self.assertEqual(len(expectedReportForDestination), len(actualReport), "fileListReport does not contain the expected number of entries.")
        self.assertListEqual(expectedReportForDestination, actualReport, "fileListReport does not contain the expected values.")   

if __name__ == '__main__':
    unittest.main()